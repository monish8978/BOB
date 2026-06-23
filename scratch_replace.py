import os

filepath = r"D:\BOB\app\chatbot\engine.py"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

old_def = """def get_menu_card(menu_dict: Dict[str, Any]) -> Dict[str, Any]:
    \"\"\"Translates static menus to clean responses.\"\"\"
    return build_chat_response(
        text=menu_dict[\"text\"],
        buttons=[{\"title\": b[\"title\"], \"payload\": b[\"payload\"]} for b in menu_dict[\"buttons\"]]
    )"""

new_def = """MENU_MAP = {
    "MAIN_MENU": MAIN_MENU,
    "MBOB_MENU": MBOB_MENU,
    "CARDS_MENU": CARDS_MENU,
    "CREDIT_CARD_MENU": CREDIT_CARD_MENU,
    "DEBIT_CARD_MENU": DEBIT_CARD_MENU,
    "GOBOB_MENU": GOBOB_MENU,
    "GOBOB_REG_MENU": GOBOB_REG_MENU,
    "ATS_MENU": ATS_MENU
}

def get_menu_card(menu_identifier: str, page: int = 1) -> Dict[str, Any]:
    \"\"\"Translates static menus to clean responses with pagination.\"\"\"
    menu_dict = MENU_MAP.get(menu_identifier)
    if not menu_dict:
        if isinstance(menu_identifier, dict):
            menu_dict = menu_identifier
        else:
            return build_chat_response(text="Menu not found.")
            
    all_buttons = menu_dict["buttons"]
    
    if len(all_buttons) > 10:
        max_per_page = 9
        total_pages = (len(all_buttons) + max_per_page - 1) // max_per_page
        start_idx = (page - 1) * max_per_page
        end_idx = start_idx + max_per_page
        
        page_buttons = all_buttons[start_idx:end_idx]
        formatted_buttons = [{"title": b["title"], "payload": b["payload"]} for b in page_buttons]
        
        if page < total_pages:
            formatted_buttons.append({"title": "More Options ➡️", "payload": f"PAGINATE_{menu_identifier}_{page+1}"})
        if page > 1:
            formatted_buttons.append({"title": "⬅️ Previous Options", "payload": f"PAGINATE_{menu_identifier}_{page-1}"})
            
        text = menu_dict["text"]
        if total_pages > 1:
            text += f" (Page {page} of {total_pages})"
            
        return build_chat_response(
            text=text,
            buttons=formatted_buttons
        )
    else:
        return build_chat_response(
            text=menu_dict["text"],
            buttons=[{"title": b["title"], "payload": b["payload"]} for b in all_buttons]
        )"""

content = content.replace(old_def, new_def)

old_handler = """    # Standard \"Reset/Main Menu\" payload handlers
    if payload == \"MAIN_MENU\" or text.lower() in [\"home\", \"main menu\", \"hi\", \"hello\", \"start\"]:"""

new_handler = """    # Pagination Payload Handler
    if payload and payload.startswith("PAGINATE_"):
        parts = payload.split("_")
        page_num = int(parts[-1])
        menu_id = "_".join(parts[1:-1])
        return get_menu_card(menu_id, page=page_num)

    # Standard \"Reset/Main Menu\" payload handlers
    if payload == \"MAIN_MENU\" or text.lower() in [\"home\", \"main menu\", \"hi\", \"hello\", \"start\"]:"""

content = content.replace(old_handler, new_handler)

menus = ["MAIN_MENU", "MBOB_MENU", "CARDS_MENU", "CREDIT_CARD_MENU", "DEBIT_CARD_MENU", "GOBOB_MENU", "GOBOB_REG_MENU", "ATS_MENU"]
for menu in menus:
    content = content.replace(f"get_menu_card({menu})", f"get_menu_card('{menu}')")

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)

print("File updated successfully!")
