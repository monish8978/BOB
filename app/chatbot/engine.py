import random
import logging
from typing import Dict, Any, List
from app.redis_client import redis_manager
from app.chatbot.flows import *
from app.tasks import process_crm_ticket

logger = logging.getLogger(__name__)

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
            choices.append({
                "id": b["payload"],
                "title": b["title"],
                "value": b["title"]
            })
            
    if quick_replies:
        for qr in quick_replies:
            choices.append({
                "id": qr["payload"],
                "title": qr["title"],
                "value": qr["title"]
            })
            
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

def get_menu_card(menu_dict: Dict[str, Any]) -> Dict[str, Any]:
    """Translates static menus to clean responses."""
    return build_chat_response(
        text=menu_dict["text"],
        buttons=[{"title": b["title"], "payload": b["payload"]} for b in menu_dict["buttons"]]
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
        if normalized in ["mbob", "mbob services", "1. mbob"]:
            payload = "FLOW_MBOB"
        elif normalized in ["cards", "card services", "2. cards"]:
            payload = "FLOW_CARDS"
        elif normalized in ["update latest kyc", "kyc", "update kyc", "3. update latest kyc"]:
            payload = "FLOW_KYC"
        elif normalized in ["download forms", "forms", "4. download forms"]:
            payload = "FLOW_DOWNLOAD_FORMS"
        elif normalized in ["gobob", "gobob app", "5. gobob"]:
            payload = "FLOW_GOBOB"
        elif normalized in ["annual travel scheme (ats)", "ats", "6. annual travel scheme (ats)"]:
            payload = "FLOW_ATS"
        elif normalized in ["bob account opening", "account opening", "7. bob account opening"]:
            payload = "FLOW_LOANS_ACCTS"
        elif normalized in ["bob loan apply online", "apply loan", "loan", "8. bob loan apply online"]:
            payload = "FLOW_LOAN_APPLY"
        elif "registration" in normalized or "register" in normalized:
            payload = "GOBOB_REG" if flow == "gobob" else "MBOB_REGISTRATION"
        elif "blocked" in normalized or "forgot" in normalized or "unlock" in normalized:
            payload = "GOBOB_BLOCKED" if flow == "gobob" else "MBOB_LOGIN_BLOCKED"
        elif "failed" in normalized or "transfer failed" in normalized:
            payload = "MBOB_TX_FAILED"
        elif "device" in normalized:
            payload = "GOBOB_LOST" if "lost" in normalized else "MBOB_DEVICE_CHANGE"
        elif "limit" in normalized:
            if flow == "cards_credit":
                payload = "CC_LIMIT"
            elif flow == "cards_debit":
                payload = "DC_LIMIT"
            elif flow == "ats":
                payload = "ATS_FAQ_LIMIT"
            elif flow == "gobob":
                payload = "GOBOB_LIMIT"
            else:
                payload = "MBOB_LIMIT"
        elif "category" in normalized or "change category" in normalized:
            payload = "MBOB_CATEGORY"
        elif "fraud" in normalized or "unauthorized" in normalized:
            payload = "DC_FRAUD" if flow == "cards_debit" else "CC_FRAUD"
        elif "eligibility" in normalized:
            payload = "DC_ELIGIBILITY" if flow == "cards_debit" else "CC_ELIGIBILITY"
        elif "issuance" in normalized:
            payload = "DC_ISSUANCE_FEE" if flow == "cards_debit" else "CC_ISSUANCE_FEE"
        elif "annual" in normalized:
            payload = "CC_ANNUAL_FEE"
        elif "replacement" in normalized or "renewal" in normalized:
            payload = "DC_REPLACEMENT_FEE" if flow == "cards_debit" else "CC_REPLACEMENT_FEE"
        elif "bill" in normalized:
            payload = "CC_BILL"
        elif "block" in normalized:
            payload = "DC_BLOCK" if flow == "cards_debit" else "CC_BLOCK"
        elif "activate" in normalized:
            payload = "DC_ACTIVATE" if flow == "cards_debit" else "CC_ACTIVATE"
        elif "kyc" in normalized:
            payload = "GOBOB_KYC" if flow == "gobob" else "FLOW_KYC"
        elif "download" in normalized or "forms" in normalized:
            payload = "FLOW_DOWNLOAD_FORMS"
        elif "gobob" in normalized:
            payload = "FLOW_GOBOB"
        elif "ats" in normalized:
            if "expiry" in normalized:
                payload = "ATS_FAQ_EXPIRY"
            elif "minor" in normalized:
                payload = "ATS_FAQ_MINOR"
            elif "card" in normalized:
                payload = "ATS_FAQ_CARD"
            elif "cash" in normalized:
                payload = "ATS_CASH"
            elif "avail" in normalized:
                payload = "ATS_AVAIL"
            else:
                payload = "FLOW_ATS"
        elif "opening" in normalized or "account opening" in normalized:
            payload = "FLOW_LOANS_ACCTS"
        elif "loan" in normalized or "apply loan" in normalized:
            payload = "FLOW_LOAN_APPLY"

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
                {"title": "Open Support Portal", "payload": "https://www.c-zentrix.com/"},
                {"title": "Back to Main Menu", "payload": "MAIN_MENU"}
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
                    {"title": "Open Website", "payload": "https://www.bob.bt/"},
                    {"title": "Back Menu", "payload": "MAIN_MENU"}
                ]
            )
        elif payload == "FLOW_DOWNLOAD_FORMS":
            return build_chat_response(
                text="""**Download Forms**

To download forms, please click the link below:""",
                buttons=[
                    {"title": "Download Forms", "payload": "https://www.bob.bt/service-and-support/download-forms/"},
                    {"title": "Back Menu", "payload": "MAIN_MENU"}
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
                    {"title": "Back Menu", "payload": "MAIN_MENU"}
                ]
            )
        elif payload == "FLOW_LOAN_APPLY":
            await redis_manager.update_session(user_id, flow="loan_apply", step="awaiting_customer_type")
            return build_chat_response(
                text="Select loan type and apply online.",
                buttons=[
                    {"title": "New Customer", "payload": "LOAN_CUST_NEW"},
                    {"title": "Existing Customer", "payload": "LOAN_CUST_EXISTING"},
                    {"title": "Back Menu", "payload": "MAIN_MENU"}
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
        if payload in FAQS:
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
                    {"title": "Back Menu", "payload": "MAIN_MENU"}
                ]
            )

    # ==========================================
    # FLOW: TICKET CREATION (CRM)
    # ==========================================
    elif flow == "ticket_creation":
        if step == "awaiting_ticket_name":
            customer_name = text.strip()
            if len(customer_name) > 2:
                await redis_manager.update_session(user_id, step="awaiting_ticket_mobile", context_update={"customer_name": customer_name})
                return build_chat_response(
                    text="Please enter your active Mobile Number:"
                )
            else:
                return build_chat_response(
                    text="Name is too short. Please type your Full Name:"
                )
        
        elif step == "awaiting_ticket_mobile":
            mobile = text.strip()
            if mobile.isdigit() and len(mobile) >= 7:
                await redis_manager.update_session(user_id, step="awaiting_ticket_issue", context_update={"mobile_number": mobile})
                buttons = [
                    {"title": "mBoB App Issue", "payload": "TKT_ISSUE_MBOB"},
                    {"title": "Card Blocked/Failed", "payload": "TKT_ISSUE_CARDS"},
                    {"title": "KYC Form Processing", "payload": "TKT_ISSUE_KYC"},
                    {"title": "GoBoB Wallet Support", "payload": "TKT_ISSUE_GOBOB"},
                    {"title": "Other Banking Inquiries", "payload": "TKT_ISSUE_OTHER"}
                ]
                return build_chat_response(
                    text="What category does your issue fall under? Please select a category:",
                    buttons=buttons
                )
            else:
                return build_chat_response(
                    text="Invalid mobile number. Please enter digits only (minimum 7 characters):"
                )
        
        elif step == "awaiting_ticket_issue":
            issue_map = {
                "TKT_ISSUE_MBOB": "mBoB App",
                "TKT_ISSUE_CARDS": "Cards",
                "TKT_ISSUE_KYC": "KYC Processing",
                "TKT_ISSUE_GOBOB": "GoBoB Wallet",
                "TKT_ISSUE_OTHER": "Other Services"
            }
            issue_selected = issue_map.get(payload, text.strip())
            await redis_manager.update_session(user_id, step="awaiting_ticket_sub_category", context_update={"issue_type": issue_selected})
            return build_chat_response(
                text="Please type your Issue Sub Category (e.g. MPIN Lock, OTP Delay, Transaction Failure):"
            )
        
        elif step == "awaiting_ticket_sub_category":
            sub_category = text.strip()
            await redis_manager.update_session(user_id, step="awaiting_ticket_description", context_update={"sub_category": sub_category})
            return build_chat_response(
                text="Finally, please provide a detailed Problem Description of your issue:"
            )
        
        elif step == "awaiting_ticket_description":
            description = text.strip()
            ticket_num = random.randint(100000, 999999)
            ticket_id = f"BOB-TKT-{ticket_num}"

            ticket_data = {
                "ticket_id": ticket_id,
                "user_id": user_id,
                "customer_name": context["customer_name"],
                "mobile_number": context["mobile_number"],
                "issue_type": context["issue_type"],
                "category": context["issue_type"], # Unified
                "sub_category": context["sub_category"],
                "description": description
            }
            
            try:
                process_crm_ticket.delay(ticket_data)
                celery_status = "successfully queued for processing."
            except Exception as e:
                logger.error(f"Failed to queue Celery task: {e}")
                celery_status = "logged directly in system database."

            await redis_manager.clear_session(user_id)
            return build_chat_response(
                text=f"Your request has been registered successfully.\nTicket ID: {ticket_id}\nOur support team will contact you shortly.",
                buttons=[{"title": "Return to Main Menu", "payload": "MAIN_MENU"}]
            )

    # Default fallback
    await redis_manager.clear_session(user_id)
    return get_menu_card(MAIN_MENU)
