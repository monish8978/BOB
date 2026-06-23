import random
import logging
import aiohttp
from typing import Dict, Any, List
from app.redis_client import redis_manager
from app.chatbot.flows import *
from app.tasks import process_crm_ticket

from app.config import settings

logger = logging.getLogger(__name__)

async def query_rag(query_text: str) -> str | None:
    url = settings.RAG_API_URL
    data = {
        "rag_id": settings.RAG_ID,
        "query": query_text,
        "top_k": 3
    }
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(url, json=data, timeout=10) as response:
                if response.status == 200:
                    res_json = await response.json()
                    answer = res_json.get("answer")
                    if answer:
                        return answer.strip()
    except Exception as e:
        logger.error(f"Error querying RAG API: {e}")
    return None

def build_chat_response(text: str, buttons: List[Dict[str, str]] = None, quick_replies: List[Dict[str, str]] = None) -> Dict[str, Any]:
    """
    Constructs the exact AdaptiveCard structure:
    - type: "adaptiveCard"
    - responseType: ""
    - body: List of blocks (TextBlock for text, Button choice block for buttons/quick_replies)
    - actions: []
    """
    body_blocks = []
    
    # 1. Add TextBlock
    body_blocks.append({
        "type": "TextBlock",
        "text": text
    })
    
    # 2. Add choice options if buttons or quick replies are present
    choices = []
    
    if buttons:
        for b in buttons:
            btn_obj = {
                "id": b["payload"],
                "title": b["title"],
                "value": b["payload"],
                "payload": b["payload"]
            }
            choices.append(btn_obj)
            
    if quick_replies:
        for qr in quick_replies:
            qr_obj = {
                "id": qr["payload"],
                "title": qr["title"],
                "value": qr["payload"],
                "payload": qr["payload"]
            }
            choices.append(qr_obj)
            
    if choices:
        body_blocks.append({
            "type": "Button",
            "id": "serviceType",
            "style": "expanded",
            "choices": choices
        })
        
    return {
        "type": "adaptiveCard",
        "responseType": "",
        "body": body_blocks,
        "actions": []
    }

MENU_MAP = {
    "MAIN_MENU": MAIN_MENU,
    "MBOB_MENU": MBOB_MENU,
    "CARDS_MENU": CARDS_MENU,
    "CREDIT_CARD_MENU": CREDIT_CARD_MENU,
    "DEBIT_CARD_MENU": DEBIT_CARD_MENU,
    "GOBOB_MENU": GOBOB_MENU,
    "GOBOB_REG_MENU": GOBOB_REG_MENU,
    "ATS_MENU": ATS_MENU
}

def get_menu_card(menu_dict_or_id: Any, page: int = 1) -> Dict[str, Any]:
    """Translates static menus to clean responses with pagination support."""
    menu_identifier = "UNKNOWN_MENU"
    
    if isinstance(menu_dict_or_id, str):
        menu_identifier = menu_dict_or_id
        menu_dict = MENU_MAP.get(menu_identifier, {"text": "Menu not found", "buttons": []})
    else:
        menu_dict = menu_dict_or_id
        # Reverse map to find the menu identifier if not passed explicitly
        for key, val in MENU_MAP.items():
            if val is menu_dict:
                menu_identifier = key
                break
                
    all_buttons = menu_dict.get("buttons", [])
    
    if len(all_buttons) > 10:
        back_button = None
        core_buttons = []
        for b in all_buttons:
            if b["title"] in ["Main Menu", "Back to Menu"]:
                back_button = b
            else:
                core_buttons.append(b)
                
        if not back_button:
            # Fallback if no specific back button is found
            back_button = core_buttons.pop()
            
        max_per_page = 7
        total_pages = (len(core_buttons) + max_per_page - 1) // max_per_page
        start_idx = (page - 1) * max_per_page
        end_idx = start_idx + max_per_page
        
        page_buttons = core_buttons[start_idx:end_idx]
        formatted_buttons = [{"title": b["title"], "payload": b["payload"]} for b in page_buttons]
        
        if page > 1:
            formatted_buttons.append({"title": "⬅️ Previous Options", "payload": f"PAGINATE_{menu_identifier}_{page-1}"})
        if page < total_pages:
            formatted_buttons.append({"title": "More Options ➡️", "payload": f"PAGINATE_{menu_identifier}_{page+1}"})
            
        formatted_buttons.append({"title": back_button["title"], "payload": back_button["payload"]})
            
        text = menu_dict.get("text", "")
        if total_pages > 1:
            text += f" (Page {page} of {total_pages})"
            
        return build_chat_response(
            text=text,
            buttons=formatted_buttons
        )
    else:
        return build_chat_response(
            text=menu_dict.get("text", ""),
            buttons=[{"title": b["title"], "payload": b["payload"]} for b in all_buttons]
        )

def get_faq_card(faq_key: str) -> Dict[str, Any]:
    """Translates static FAQs to clean responses."""
    faq = FAQS[faq_key]
    buttons = None
    quick_replies = None
    
    if "buttons" in faq:
        buttons = [{"title": b["title"], "payload": b["payload"]} for b in faq["buttons"]]
    if "quick_replies" in faq:
        quick_replies = [{"title": q["title"], "payload": q["payload"]} for q in faq["quick_replies"]]
        
    return build_chat_response(
        text=faq["text"],
        buttons=buttons,
        quick_replies=quick_replies
    )

async def process_user_message(user_id: str, text: str, payload: str = None) -> Dict[str, Any]:
    """
    Main state machine routing incoming text or button payloads for a user session.
    Returns standard simple JSON responses matching user flow specification.
    """
    # 1. Retrieve or initialize user session state from Redis
    session = await redis_manager.get_session(user_id)
    flow = session["current_flow"]
    step = session["current_step"]
    context = session["context"]

    logger.info(f"User {user_id} - Flow: {flow}, Step: {step}, Payload: {payload}, Text: {text}")

    # Intelligent text-to-payload fallback mapping
    if not payload and text:
        normalized = text.lower().strip()
        
        # 1. Global exact matches for menu structures and actions
        EXACT_MATCHES = {
            # Main Menu navigation
            "mbob": "FLOW_MBOB",
            "mbob services": "FLOW_MBOB",
            "1. mbob": "FLOW_MBOB",
            "cards": "FLOW_CARDS",
            "card services": "FLOW_CARDS",
            "2. cards": "FLOW_CARDS",
            "update latest kyc": "FLOW_KYC",
            "kyc": "FLOW_KYC",
            "update kyc": "FLOW_KYC",
            "3. update latest kyc": "FLOW_KYC",
            "download forms": "FLOW_DOWNLOAD_FORMS",
            "forms": "FLOW_DOWNLOAD_FORMS",
            "4. download forms": "FLOW_DOWNLOAD_FORMS",
            "gobob": "FLOW_GOBOB",
            "gobob app": "FLOW_GOBOB",
            "5. gobob": "FLOW_GOBOB",
            "annual travel scheme (ats)": "FLOW_ATS",
            "ats": "FLOW_ATS",
            "6. annual travel scheme (ats)": "FLOW_ATS",
            "bob account opening": "FLOW_LOANS_ACCTS",
            "account opening": "FLOW_LOANS_ACCTS",
            "7. bob account opening": "FLOW_LOANS_ACCTS",
            "bob loan apply online": "FLOW_LOAN_APPLY",
            "apply loan": "FLOW_LOAN_APPLY",
            "loan": "FLOW_LOAN_APPLY",
            "8. bob loan apply online": "FLOW_LOAN_APPLY",
            
            # Common/Standard Action words
            "home": "MAIN_MENU",
            "main menu": "MAIN_MENU",
            "back menu": "MAIN_MENU",
            "back to main menu": "MAIN_MENU",
            "create ticket": "RESOLVED_NO",
            "no": "RESOLVED_NO",
            "still facing issue": "RESOLVED_NO",
            
            # GoBoB menu options
            "what is gobob": "GOBOB_FAQ_WHAT",
            "login access blocked": "GOBOB_BLOCKED",
            "registration options": "GOBOB_REG_MENU",
            "lost device block": "GOBOB_LOST",
            "charges": "GOBOB_CHARGES",
            "qr scan": "GOBOB_QR",
            "deactivate gobob": "GOBOB_DEACTIVATE",
            "wallet refund request": "GOBOB_REFUND",
            "customer limit category": "GOBOB_LIMIT",
            
            # GoBoB Registration options
            "general registration": "GOBOB_REG",
            "how to register": "GOBOB_HOW_TO_REG",
            "registration for tourist": "GOBOB_TOURIST",
            "tourist kyc verification": "GOBOB_TOURIST_KYC",
            
            # Cards general
            "debit card": "CARD_DEBIT",
            "credit card": "CARD_CREDIT",
        }
        
        if normalized in EXACT_MATCHES:
            payload = EXACT_MATCHES[normalized]
            
        # 2. Flow-specific exact keyword matches
        else:
            if flow == "cards_debit":
                flow_matches = {
                    "limit": "DC_LIMIT_DOM",
                    "debit card limit": "DC_LIMIT_DOM",
                    "fraud": "DC_FRAUD",
                    "unauthorized": "DC_FRAUD",
                    "eligibility": "DC_ELIGIBILITY_DOM",
                    "issuance": "DC_ISSUANCE_FEE",
                    "issuance fee": "DC_ISSUANCE_FEE",
                    "replacement": "DC_REPLACEMENT_FEE",
                    "replacement fee": "DC_REPLACEMENT_FEE",
                    "block": "DC_BLOCK",
                    "activate": "DC_ACTIVATE",
                }
                if normalized in flow_matches:
                    payload = flow_matches[normalized]
                    
            elif flow == "cards_credit":
                flow_matches = {
                    "limit": "CC_LIMIT",
                    "credit card limit": "CC_LIMIT",
                    "fraud": "CC_FRAUD",
                    "unauthorized": "CC_FRAUD",
                    "eligibility": "CC_ELIGIBILITY",
                    "issuance": "CC_ISSUANCE_FEE",
                    "issuance fee": "CC_ISSUANCE_FEE",
                    "annual": "CC_ANNUAL_FEE",
                    "annual fee": "CC_ANNUAL_FEE",
                    "replacement": "CC_REPLACEMENT_FEE",
                    "replacement fee": "CC_REPLACEMENT_FEE",
                    "bill": "CC_BILL",
                    "block": "CC_BLOCK",
                    "activate": "CC_ACTIVATE",
                }
                if normalized in flow_matches:
                    payload = flow_matches[normalized]
                    
            elif flow == "gobob":
                flow_matches = {
                    "limit": "GOBOB_LIMIT",
                    "kyc": "GOBOB_KYC",
                    "registration": "GOBOB_REG",
                    "register": "GOBOB_HOW_TO_REG",
                    "blocked": "GOBOB_BLOCKED",
                    "lost": "GOBOB_LOST",
                    "refund": "GOBOB_REFUND",
                }
                if normalized in flow_matches:
                    payload = flow_matches[normalized]
                    
            elif flow == "ats":
                flow_matches = {
                    "limit": "ATS_FAQ_LIMIT",
                    "expiry": "ATS_FAQ_EXPIRY",
                    "minor": "ATS_FAQ_MINOR",
                    "card": "ATS_FAQ_CARD",
                    "cash": "ATS_CASH",
                    "avail": "ATS_AVAIL",
                }
                if normalized in flow_matches:
                    payload = flow_matches[normalized]
                    
            # 3. Fallback general exact matches (when flow is not set or not specific)
            if not payload:
                general_matches = {
                    "registration": "MBOB_REGISTRATION",
                    "register": "MBOB_REGISTRATION",
                    "blocked": "MBOB_LOGIN_BLOCKED",
                    "forgot": "MBOB_LOGIN_BLOCKED",
                    "unlock": "MBOB_LOGIN_BLOCKED",
                    "failed": "MBOB_TX_FAILED",
                    "transfer failed": "MBOB_TX_FAILED",
                    "device": "MBOB_DEVICE_CHANGE",
                    "limit": "MBOB_LIMIT",
                    "category": "MBOB_CATEGORY",
                    "change category": "MBOB_CATEGORY",
                }
                if normalized in general_matches:
                    payload = general_matches[normalized]

    # Pagination Payload Handler
    if payload and payload.startswith("PAGINATE_"):
        parts = payload.split("_")
        page_num = int(parts[-1])
        menu_id = "_".join(parts[1:-1])
        return get_menu_card(menu_id, page=page_num)

    # Standard "Reset/Main Menu" payload handlers
    if payload == "MAIN_MENU" or text.lower() in ["home", "main menu", "hi", "hello", "start"]:
        await redis_manager.clear_session(user_id)
        return get_menu_card(MAIN_MENU)

    # Global FAQ Payload Handler
    if payload in FAQS:
        return get_faq_card(payload)

    # Trigger support ticket creation
    if payload == "RESOLVED_NO" or text.lower() in ["create ticket", "ticket", "no", "still facing issue", "create ticket / talk to support", "create support ticket"]:
        await redis_manager.clear_session(user_id)
        return build_chat_response(
            text="Please click the button below to open the support portal in your browser.",
            buttons=[
                {"title": "Open Support Portal", "payload": settings.BOB_SUPPORT_URL},
                {"title": "Main Menu", "payload": "MAIN_MENU"}
            ]
        )

    # RAG Integration for free-text questions
    if not payload and text and flow != "ticket_creation":
        rag_answer = await query_rag(text)
        if rag_answer:
            return build_chat_response(
                text=rag_answer,
                buttons=[
                    {"title": "Main Menu", "payload": "MAIN_MENU"}
                    # {"title": "Still Facing Issue", "payload": "RESOLVED_NO"}
                ]
            )

    # ==========================================
    # FLOW: MAIN MENU TRANSITIONS
    # ==========================================
    if flow == "main_menu" or step == "start":
        if payload == "FLOW_MBOB":
            await redis_manager.update_session(user_id, flow="mbob", step="menu")
            return get_menu_card(MBOB_MENU)
        elif payload == "FLOW_CARDS":
            await redis_manager.update_session(user_id, flow="cards", step="menu")
            return get_menu_card(CARDS_MENU)
        elif payload == "FLOW_KYC":
            return build_chat_response(
                text="""**Update your Latest KYC (Mobile, Email, Address, etc.)**

To keep your details updated with the bank, please fill in the following forms and submit them at your nearest branch:
1. **Customer Information Change Form**
2. **Customer Information Update Form**
3. **mBoB Change Request Form**

**If you are abroad:**
- Please email the first two forms (**Customer Information Change & Update Forms**) to 📧 operations@bob.bt
- Please email the **mBoB Change Request Form** to 📧 mbob@bob.bt
*(Note: Please send the emails from your registered email address).*
""",
                buttons=[
                    {"title": "Open Website", "payload": settings.BOB_WEBSITE_URL},
                    {"title": "Main Menu", "payload": "MAIN_MENU"}
                ]
            )
        elif payload == "FLOW_DOWNLOAD_FORMS":
            return build_chat_response(
                text="""**Download Forms**

To download forms, please click the link below:""",
                buttons=[
                    {"title": "Download Forms", "payload": settings.BOB_DOWNLOAD_FORMS_URL},
                    {"title": "Main Menu", "payload": "MAIN_MENU"}
                ]
            )
        elif payload == "FLOW_GOBOB":
            await redis_manager.update_session(user_id, flow="gobob", step="menu")
            return get_menu_card(GOBOB_MENU)
        elif payload == "FLOW_ATS":
            await redis_manager.update_session(user_id, flow="ats", step="menu")
            return get_menu_card(ATS_MENU)
        elif payload == "FLOW_LOANS_ACCTS":
            return build_chat_response(
                text="Savings account can be opened online via BoB website.\n\nSteps:\n\nUpdate NDI App details\nShare details with BoB\nFill form\nSubmit",
                buttons=[
                    {"title": "Open Account Portal", "payload": "ACCT_PORTAL_OPEN"},
                    {"title": "Main Menu", "payload": "MAIN_MENU"}
                ]
            )
        elif payload == "FLOW_LOAN_APPLY":
            await redis_manager.update_session(user_id, flow="loan_apply", step="awaiting_customer_type")
            return build_chat_response(
                text="Select loan type and apply online.",
                buttons=[
                    {"title": "New Customer", "payload": "LOAN_CUST_NEW"},
                    {"title": "Existing Customer", "payload": "LOAN_CUST_EXISTING"},
                    {"title": "Main Menu", "payload": "MAIN_MENU"}
                ]
            )
        else:
            return get_menu_card(MAIN_MENU)

    # ==========================================
    # FLOW: mBoB
    # ==========================================
    elif flow == "mbob":
        if payload == "FLOW_MBOB":
            return get_menu_card(MBOB_MENU)
        elif payload in FAQS:
            return get_faq_card(payload)
        else:
            return get_menu_card(MBOB_MENU)

    # ==========================================
    # FLOW: CARDS
    # ==========================================
    elif flow == "cards":
        if payload == "FLOW_CARDS":
            return get_menu_card(CARDS_MENU)
        elif payload == "CARD_CREDIT":
            await redis_manager.update_session(user_id, flow="cards_credit", step="menu")
            return get_menu_card(CREDIT_CARD_MENU)
        elif payload == "CARD_DEBIT":
            await redis_manager.update_session(user_id, flow="cards_debit", step="menu")
            return get_menu_card(DEBIT_CARD_MENU)
        else:
            return get_menu_card(CARDS_MENU)

    elif flow == "cards_credit":
        if payload == "FLOW_CARDS":
            await redis_manager.update_session(user_id, flow="cards", step="menu")
            return get_menu_card(CARDS_MENU)
        elif payload in FAQS:
            return get_faq_card(payload)
        else:
            return get_menu_card(CREDIT_CARD_MENU)

    elif flow == "cards_debit":
        if payload == "FLOW_CARDS":
            await redis_manager.update_session(user_id, flow="cards", step="menu")
            return get_menu_card(CARDS_MENU)
        elif payload in FAQS:
            return get_faq_card(payload)
        else:
            return get_menu_card(DEBIT_CARD_MENU)

    # ==========================================
    # FLOW: GOBOB
    # ==========================================
    elif flow == "gobob":
        if payload == "GOBOB_REG_MENU":
            return get_menu_card(GOBOB_REG_MENU)
        elif payload in FAQS:
            return get_faq_card(payload)
        else:
            return get_menu_card(GOBOB_MENU)

    # ==========================================
    # FLOW: ATS
    # ==========================================
    elif flow == "ats":
        if payload in FAQS:
            return get_faq_card(payload)
        else:
            return get_menu_card(ATS_MENU)

    # ==========================================
    # FLOW: LOAN APPLICATION
    # ==========================================
    elif flow == "loan_apply":
        if payload in ["LOAN_CUST_NEW", "LOAN_CUST_EXISTING"]:
            cust_status = "New" if payload == "LOAN_CUST_NEW" else "Existing"
            await redis_manager.clear_session(user_id)
            return build_chat_response(
                text=f"Formal online loan portal redirection configured for {cust_status} Customer.",
                buttons=[
                    {"title": "Apply Loan", "payload": "LOAN_PORTAL_OPEN"},
                    {"title": "Main Menu", "payload": "MAIN_MENU"}
                ]
            )



    # Default fallback
    await redis_manager.clear_session(user_id)
    return get_menu_card(MAIN_MENU)
