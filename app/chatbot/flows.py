# BOB Bank Chatbot Static Menus and FAQ Responses (Spec-Aligned Copy)

# Main Menu Options
MAIN_MENU = {
    "text": "Welcome to Bank of Bhutan Assistant.\nPlease choose an option below to continue.",
    "buttons": [
        {"title": "mBoB", "payload": "FLOW_MBOB"},
        {"title": "Cards", "payload": "FLOW_CARDS"},
        {"title": "Update Latest KYC", "payload": "FLOW_KYC"},
        {"title": "Download Forms", "payload": "FLOW_DOWNLOAD_FORMS"},
        {"title": "GoBoB", "payload": "FLOW_GOBOB"},
        {"title": "Annual Travel Scheme (ATS)", "payload": "FLOW_ATS"},
        {"title": "BOB Account Opening", "payload": "FLOW_LOANS_ACCTS"},
        {"title": "BOB Loan Apply Online", "payload": "FLOW_LOAN_APPLY"},
        {"title": "Create Ticket / Talk to Support", "payload": "RESOLVED_NO"},
    ]
}

# mBoB Menu
MBOB_MENU = {
    "text": "Please select your mBoB concern.",
    "buttons": [
        {"title": "Registration", "payload": "MBOB_REGISTRATION"},
        {"title": "Login Access Blocked", "payload": "MBOB_LOGIN_BLOCKED"},
        {"title": "Fund Transfer Failed to Other Banks", "payload": "MBOB_TX_FAILED"},
        {"title": "Device Change", "payload": "MBOB_DEVICE_CHANGE"},
        {"title": "Fund Transfer Limit", "payload": "MBOB_LIMIT"},
        {"title": "Check/Change Fund Transfer Category", "payload": "MBOB_CATEGORY"}
    ]
}

# Cards Menu
CARDS_MENU = {
    "text": "Please select card type.",
    "buttons": [
        {"title": "Credit Card", "payload": "CARD_CREDIT"},
        {"title": "Debit Card", "payload": "CARD_DEBIT"},
        {"title": "Back Menu", "payload": "MAIN_MENU"}
    ]
}

# Credit Card Menu
CREDIT_CARD_MENU = {
    "text": "Please select your credit card concern.",
    "buttons": [
        {"title": "Unauthorized/Fraud Transactions", "payload": "CC_FRAUD"},
        {"title": "Eligibility", "payload": "CC_ELIGIBILITY"},
        {"title": "Types of Credit Card", "payload": "CC_TYPES"},
        {"title": "Issuance Fee", "payload": "CC_ISSUANCE_FEE"},
        {"title": "Annual Fee", "payload": "CC_ANNUAL_FEE"},
        {"title": "Replacement/Renewal Fee", "payload": "CC_REPLACEMENT_FEE"},
        {"title": "Credit Card Limit", "payload": "CC_LIMIT"},
        {"title": "Credit Card Bill", "payload": "CC_BILL"},
        {"title": "Block Credit Card", "payload": "CC_BLOCK"},
        {"title": "Activate Credit Card", "payload": "CC_ACTIVATE"},
        {"title": "Back Menu", "payload": "FLOW_CARDS"}
    ]
}

# Debit Card Menu
DEBIT_CARD_MENU = {
    "text": "Please select your debit card concern.",
    "buttons": [
        {"title": "Card Issuance Fee", "payload": "DC_ISSUANCE_FEE"},
        {"title": "Replacement/Renewal Fee", "payload": "DC_REPLACEMENT_FEE"},
        {"title": "Fraud Transaction", "payload": "DC_FRAUD"},
        {"title": "Card Types", "payload": "DC_TYPES"},
        {"title": "Eligibility", "payload": "DC_ELIGIBILITY"},
        {"title": "Withdrawal Limit", "payload": "DC_LIMIT"},
        {"title": "New Card Request", "payload": "DC_NEW_REQUEST"},
        {"title": "Block Debit Card", "payload": "DC_BLOCK"},
        {"title": "Activate Debit Card", "payload": "DC_ACTIVATE"},
        {"title": "Back Menu", "payload": "FLOW_CARDS"}
    ]
}

# GoBoB Menu
GOBOB_MENU = {
    "text": "Please select your GoBoB concern.",
    "buttons": [
        {"title": "What is GoBoB", "payload": "GOBOB_FAQ_WHAT"},
        {"title": "Login Access Blocked", "payload": "GOBOB_BLOCKED"},
        {"title": "Registration", "payload": "GOBOB_REG"},
        {"title": "Registration for Tourist", "payload": "GOBOB_TOURIST"},
        {"title": "KYC Verification", "payload": "GOBOB_KYC"},
        {"title": "Lost Device Block", "payload": "GOBOB_LOST"},
        {"title": "Charges", "payload": "GOBOB_CHARGES"},
        {"title": "QR Scan", "payload": "GOBOB_QR"},
        {"title": "Deactivate GoBoB", "payload": "GOBOB_DEACTIVATE"},
        {"title": "Wallet Refund Request", "payload": "GOBOB_REFUND"},
        {"title": "Customer Limit Category", "payload": "GOBOB_LIMIT"},
        {"title": "Back Menu", "payload": "MAIN_MENU"}
    ]
}

# ATS Menu
ATS_MENU = {
    "text": "Please select your ATS concern.",
    "buttons": [
        {"title": "What is ATS", "payload": "ATS_FAQ_WHAT"},
        {"title": "Avail ATS", "payload": "ATS_AVAIL"},
        {"title": "ATS Limit", "payload": "ATS_FAQ_LIMIT"},
        {"title": "ATS Cash", "payload": "ATS_CASH"},
        {"title": "ATS Add to Card", "payload": "ATS_FAQ_CARD"},
        {"title": "ATS for Minor", "payload": "ATS_FAQ_MINOR"},
        {"title": "ATS Expiry", "payload": "ATS_FAQ_EXPIRY"},
        {"title": "Back Menu", "payload": "MAIN_MENU"}
    ]
}

# Static FAQ Content (Aligned to copy specifications)
FAQS = {
    # mBoB Registration Information
    "MBOB_REGISTRATION": {
        "text": "An account with Bank of Bhutan and registered Mobile/Email address is required to avail this service.\nFor thumb print account, please visit nearest BoB branch for registration.\n\nFor accounts with signature, follow below steps:\n\nTap Sign-Up option on mBoB app\nEnter:\nBoB Account Number\nCID / License / Work Permit / Passport Number\nClick Submit\nAccept Terms & Conditions\nOTP will be sent to registered mobile & email\nEnter OTP\nUser ID & MPIN will be generated.",
        "buttons": [
            {"title": "Back to mBoB Menu", "payload": "FLOW_MBOB"},
            {"title": "Create Ticket", "payload": "RESOLVED_NO"}
        ]
    },
    
    # mBoB Login Access Blocked
    "MBOB_LOGIN_BLOCKED": {
        "text": "To reset MPIN or unblock login access:\n\nOpen mBoB App\nTap Forgot option\nEnter:\nUser ID\nRegistered Mobile Number\nCID Number\nOTP will be sent on registered email/mobile\nEnter OTP\nNew MPIN will be sent\nLogin using New MPIN\nSet new MPIN.",
        "buttons": [
            {"title": "Still Facing Issue", "payload": "RESOLVED_NO"},
            {"title": "Back Menu", "payload": "FLOW_MBOB"}
        ]
    },
    
    # mBoB Fund Transfer Failed to Other Banks
    "MBOB_TX_FAILED": {
        "text": "As per RMA and force credit policy, all interbank failed transactions are credited to beneficiary account on the next working day if beneficiary account is valid and active.",
        "buttons": [
            {"title": "Create Ticket", "payload": "RESOLVED_NO"},
            {"title": "Back Menu", "payload": "FLOW_MBOB"}
        ]
    },
    
    # mBoB Device Change
    "MBOB_DEVICE_CHANGE": {
        "text": "An mBoB user can only access mBoB from one device at a time.\n\nIf changed device:\n\nWithin Bhutan\n📞 1095\n\nOutside Bhutan\n📞 +975-2-349903\n\n📧 mbob@bob.bt",
        "buttons": [
            {"title": "Create Ticket", "payload": "RESOLVED_NO"},
            {"title": "Back Menu", "payload": "FLOW_MBOB"}
        ]
    },
    
    # mBoB Fund Transfer Limit
    "MBOB_LIMIT": {
        "text": "Within BoB Accounts\n\nGold Category: Unlimited\nSilver Category: Nu.500,000/day\nGeneral Category: Nu.100,000/day\n\nThumbprint Account\n\nDaily Limit: Nu.5,000\nTransaction Limit: Nu.3,000\n\nOther Banks\n\nNu.1 Million/day",
        "buttons": [
            {"title": "Back Menu", "payload": "FLOW_MBOB"}
        ]
    },
    
    # mBoB Check/Change Fund Transfer Category
    "MBOB_CATEGORY": {
        "text": "To check/change your fund transfer category:\n\nLogin mBoB\nOpen Menu\nTap Change Category\nView current category\nChange category",
        "buttons": [
            {"title": "Back Menu", "payload": "FLOW_MBOB"}
        ]
    },

    # CREDIT CARD SPECS
    "CC_FRAUD": {
        "text": "Unauthorized or Fraud Transactions\n\nIf you notice any unauthorized or fraud transaction on your Credit Card, please lock it immediately via mBoB app or call 1095 to block the card permanently.",
        "buttons": [{"title": "Back Menu", "payload": "CARD_CREDIT"}]
    },
    "CC_ELIGIBILITY": {
        "text": "Credit Card Eligibility\n\nMust be a Bhutanese citizen or resident between 18 and 65 years of age, holding an active account with Bank of Bhutan showing stable source of income.",
        "buttons": [{"title": "Back Menu", "payload": "CARD_CREDIT"}]
    },
    "CC_TYPES": {
        "text": "Types of Credit Card\n\nWe offer Gold, Silver, and Classic Credit Cards, tailored for local, domestic, and international usage limits.",
        "buttons": [{"title": "Back Menu", "payload": "CARD_CREDIT"}]
    },
    "CC_ISSUANCE_FEE": {
        "text": "Issuance Fee\n\nCredit Card Issuance Fee:\n- Classic Card: Nu. 500\n- Silver Card: Nu. 1,000\n- Gold Card: Nu. 1,500",
        "buttons": [{"title": "Back Menu", "payload": "CARD_CREDIT"}]
    },
    "CC_ANNUAL_FEE": {
        "text": "Annual Fee\n\nCredit Card Annual Maintenance Fee is Nu. 1,000 for standard accounts, charged at the end of every calendar year.",
        "buttons": [{"title": "Back Menu", "payload": "CARD_CREDIT"}]
    },
    "CC_REPLACEMENT_FEE": {
        "text": "Replacement/Renewal Fee\n\nCard replacement or renewal due to damage, loss, or expiry is Nu. 500.",
        "buttons": [{"title": "Back Menu", "payload": "CARD_CREDIT"}]
    },
    "CC_LIMIT": {
        "text": "Credit Card Limit\n\nYour credit card limit is determined during credit analysis based on income tax returns and salary statements.",
        "buttons": [{"title": "Back Menu", "payload": "CARD_CREDIT"}]
    },
    "CC_BILL": {
        "text": "Credit Card Bill\n\nBills are generated on a monthly cycle. You can pay your outstanding amount via standing instruction (ATS) or manually through mBoB.",
        "buttons": [{"title": "Back Menu", "payload": "CARD_CREDIT"}]
    },
    
    # Credit Card Block
    "CC_BLOCK": {
        "text": "To block your card:\n\nCall 1095\n\nOR\n\nLogin mBoB → Cards → Select Card → Manage Card → Card Controls → Turn OFF ATM/POS/Online transaction.",
        "buttons": [
            {"title": "Create Ticket", "payload": "RESOLVED_NO"},
            {"title": "Back Menu", "payload": "CARD_CREDIT"}
        ]
    },
    
    # Credit Card Activate
    "CC_ACTIVATE": {
        "text": "Login mBoB → Cards → Credit Card → Activate → Set Card PIN → Submit.",
        "buttons": [
            {"title": "Back Menu", "payload": "CARD_CREDIT"}
        ]
    },

    # DEBIT CARD SPECS
    "DC_ISSUANCE_FEE": {
        "text": "Card Issuance Fee\n\nStandard Debit Card issuance fee is Nu. 250 upon first time account creation.",
        "buttons": [{"title": "Back Menu", "payload": "CARD_DEBIT"}]
    },
    "DC_REPLACEMENT_FEE": {
        "text": "Replacement/Renewal Fee\n\nReplacement of lost, stolen, or damaged Debit Card is Nu. 250.",
        "buttons": [{"title": "Back Menu", "payload": "CARD_DEBIT"}]
    },
    "DC_FRAUD": {
        "text": "Fraud Transaction\n\nIn case of suspected fraud on your Debit Card, lock it instantly via mBoB app or call 1095 for instant permanent block.",
        "buttons": [{"title": "Back Menu", "payload": "CARD_DEBIT"}]
    },
    "DC_TYPES": {
        "text": "Card Types\n\nWe provide standard RuPay, Visa, and Mastercard Debit Cards for domestic and international ATM/POS transactions.",
        "buttons": [{"title": "Back Menu", "payload": "CARD_DEBIT"}]
    },
    "DC_ELIGIBILITY": {
        "text": "Eligibility\n\nAll active Savings and Current Account holders are automatically eligible to apply for a Debit Card.",
        "buttons": [{"title": "Back Menu", "payload": "CARD_DEBIT"}]
    },
    "DC_LIMIT": {
        "text": "Withdrawal Limit\n\nMaximum daily ATM cash withdrawal limit is Nu. 40,000.",
        "buttons": [{"title": "Back Menu", "payload": "CARD_DEBIT"}]
    },
    "DC_NEW_REQUEST": {
        "text": "New Card Request\n\nYou can submit a request for a new Debit Card at your nearest branch or online via the internet banking portal.",
        "buttons": [{"title": "Back Menu", "payload": "CARD_DEBIT"}]
    },
    
    # Debit Card Block
    "DC_BLOCK": {
        "text": "Call 1095 OR\n\nLogin mBoB → Cards → Select Account → Select Card → Manage Card → Card ON/OFF",
        "buttons": [
            {"title": "Create Ticket", "payload": "RESOLVED_NO"},
            {"title": "Back Menu", "payload": "CARD_DEBIT"}
        ]
    },
    
    # Debit Card Activate
    "DC_ACTIVATE": {
        "text": "Login mBoB → Cards → Debit Card → Select Account → Activate → Set 4 digit PIN → Submit.",
        "buttons": [
            {"title": "Back Menu", "payload": "CARD_DEBIT"}
        ]
    },

    # GoBoB FAQs
    "GOBOB_FAQ_WHAT": {
        "text": "What is GoBoB\n\nGoBoB is the official digital mobile wallet of Bank of Bhutan, allowing instant payments, transfer, and agent cash withdrawals.",
        "buttons": [{"title": "Back Menu", "payload": "FLOW_GOBOB"}]
    },
    "GOBOB_BLOCKED": {
        "text": "Login Access Blocked\n\nEnter registered mobile and citizen details to receive MPIN reset OTP and set new wallet credentials.",
        "buttons": [{"title": "Back Menu", "payload": "FLOW_GOBOB"}]
    },
    "GOBOB_REG": {
        "text": "Registration\n\nDownload GoBoB app, click Register, and provide mobile details to instantly activate your digital wallet.",
        "buttons": [{"title": "Back Menu", "payload": "FLOW_GOBOB"}]
    },
    "GOBOB_TOURIST": {
        "text": "Registration for Tourist\n\nTourists can register at branches or agents using passport information and local mobile network connections.",
        "buttons": [{"title": "Back Menu", "payload": "FLOW_GOBOB"}]
    },
    "GOBOB_KYC": {
        "text": "KYC Verification\n\nKYC verification elevates your transaction limit categories, requiring a physical verification visit.",
        "buttons": [{"title": "Back Menu", "payload": "FLOW_GOBOB"}]
    },
    "GOBOB_LOST": {
        "text": "Lost Device Block\n\nCall our 24/7 Toll-Free number 1095 instantly to temporarily lock your digital wallet and secure your funds.",
        "buttons": [{"title": "Back Menu", "payload": "FLOW_GOBOB"}]
    },
    "GOBOB_CHARGES": {
        "text": "Charges\n\nWallet creation is free of cost. Wallet to wallet transfers are free. Cash out at agents incurs a minimal fee.",
        "buttons": [{"title": "Back Menu", "payload": "FLOW_GOBOB"}]
    },
    "GOBOB_QR": {
        "text": "QR Scan\n\nScan any standard BoB Pay QR or Bhutan QR at merchant outlets to authorize instant digital payments.",
        "buttons": [{"title": "Back Menu", "payload": "FLOW_GOBOB"}]
    },
    "GOBOB_DEACTIVATE": {
        "text": "Deactivate GoBoB\n\nVisit nearest branch to deactivate GoBoB and close your digital wallet account permanently.",
        "buttons": [{"title": "Back Menu", "payload": "FLOW_GOBOB"}]
    },
    "GOBOB_REFUND": {
        "text": "Wallet Refund Request\n\nSubmit a request at branch to refund wallet balance to your primary bank account.",
        "buttons": [{"title": "Back Menu", "payload": "FLOW_GOBOB"}]
    },
    "GOBOB_LIMIT": {
        "text": "Customer Limit Category\n\nLimit category determines maximum cash volume permissible per day, which scales based on verification level.",
        "buttons": [{"title": "Back Menu", "payload": "FLOW_GOBOB"}]
    },

    # ATS FAQs
    "ATS_FAQ_WHAT": {
        "text": "What is ATS\n\nAutomated Transfer System configures standing instructions for automated loan or bill clearings.",
        "buttons": [{"title": "Back Menu", "payload": "FLOW_ATS"}]
    },
    "ATS_AVAIL": {
        "text": "Avail ATS\n\nYou can configure ATS standing instruction directly inside internet banking or by visiting a branch.",
        "buttons": [{"title": "Back Menu", "payload": "FLOW_ATS"}]
    },
    "ATS_FAQ_LIMIT": {
        "text": "ATS Limit\n\nATS transactional limit is dictated by your savings or current account balance standing.",
        "buttons": [{"title": "Back Menu", "payload": "FLOW_ATS"}]
    },
    "ATS_CASH": {
        "text": "ATS Cash\n\nStanding instructions can trigger cash accumulation sweeps to designated savings categories automatically.",
        "buttons": [{"title": "Back Menu", "payload": "FLOW_ATS"}]
    },
    "ATS_FAQ_CARD": {
        "text": "ATS Add to Card\n\nLink your credit card bill payments directly to ATS for automated monthly clearing sweeps.",
        "buttons": [{"title": "Back Menu", "payload": "FLOW_ATS"}]
    },
    "ATS_FAQ_MINOR": {
        "text": "ATS for Minor\n\nATS is valid for minor savings accounts when authenticated by natural guardians in writing.",
        "buttons": [{"title": "Back Menu", "payload": "FLOW_ATS"}]
    },
    "ATS_FAQ_EXPIRY": {
        "text": "ATS Expiry\n\nStanding instructions persist until specified cancellation criteria are met or the time period expires.",
        "buttons": [{"title": "Back Menu", "payload": "FLOW_ATS"}]
    }
}
