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
        {"title": "Annual Travel (ATS)", "payload": "FLOW_ATS"},
        {"title": "BOB Account Opening", "payload": "FLOW_LOANS_ACCTS"},
        {"title": "BOB Loan Apply Online", "payload": "FLOW_LOAN_APPLY"},
        {"title": "Create Support Ticket", "payload": "RESOLVED_NO"},
    ]
}

# mBoB Menu
MBOB_MENU = {
    "text": "Please select your mBoB concern.",
    "buttons": [
        {"title": "Registration", "payload": "MBOB_REGISTRATION"},
        {"title": "Login Access Blocked", "payload": "MBOB_LOGIN_BLOCKED"},
        {"title": "Interbank Transfer Fail", "payload": "MBOB_TX_FAILED"},
        {"title": "Device Change", "payload": "MBOB_DEVICE_CHANGE"},
        {"title": "Fund Transfer Limit", "payload": "MBOB_LIMIT"},
        {"title": "Check/Change Category", "payload": "MBOB_CATEGORY"}
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
        {"title": "Unauthorized/Fraud Txn", "payload": "CC_FRAUD"},
        {"title": "Eligibility", "payload": "CC_ELIGIBILITY"},
        {"title": "Types of Credit Card", "payload": "CC_TYPES"},
        {"title": "Issuance & Annual Fee", "payload": "CC_FEES"},
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
        # {"title": "Login Access Blocked", "payload": "GOBOB_BLOCKED"},
        {"title": "Registration Options", "payload": "GOBOB_REG_MENU"},
        {"title": "Lost Device Block", "payload": "GOBOB_LOST"},
        {"title": "Charges", "payload": "GOBOB_CHARGES"},
        {"title": "QR Scan", "payload": "GOBOB_QR"},
        {"title": "Deactivate GoBoB", "payload": "GOBOB_DEACTIVATE"},
        {"title": "Wallet Refund Request", "payload": "GOBOB_REFUND"},
        {"title": "Customer Limit Category", "payload": "GOBOB_LIMIT"},
        {"title": "Back Menu", "payload": "MAIN_MENU"}
    ]
}

# GoBoB Registration Sub-Menu
GOBOB_REG_MENU = {
    "text": "Please select your GoBoB Registration concern.",
    "buttons": [
        {"title": "General Registration", "payload": "GOBOB_REG"},
        {"title": "How to register", "payload": "GOBOB_HOW_TO_REG"},
        {"title": "Registration for Tourist", "payload": "GOBOB_TOURIST"},
        {"title": "Tourist KYC Verification", "payload": "GOBOB_TOURIST_KYC"},
        {"title": "Back to GoBoB Menu", "payload": "FLOW_GOBOB"}
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
        "text": """**Registration**

An account with Bank of Bhutan and a registered Mobile/Email address is required to avail this service.

* **Thumb Print Accounts**: Please visit the nearest BoB branch for registration.
* **Signature Accounts**: Please register from the mBoB app by following the below steps:

1. Tap **"Sign-Up"** option on the main mBoB app screen.
2. Enter your **BoB Account Number** and your **CID/License/Work Permit/Passport number** registered with the bank and tap **"Submit"**.
   *Note: You will need to agree to the mBoB Terms and Conditions to use the app.*
3. An **OTP** will be sent to the registered email ID and mobile number for confirmation.
4. Enter the **OTP** received and proceed.
5. Your **mBoB User ID** and **MPIN (Login PIN)** will be sent to you.""",
        "buttons": [
            {"title": "Back to mBoB Menu", "payload": "FLOW_MBOB"},
            {"title": "Create Ticket", "payload": "RESOLVED_NO"}
        ]
    },
    
    # mBoB Login Access Blocked
    "MBOB_LOGIN_BLOCKED": {
        "text": """**Login Access Blocked**

To reset MPIN or unblock login access to mBoB:

1. **Open mBoB App**
2. Tap **"Forgot"** option on the login page
3. Enter your **User ID, Registered Mobile number and CID Number** and Submit. (An OTP will be sent to your registered email address and mobile number)
4. Enter the **OTP** received via SMS or email to reset your MPIN
5. A **new MPIN** will be sent to your registered email address and mobile number
6. Enter the **New MPIN** received on the main login page
7. Once done, it will take you to the **"Reset M-PIN"** page where you will have to enter the MPIN received on the **"Enter Default M-PIN"** field.
8. On the **"New M-PIN"** field, enter the PIN of your choice and repeat the same on **"Confirm New M-PIN"**
9. Your M-PIN will be successfully reset.""",
        "buttons": [
            {"title": "Still Facing Issue", "payload": "RESOLVED_NO"},
            {"title": "Back Menu", "payload": "FLOW_MBOB"}
        ]
    },
    
    # mBoB Fund Transfer Failed to Other Banks
    "MBOB_TX_FAILED": {
        "text": "As per the RMA and force credit policy, all interbank failed transactions will be credited to the beneficiary’s account on the next working day if the beneficiary account is valid and active. Hence please allow us time for the payment to process.",
        "buttons": [
            {"title": "Create Ticket", "payload": "RESOLVED_NO"},
            {"title": "Back Menu", "payload": "FLOW_MBOB"}
        ]
    },
    
    # mBoB Device Change
    "MBOB_DEVICE_CHANGE": {
        "text": "An individual mBoB user can only access mBoB from one device at a time. If you have changed your device and wish to access mBoB on a new device, please call us at our Toll-Free Number 1095 (Within Bhutan) or visit the nearest BoB branch. For customers residing abroad, please call us at 📞 +975-2-349903 or email the duly filled mBoB Change Request form to 📧 mbob@bob.bt",
        "buttons": [
            {"title": "Create Ticket", "payload": "RESOLVED_NO"},
            {"title": "Back Menu", "payload": "FLOW_MBOB"}
        ]
    },
    
    # mBoB Fund Transfer Limit
    "MBOB_LIMIT": {
        "text": """**Fund Transfer Limit**

Following are the limit details for fund transfers:

1. **Within BoB Accounts (Accounts with Signature)**: Unlimited. However, it depends on your mBoB Category:
   - **Gold Category**: Unlimited
   - **Silver Category**: Nu. 500,000 (Daily Limit)
   - **General Category**: Nu. 100,000 (Daily Limit)

2. **Within BoB Accounts (Thumbprint Account)**:
   - **Daily Limit**: Nu. 5,000
   - **Transaction Limit**: Nu. 3,000

3. **BoB to Other Banks**:
   - **Daily Limit**: Nu. 1 Million per day (as per RMA guidelines)""",
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
        "text": "To prevent unauthorized or fraudulent activity, cardholders may immediately block their card via mBoB or request a card replacement.",
        "buttons": [{"title": "Back Menu", "payload": "CARD_CREDIT"}]
    },
    "CC_ELIGIBILITY": {
        "text": "Any Bhutanese between the age of 18 to 70 years with a legitimate repayment source. Salaried employees with minimum net take home pay of Nu.10,040/-.",
        "buttons": [{"title": "Back Menu", "payload": "CARD_CREDIT"}]
    },
    "CC_TYPES": {
        "text": """**Types of Credit Cards**

* **Visa Domestic Credit card**: Valid in Bhutan, India & Nepal.
* **Visa International Credit card**: Valid outside Bhutan, India & Nepal.
* **Corporate Credit card**: Valid in all countries.""",
        "buttons": [{"title": "Back Menu", "payload": "CARD_CREDIT"}]
    },
    "CC_FEES": {
        "text": "The issuance Fee of a credit card is Nu.525 Per Card. The credit card will also be charged with Nu.1048.95 annually as annual Fee.",
        "buttons": [{"title": "Back Menu", "payload": "CARD_CREDIT"}]
    },
    "CC_REPLACEMENT_FEE": {
        "text": "The Fee for Credit card Replacement/Renewal is Nu.315 Per Card. You can apply this using mBoB.",
        "buttons": [{"title": "Back Menu", "payload": "CARD_CREDIT"}]
    },
    "CC_LIMIT": {
        "text": "The Maximum Card limit is up to Nu.150,000/-. You can increase your card limit against a collateral such as fixed assets, lien against deposit in CASA account, Fixed Deposit or Recurring Deposit account.",
        "buttons": [{"title": "Back Menu", "payload": "CARD_CREDIT"}]
    },
    "CC_BILL": {
        "text": """There are two payment options:
1. **FAD (Full Amount Due)**: Total Due amount.
2. **MAD (Minimum Amount Due)**: 10% of the FAD.

The cardholder can either opt to pay FAD or MAD. The cardholder can make the re-payment through mBoB or Choose for Auto debit (SI) from Savings account.""",
        "buttons": [{"title": "Back Menu", "payload": "CARD_CREDIT"}]
    },
    
    # Credit Card Block
    "CC_BLOCK": {
        "text": """To block your credit card, call **1095** or send email to **creditcard@bob.bt**.

However, transaction controls can be turned OFF/ON via mBoB:
Login to mBoB app > select cards > select card > manage card > card controls > turn off the toggle switch for ATM/Online/POS. Your credit card will be temporarily blocked for further transactions.""",
        "buttons": [
            {"title": "Create Ticket", "payload": "RESOLVED_NO"},
            {"title": "Back Menu", "payload": "CARD_CREDIT"}
        ]
    },
    
    # Credit Card Activate
    "CC_ACTIVATE": {
        "text": """You can activate your new/ replaced issued credit cards using the mBoB app.

To activate the card, login to mBoB > select cards > credit card > activate > set card pin > enter four-digit pin of your choice > submit.""",
        "buttons": [
            {"title": "Back Menu", "payload": "CARD_CREDIT"}
        ]
    },

    # DEBIT CARD SPECS
    "DC_ISSUANCE_FEE": {
        "text": "The issuance Fee of debit card is Nu.315 Per Card.",
        "buttons": [{"title": "Back Menu", "payload": "CARD_DEBIT"}]
    },
    "DC_REPLACEMENT_FEE": {
        "text": "The Fee for debit card Replacement/Renewal is Nu.315 Per Card. You can apply this using mBoB.",
        "buttons": [{"title": "Back Menu", "payload": "CARD_DEBIT"}]
    },
    "DC_FRAUD": {
        "text": "To prevent unauthorized or fraudulent activity, cardholders may immediately block their card via mBoB or request a card replacement.",
        "buttons": [{"title": "Back Menu", "payload": "CARD_DEBIT"}]
    },
    "DC_TYPES": {
        "text": """**Types of Debit Cards**

* **Proprietary Debit card**: Valid within Bhutan only.
* **Visa Domestic debit card**: Valid in Bhutan, India & Nepal.
* **Visa International debit card (Public)**: Valid outside Bhutan, India & Nepal.
* **Visa International debit card (Student)**: Valid outside Bhutan, India & Nepal. The student card is issued to suffice your living expenses abroad. Therefore, upon issuance of the card, bank will not remit or bank transfer your monthly living allowance and vice versa. Card validity is based on applicant student’s study period up to 4 years.

**Documentation required for Visa International Debit Card (Student)**:
* Valid passport copy
* Duly filled application or renewal forms
* University admission/enrollment letter
* Valid visa/permits""",
        "buttons": [{"title": "Back Menu", "payload": "CARD_DEBIT"}]
    },
    "DC_ELIGIBILITY": {
        "text": """**Eligibility criteria for Debit Cards**:

* **Domestic Debit Card**: All savings bank account holders with BoB and account with Individual, Either or Survivor (E or S) are eligible. Thumb impression/Joint account holders & Non-Bhutanese Nationals are **NOT ELIGIBLE**.
* **International Debit Card**: All savings bank account holders with BoB and account with Either or Survivor (E or S) are eligible. Thumb impression/Joint account holders are **NOT ELIGIBLE**.""",
        "buttons": [{"title": "Back Menu", "payload": "CARD_DEBIT"}]
    },
    "DC_LIMIT": {
        "text": """**Withdrawal & POS Limits**:

**Domestic Debit Card**:
Cardholders may utilize funds up to their available account balance, subject to the transaction limits below.
* **Cash Withdrawal**: Nu. 15,000 per transaction. Up to Nu.40,000 per day in BoB ATMs & Nu.30,000 per day in BFS ATMs. INR 10,000 Per day and up to INR 15,000 per month in India/Nepal.
* **POS**: Nu. 500,000 Per transaction in BoB - POS Terminals with unlimited daily/monthly limit. INR 50,000 per month in POS - Visa Network Terminals in India/Nepal.

**International Debit Card**:
Cardholders may utilize funds up to their available account balance, subject to a maximum annual expenditure limit:
* **Visa International debit card (Public)**: USD 1,000 + ATS (If ATS is added) in a year.
* **Visa International debit card (Student)**: USD 1,200/- (Approx. AUD 1,730/- Per month) & USD 10,000 + ATS (if ATS is added) in a year.""",
        "buttons": [{"title": "Back Menu", "payload": "CARD_DEBIT"}]
    },
    "DC_NEW_REQUEST": {
        "text": "To avail a new card, you are required to visit our nearest Bank of Bhutan branch office.",
        "buttons": [{"title": "Back Menu", "payload": "CARD_DEBIT"}]
    },
    
    # Debit Card Block
    "DC_BLOCK": {
        "text": "To block your debit card, call **1095** or Login to mBoB app > select cards > select account > select card > manage card > card ON/OFF.",
        "buttons": [
            {"title": "Create Ticket", "payload": "RESOLVED_NO"},
            {"title": "Back Menu", "payload": "CARD_DEBIT"}
        ]
    },
    
    # Debit Card Activate
    "DC_ACTIVATE": {
        "text": """You can activate your new/ replaced issued debit cards using the mBoB app.

To activate the card, login to mBoB > select cards > debit card > Select Account and activate > set card pin > enter four-digit pin of your choice > submit.""",
        "buttons": [
            {"title": "Back Menu", "payload": "CARD_DEBIT"}
        ]
    },

    # GoBoB FAQs
    "GOBOB_FAQ_WHAT": {
        "text": """**What is GoBoB**

GoBoB is a digital wallet service offered by the Bank of Bhutan. It enables users to securely store funds and perform various financial transactions without the need to open a savings or current account.""",
        "buttons": [{"title": "Back Menu", "payload": "FLOW_GOBOB"}]
    },
    "GOBOB_BLOCKED": {
        "text": """**Login Access Blocked - GoBoB**

To reset MPIN or unblock login access to goBoB > Open goBoB App > Tap “Forgot M-PIN” option on the login page and login with OTP. If you receive an error message such as “Entered details are not valid”, please prepare a copy of your CID or family tree (in case of a minor) and visit the nearest BoBL branch.""",
        "buttons": [{"title": "Back Menu", "payload": "FLOW_GOBOB"}]
    },
    "GOBOB_REG": {
        "text": """**Registration - goBoB**

Anyone can register and use goBoB wallet including minors with a mobile number, email address & CID/Passport/Work permit. However, minors between the age of 10 and under 18 can use goBoB with minimal transaction rights only.""",
        "buttons": [{"title": "Back Menu", "payload": "GOBOB_REG_MENU"}]
    },
    "GOBOB_HOW_TO_REG": {
        "text": """**How to Register**

You can download the goBoB application and can register instantly. However, you can also visit nearest BoB branch offices to register for the service.""",
        "buttons": [{"title": "Back Menu", "payload": "GOBOB_REG_MENU"}]
    },
    "GOBOB_TOURIST": {
        "text": """**Registration for Tourist**

Tourists can conveniently register for the goBoB wallet even before arriving in Bhutan. They can also load funds into the wallet using their cards, ensuring a safe and hassle-free travel experience. This allows tourists to connect and resolve any issue with banks prior to the travel to Bhutan. Providing the correct information during the registration will be critical to ensuring seamless experience.""",
        "buttons": [{"title": "Back Menu", "payload": "GOBOB_REG_MENU"}]
    },
    "GOBOB_TOURIST_KYC": {
        "text": """**KYC verification for Tourist Customers**

The tourist customer can load money into the wallet but will not be able to initiate any transactions from the wallet unless KYC is verified. The Tourist KYC is verified with the Department of Immigration (DOI). Verification needs to be initiated by the customer through ‘Verify KYC’ option available under App’s settings. KYC verification with DOI is instant. However, the customer must ensure that their personal information is correctly provided during the registration. Upon successful KYC verification, the customer can initiate transactions in a seamless manner.""",
        "buttons": [{"title": "Back Menu", "payload": "GOBOB_REG_MENU"}]
    },
    "GOBOB_KYC": {
        "text": "KYC Verification\n\nKYC verification elevates your transaction limit categories, requiring a physical verification visit.",
        "buttons": [{"title": "Back Menu", "payload": "FLOW_GOBOB"}]
    },
    "GOBOB_LOST": {
        "text": """**Block goBoB if lost Device**

You may call us at your toll free 1095 (Within Bhutan) or +975-2-349903 (Calling from Abroad) to temporarily block the transaction access for goBoB incase of device/phone lost.""",
        "buttons": [{"title": "Back Menu", "payload": "FLOW_GOBOB"}]
    },
    "GOBOB_CHARGES": {
        "text": """**Charges**

Registration is free. There are no charges for other services except for adding money from cards and transfer to bank accounts. A convenience fee of 3.68% will be charged while loading your wallet using cards and 2.1% will be charged while sending money to the bank accounts.""",
        "buttons": [{"title": "Back Menu", "payload": "FLOW_GOBOB"}]
    },
    "GOBOB_QR": {
        "text": """**QR Scan**

The QR Scan to Pay payment from goBoB is free and there are no charges for it.""",
        "buttons": [{"title": "Back Menu", "payload": "FLOW_GOBOB"}]
    },
    "GOBOB_DEACTIVATE": {
        "text": """**Deactivate goBoB**

goBoB wallet deactivation is not available through the App. Customers are required to fill out goBoB wallet deactivation form available at our website and submit to the nearest branch. In the event that the customer needs to reuse the wallet, customer will be required to re-register for the goBoB wallet.""",
        "buttons": [{"title": "Back Menu", "payload": "FLOW_GOBOB"}]
    },
    "GOBOB_REFUND": {
        "text": """**Wallet balance refund request**

The refund will be accepted & processed only if the amount was previously loaded using your card.""",
        "buttons": [{"title": "Back Menu", "payload": "FLOW_GOBOB"}]
    },
    "GOBOB_LIMIT": {
        "text": """**Different type of Customer Limit category**

* **Minimal KYC (KYC not verified) & Minor (10 years to less than 18 years)**:
  - **Daily Transaction Limit**: Nu. 2,000
  - **Daily Balance Limit**: Nu. 5,000
  - **Aggregated Monthly Limit**: Nu. 10,000

* **Full KYC (KYC verified)**:
  - **Daily Transaction Limit**: Nu. 30,000
  - **Daily Balance Limit**: Nu. 50,000
  - **Aggregated Monthly Limit**: Nu. 100,000

* **Tourist and Non-tourist (KYC verified with Dept. of Immigration)**:
  - **Daily Transaction Limit**: Nu. 10 million
  - **Daily Balance Limit**: Nu. 20 million
  - **Aggregated Monthly Limit**: Nu. 50 million""",
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
