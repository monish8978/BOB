# BOB Bank Chatbot Static Menus and FAQ Responses (Spec-Aligned Copy)

# Main Menu Options
MAIN_MENU = {
    "text": "Please choose an option below to continue.",
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
        {"title": "Fund transfer failed to other banks", "payload": "MBOB_TX_FAILED"},
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
        {"title": "Main Menu", "payload": "MAIN_MENU"}
    ]
}

# Credit Card Menu
CREDIT_CARD_MENU = {
    "text": "Please select your credit card concern.",
    "buttons": [
        {"title": "Unauthorized/Fraud Txn", "payload": "CC_FRAUD"},
        {"title": "Eligibility", "payload": "CC_ELIGIBILITY"},
        {"title": "Types of Credit Card", "payload": "CC_TYPES"},
        {"title": "Issuance Fee", "payload": "CC_ISSUANCE_FEE"},
        {"title": "Annual Fee", "payload": "CC_ANNUAL_FEE"},
        {"title": "Replacement/Renewal Fee", "payload": "CC_REPLACEMENT_FEE"},
        {"title": "Credit Card Limit", "payload": "CC_LIMIT"},
        {"title": "Credit Card Bill", "payload": "CC_BILL"},
        {"title": "Block Credit Card", "payload": "CC_BLOCK"},
        {"title": "Activate Credit Card", "payload": "CC_ACTIVATE"},
        {"title": "Back To Menu", "payload": "FLOW_CARDS"}, {"title": "Main Menu", "payload": "MAIN_MENU"}
    ]
}

# Debit Card Menu
DEBIT_CARD_MENU = {
    "text": "Please select your debit card concern.",
    "buttons": [
        {"title": "Card Issuance Fee", "payload": "DC_ISSUANCE_FEE"},
        {"title": "Replacement/Renewal Fee", "payload": "DC_REPLACEMENT_FEE"},
        {"title": "Unauthorized/Fraud Txns", "payload": "DC_FRAUD"},
        {"title": "Types of Debit Card", "payload": "DC_TYPES"},
        {"title": "Visa Intl (Student)", "payload": "DC_STUDENT"},
        {"title": "Documentation - Student", "payload": "DC_DOCS_STUDENT"},
        {"title": "Eligibility - Domestic", "payload": "DC_ELIGIBILITY_DOM"},
        {"title": "Withdrawal Limit - Domestic", "payload": "DC_LIMIT_DOM"},
        {"title": "Eligibility - Intl", "payload": "DC_ELIGIBILITY_INTL"},
        {"title": "Withdrawal Limit - Intl", "payload": "DC_LIMIT_INTL"},
        {"title": "Card Application Request", "payload": "DC_NEW_REQUEST"},
        {"title": "Block Debit Card", "payload": "DC_BLOCK"},
        {"title": "Activate Debit Card", "payload": "DC_ACTIVATE"},
        {"title": "Back To Menu", "payload": "FLOW_CARDS"}, {"title": "Main Menu", "payload": "MAIN_MENU"}
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
        {"title": "Main Menu", "payload": "MAIN_MENU"}
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
        {"title": "Back To Menu", "payload": "FLOW_GOBOB"}, {"title": "Main Menu", "payload": "MAIN_MENU"}
    ]
}

# ATS Menu
ATS_MENU = {
    "text": "Annual Travel (ATS)\n\nPlease select your ATS concern.",
    "buttons": [
        {"title": "What is ATS", "payload": "ATS_FAQ_WHAT"},
        {"title": "Avail ATS", "payload": "ATS_AVAIL"},
        {"title": "ATS Limit", "payload": "ATS_FAQ_LIMIT"},
        {"title": "ATS Cash", "payload": "ATS_CASH"},
        {"title": "ATS Add to Card", "payload": "ATS_FAQ_CARD"},
        {"title": "ATS for Minor", "payload": "ATS_FAQ_MINOR"},
        {"title": "ATS Expiry", "payload": "ATS_FAQ_EXPIRY"},
        {"title": "Main Menu", "payload": "MAIN_MENU"}
    ]
}

# Static FAQ Content (Aligned to copy specifications)
FAQS = {
    # mBoB Registration Information
    "MBOB_REGISTRATION": {
        "text": """<b>Registration</b>

An account with Bank of Bhutan and a registered Mobile/Email address is required to avail this service.

* <b>Thumb Print Accounts</b>: Please visit the nearest BoB branch for registration.
* <b>Signature Accounts</b>: Please register from the mBoB app by following the below steps:

1. Tap <b>"Sign-Up"</b> option on the main mBoB app screen.
2. Enter your <b>BoB Account Number</b> and your <b>CID/License/Work Permit/Passport number</b> registered with the bank and tap <b>"Submit"</b>.
   *Note: You will need to agree to the mBoB Terms and Conditions to use the app.*
3. An <b>OTP</b> will be sent to the registered email ID and mobile number for confirmation.
4. Enter the <b>OTP</b> received and proceed.
5. Your <b>mBoB User ID</b> and <b>MPIN (Login PIN)</b> will be sent to you.""",
        "buttons": [
            {"title": "Back To Menu", "payload": "FLOW_MBOB"}, {"title": "Main Menu", "payload": "MAIN_MENU"},
            {"title": "Create Ticket", "payload": "RESOLVED_NO"}
        ]
    },
    
    # mBoB Login Access Blocked
    "MBOB_LOGIN_BLOCKED": {
        "text": """<b>Login Access Blocked</b>

To reset MPIN or unblock login access to mBoB:

1. <b>Open mBoB App</b>
2. Tap <b>"Forgot"</b> option on the login page
3. Enter your <b>User ID, Registered Mobile number and CID Number</b> and Submit. (An OTP will be sent to your registered email address and mobile number)
4. Enter the <b>OTP</b> received via SMS or email to reset your MPIN
5. A <b>new MPIN</b> will be sent to your registered email address and mobile number
6. Enter the <b>New MPIN</b> received on the main login page
7. Once done, it will take you to the <b>"Reset M-PIN"</b> page where you will have to enter the MPIN received on the <b>"Enter Default M-PIN"</b> field.
8. On the <b>"New M-PIN"</b> field, enter the PIN of your choice and repeat the same on <b>"Confirm New M-PIN"</b>
9. Your M-PIN will be successfully reset.""",
        "buttons": [
            {"title": "Back To Menu", "payload": "FLOW_MBOB"}, {"title": "Main Menu", "payload": "MAIN_MENU"}
        ]
    },
    
    # mBoB Fund Transfer Failed to Other Banks
    "MBOB_TX_FAILED": {
        "text": """<b>Fund transfer failed to other banks</b>

As per the RMA and force credit policy, all interbank failed transactions will be
credited to the beneficiary’s account on the next working day if the beneficiary
account is valid and active. Hence please allow us time for the payment to
process. 

Please allow us some time for the payment to process.""",
        "buttons": [
            {"title": "Create Ticket", "payload": "RESOLVED_NO"},
            {"title": "Back To Menu", "payload": "FLOW_MBOB"}, {"title": "Main Menu", "payload": "MAIN_MENU"}
        ]
    },
    
    # mBoB Device Change
    "MBOB_DEVICE_CHANGE": {
        "text": """<b>mBoB Device Change</b>

An individual mBoB user can only access mBoB from one device at a time. If
you have changed your device and wish to access mBoB on a new device,
please call us at our Toll-Free Number 1095 (Within Bhutan) or visit the nearest
BoB branch. For customers residing abroad, please call us at +975-2-349903
or email the duly filled mBoB Change Request form to mbob@bob.bt""",
        "buttons": [
            {"title": "Create Ticket", "payload": "RESOLVED_NO"},
            {"title": "Back To Menu", "payload": "FLOW_MBOB"}, {"title": "Main Menu", "payload": "MAIN_MENU"}
        ]
    },
    
    # mBoB Fund Transfer Limit
    "MBOB_LIMIT": {
        "text": """<b>Fund Transfer Limit</b>

Following are the details:

1. <b>Within BoB Accounts (Accounts with Signature)</b>: Unlimited. However, it depends on your mBoB Category:
   - <b>Gold Category</b>: Unlimited
   - <b>Silver Category</b>: Nu. 500,000 (Daily Limit)
   - <b>General Category</b>: Nu. 100,000 (Daily Limit)

2. <b>Within BoB Accounts (Thumbprint Account)</b>:
   - <b>Daily Limit</b>: Nu. 5,000
   - <b>Transaction Limit</b>: Nu. 3,000

3. <b>BoB to Other Banks</b>:
   - <b>Daily Limit</b>: Nu. 1 Million per day (as per RMA guidelines)""",
        "buttons": [
            {"title": "Back To Menu", "payload": "FLOW_MBOB"}, {"title": "Main Menu", "payload": "MAIN_MENU"}
        ]
    },
    
    # mBoB Check/Change Fund Transfer Category
    "MBOB_CATEGORY": {
        "text": """<b>Check/Change Fund Transfer Category</b>

To check your mBoB fund transfer category, follow the steps below:
1. Login to <b>mBoB</b>
2. Tap on the drop-down menu on the top left corner after successful login
3. Tap “Change Category”. Your current category will be displayed at the top
followed by the option to change your new Category.
""",
        "buttons": [
            {"title": "Back To Menu", "payload": "FLOW_MBOB"}, {"title": "Main Menu", "payload": "MAIN_MENU"}
        ]
    },
    # CREDIT CARD SPECS
    "CC_FRAUD": {
        "text": "To prevent unauthorized or fraudulent activity, cardholders may immediately block their card via mBoB or request a card replacement.",
        "buttons": [{"title": "Back To Menu", "payload": "CARD_CREDIT"}, {"title": "Main Menu", "payload": "MAIN_MENU"}]
    },
    "CC_ELIGIBILITY": {
        "text": "Any Bhutanese between the age of 18 to 70 years with a legitimate repayment source. Salaried employees with minimum net take home pay of Nu.10,040/-.",
        "buttons": [{"title": "Back To Menu", "payload": "CARD_CREDIT"}, {"title": "Main Menu", "payload": "MAIN_MENU"}]
    },
    "CC_TYPES": {
        "text": """<b>Types of Credit Cards</b>

* <b>Visa Domestic Credit card</b>: Valid in Bhutan, India & Nepal.
* <b>Visa International Credit card</b>: Valid outside Bhutan, India & Nepal.
* <b>Corporate Credit card</b>: Valid in all countries.""",
        "buttons": [{"title": "Back To Menu", "payload": "CARD_CREDIT"}, {"title": "Main Menu", "payload": "MAIN_MENU"}]
    },
    "CC_ISSUANCE_FEE": {
        "text": "The issuance Fee of credit card is Nu.525 Per Card.",
        "buttons": [{"title": "Back To Menu", "payload": "CARD_CREDIT"}, {"title": "Main Menu", "payload": "MAIN_MENU"}]
    },
    "CC_ANNUAL_FEE": {
        "text": "The credit card will be charged with Nu.1048.95 annually as annual Fee.",
        "buttons": [{"title": "Back To Menu", "payload": "CARD_CREDIT"}, {"title": "Main Menu", "payload": "MAIN_MENU"}]
    },
    "CC_REPLACEMENT_FEE": {
        "text": "The Fee for Credit card Replacement/Renewal is Nu.315 Per Card. You can apply this using mBoB.",
        "buttons": [{"title": "Back To Menu", "payload": "CARD_CREDIT"}, {"title": "Main Menu", "payload": "MAIN_MENU"}]
    },
    "CC_LIMIT": {
        "text": "The Maximum Card limit is up to Nu.150,000/-. You can increase your card limit against a collateral such as fixed assets, lien against deposit in CASA account, Fixed Deposit or Recurring Deposit account.",
        "buttons": [{"title": "Back To Menu", "payload": "CARD_CREDIT"}, {"title": "Main Menu", "payload": "MAIN_MENU"}]
    },
    "CC_BILL": {
        "text": """There are two payment options:
1. <b>FAD (Full Amount Due)</b>: Total Due amount.
2. <b>MAD (Minimum Amount Due)</b>: 10% of the FAD.

The cardholder can either opt to pay FAD or MAD. The cardholder can make the re-payment through mBoB or Choose for Auto debit (SI) from Savings account.""",
        "buttons": [{"title": "Back To Menu", "payload": "CARD_CREDIT"}, {"title": "Main Menu", "payload": "MAIN_MENU"}]
    },
    
    # Credit Card Block
    "CC_BLOCK": {
        "text": """To block your credit card, call <b>1095</b> or send email to <b>creditcard@bob.bt</b>.

However, transaction controls can be turned OFF/ON via mBoB:
Login to mBoB app > select cards > select card > manage card > card controls > turn off the toggle switch for ATM/Online/POS. Your credit card will be temporarily blocked for further transactions.""",
        "buttons": [
            {"title": "Create Ticket", "payload": "RESOLVED_NO"},
            {"title": "Back To Menu", "payload": "CARD_CREDIT"}, {"title": "Main Menu", "payload": "MAIN_MENU"}
        ]
    },
    
    # Credit Card Activate
    "CC_ACTIVATE": {
        "text": """You can activate your new/ replaced issued credit cards using the mBoB app.

To activate the card, login to mBoB > select cards > credit card > activate > set card pin > enter four-digit pin of your choice > submit.""",
        "buttons": [
            {"title": "Back To Menu", "payload": "CARD_CREDIT"}, {"title": "Main Menu", "payload": "MAIN_MENU"}
        ]
    },

    # DEBIT CARD SPECS
    "DC_ISSUANCE_FEE": {
        "text": "The issuance Fee of debit card is Nu.315 Per Card.",
        "buttons": [{"title": "Back To Menu", "payload": "CARD_DEBIT"}, {"title": "Main Menu", "payload": "MAIN_MENU"}]
    },
    "DC_REPLACEMENT_FEE": {
        "text": "The Fee for debit card Replacement/Renewal is Nu.315 Per Card. You can apply this using mBoB.",
        "buttons": [{"title": "Back To Menu", "payload": "CARD_DEBIT"}, {"title": "Main Menu", "payload": "MAIN_MENU"}]
    },
    "DC_FRAUD": {
        "text": "To prevent unauthorized or fraudulent activity, cardholders may immediately block their card via mBoB or request a card replacement.",
        "buttons": [{"title": "Back To Menu", "payload": "CARD_DEBIT"}, {"title": "Main Menu", "payload": "MAIN_MENU"}]
    },
    "DC_TYPES": {
        "text": """<b>Types of Debit Cards</b>

Proprietary Debit card â€“ Valid within Bhutan only.
Visa Domestic debit card â€“ Valid in Bhutan, India & Nepal.
Visa International debit card (Public) â€“ Valid outside Bhutan, India & Nepal.
Visa International debit card (Student) â€“ Valid outside Bhutan, India & Nepal.""",
        "buttons": [{"title": "Back To Menu", "payload": "CARD_DEBIT"}, {"title": "Main Menu", "payload": "MAIN_MENU"}]
    },
    "DC_STUDENT": {
        "text": "The student card is issued to suffice your living expenses abroad. Therefore, upon issuance of the card, bank will not remit or bank transfer your monthly living allowance and vice versa. Card validity is based on applicant studentâ€™s study period up to 4 years.",
        "buttons": [{"title": "Back To Menu", "payload": "CARD_DEBIT"}, {"title": "Main Menu", "payload": "MAIN_MENU"}]
    },
    "DC_DOCS_STUDENT": {
        "text": """<b>Documentation - Visa International debit card (Student)</b>

â— Valid passport copy
â— Duly filled application or renewal forms
â— University admission/enrollment letter
â— Valid visa/permits (for future students)
â— Valid visa/permits (for current students).
â— Student ID""",
        "buttons": [{"title": "Back To Menu", "payload": "CARD_DEBIT"}, {"title": "Main Menu", "payload": "MAIN_MENU"}]
    },
    "DC_ELIGIBILITY_DOM": {
        "text": "All savings bank account holders with BoB and account with Individual, Either or Survivor (E OR S) are eligible. Thumb impression/Joint account holders & Non-Bhutanese Nationals are NOT ELIGIBLE.",
        "buttons": [{"title": "Back To Menu", "payload": "CARD_DEBIT"}, {"title": "Main Menu", "payload": "MAIN_MENU"}]
    },
    "DC_LIMIT_DOM": {
        "text": """<b>Withdrawal Limit on Domestic debit card</b>

Cardholders may utilize funds up to their available account balance, subject to the transaction limit as below.

Cash Withdrawal:
â— Nu. 15,000 per transaction. Up to Nu.40,000 per day in BOB ATMs & Nu.30,000 per day in BFS ATMs.
â— INR 10,000 Per day and up to INR 15,000 per month in India/Nepal.

POS:
â— Nu. 500,000 Per transaction in BOB - POS Terminals with unlimited daily/monthly limit.
â— INR 50,000 per month in POS - Visa Network Terminals in India/Nepal.""",
        "buttons": [{"title": "Back To Menu", "payload": "CARD_DEBIT"}, {"title": "Main Menu", "payload": "MAIN_MENU"}]
    },
    "DC_ELIGIBILITY_INTL": {
        "text": "All savings bank account holders with BoB and account with Either or Survivor (E OR S) are eligible. Thumb impression/Joint account holders are NOT ELIGIBLE.",
        "buttons": [{"title": "Back To Menu", "payload": "CARD_DEBIT"}, {"title": "Main Menu", "payload": "MAIN_MENU"}]
    },
    "DC_LIMIT_INTL": {
        "text": """<b>Withdrawal Limit on International debit card</b>

Cardholders may utilize funds up to their available account balance, subject to a maximum annual expenditure limit.

Visa International debit card (Public): USD 1,000 + ATS (If ATS is added) in a year.
Visa International debit card (Student): USD 1,200/- (Approx. AUD 1,730/- Per month). & USD 10,000 + ATS (if ATS is added) in a year.""",
        "buttons": [{"title": "Back To Menu", "payload": "CARD_DEBIT"}, {"title": "Main Menu", "payload": "MAIN_MENU"}]
    },
    "DC_NEW_REQUEST": {
        "text": "To avail a new card, you are required to visit our nearest Bank of Bhutan branch office.",
        "buttons": [{"title": "Back To Menu", "payload": "CARD_DEBIT"}, {"title": "Main Menu", "payload": "MAIN_MENU"}]
    },
    
    # Debit Card Block
    "DC_BLOCK": {
        "text": "To block your debit card, call <b>1095</b> or Login to mbob app > select cards > select account > select card > manage card > card ON/OFF.",
        "buttons": [
            {"title": "Create Ticket", "payload": "RESOLVED_NO"},
            {"title": "Back To Menu", "payload": "CARD_DEBIT"}, {"title": "Main Menu", "payload": "MAIN_MENU"}
        ]
    },
    
    # Debit Card Activate
    "DC_ACTIVATE": {
        "text": """You can activate your new/ replaced issued debit cards using the mbob app.

To activate the card, login to mbob > select cards > debit card > Select Account and activate > set card pin > enter four-digit pin of your choice > submit.""",
        "buttons": [
            {"title": "Back To Menu", "payload": "CARD_DEBIT"}, {"title": "Main Menu", "payload": "MAIN_MENU"}
        ]
    },

    # GoBoB FAQs
    "GOBOB_FAQ_WHAT": {
        "text": """<b>What is GoBoB</b>

GoBoB is a digital wallet service offered by the Bank of Bhutan. It enables users to securely store funds and perform various financial transactions without the need to open a savings or current account.""",
        "buttons": [{"title": "Back To Menu", "payload": "FLOW_GOBOB"}, {"title": "Main Menu", "payload": "MAIN_MENU"}]
    },
    "GOBOB_BLOCKED": {
        "text": """<b>Login Access Blocked - GoBoB</b>

To reset MPIN or unblock login access to goBoB:
1. Open <b>goBoB App</b>
2. Tap <b>â€œForgot M-PINâ€</b> option on the login page and login with OTP. 

<i>Note: If you receive an error message such as â€œEntered details are not validâ€, please prepare a copy of your CID or family tree (in case of a minor) and visit the nearest BoBL branch.</i>""",
        "buttons": [{"title": "Back To Menu", "payload": "FLOW_GOBOB"}, {"title": "Main Menu", "payload": "MAIN_MENU"}]
    },
    "GOBOB_REG": {
        "text": """<b>Registration - goBoB</b>

Anyone can register and use goBoB wallet including minors with a mobile number, email address & CID/Passport/Work permit. However, minors between the age of 10 and under 18 can use goBoB with minimal transaction rights only.""",
        "buttons": [{"title": "Back To Menu", "payload": "GOBOB_REG_MENU"}, {"title": "Main Menu", "payload": "MAIN_MENU"}]
    },
    "GOBOB_HOW_TO_REG": {
        "text": """<b>How to Register</b>

You can download the goBoB application and can register instantly. However, you can also visit nearest BoB branch offices to register for the service.""",
        "buttons": [{"title": "Back To Menu", "payload": "GOBOB_REG_MENU"}, {"title": "Main Menu", "payload": "MAIN_MENU"}]
    },
    "GOBOB_TOURIST": {
        "text": """<b>Registration for Tourist</b>

Tourists can conveniently register for the goBoB wallet even before arriving in Bhutan. They can also load funds into the wallet using their cards, ensuring a safe and hassle-free travel experience. This allows tourists to connect and resolve any issue with banks prior to the travel to Bhutan. Providing the correct information during the registration will be critical to ensuring seamless experience.""",
        "buttons": [{"title": "Back To Menu", "payload": "GOBOB_REG_MENU"}, {"title": "Main Menu", "payload": "MAIN_MENU"}]
    },
    "GOBOB_TOURIST_KYC": {
        "text": """<b>KYC verification for Tourist Customers</b>

The tourist customer can load money into the wallet but will not be able to initiate any transactions from the wallet unless KYC is verified. The Tourist KYC is verified with the Department of Immigration (DOI). Verification needs to be initiated by the customer through â€˜Verify KYCâ€™ option available under Appâ€™s settings. KYC verification with DOI is instant. However, the customer must ensure that their personal information is correctly provided during the registration. Upon successful KYC verification, the customer can initiate transactions in a seamless manner.""",
        "buttons": [{"title": "Back To Menu", "payload": "GOBOB_REG_MENU"}, {"title": "Main Menu", "payload": "MAIN_MENU"}]
    },
    "GOBOB_KYC": {
        "text": """<b>KYC Verification</b>

KYC verification elevates your transaction limit categories, requiring a physical verification visit to your nearest branch.""",
        "buttons": [{"title": "Back To Menu", "payload": "FLOW_GOBOB"}, {"title": "Main Menu", "payload": "MAIN_MENU"}]
    },
    "GOBOB_LOST": {
        "text": """<b>Block goBoB if lost Device</b>

You may call us at your toll free 1095 (Within Bhutan) or +975-2-349903 (Calling from Abroad) to temporarily block the transaction access for goBoB incase of device/phone lost.""",
        "buttons": [{"title": "Back To Menu", "payload": "FLOW_GOBOB"}, {"title": "Main Menu", "payload": "MAIN_MENU"}]
    },
    "GOBOB_CHARGES": {
        "text": """<b>Charges</b>

Registration is free. There are no charges for other services except for adding money from cards and transfer to bank accounts. A convenience fee of 3.68% will be charged while loading your wallet using cards and 2.1% will be charged while sending money to the bank accounts.""",
        "buttons": [{"title": "Back To Menu", "payload": "FLOW_GOBOB"}, {"title": "Main Menu", "payload": "MAIN_MENU"}]
    },
    "GOBOB_QR": {
        "text": """<b>QR Scan</b>

The QR Scan to Pay payment from goBoB is free and there are no charges for it.""",
        "buttons": [{"title": "Back To Menu", "payload": "FLOW_GOBOB"}, {"title": "Main Menu", "payload": "MAIN_MENU"}]
    },
    "GOBOB_DEACTIVATE": {
        "text": """<b>Deactivate goBoB</b>

goBoB wallet deactivation is not available through the App. Customers are required to fill out goBoB wallet deactivation form available at our website and submit to the nearest branch. In the event that the customer needs to reuse the wallet, customer will be required to re-register for the goBoB wallet.""",
        "buttons": [{"title": "Back To Menu", "payload": "FLOW_GOBOB"}, {"title": "Main Menu", "payload": "MAIN_MENU"}]
    },
    "GOBOB_REFUND": {
        "text": """<b>Wallet balance refund request</b>

The refund will be accepted & processed only if the amount was previously loaded using your card.""",
        "buttons": [{"title": "Back To Menu", "payload": "FLOW_GOBOB"}, {"title": "Main Menu", "payload": "MAIN_MENU"}]
    },
    "GOBOB_LIMIT": {
        "text": """<b>Different type of Customer Limit category</b>

* <b>Minimal KYC (KYC not verified) & Minor (10 years to less than 18 years)</b>:
  - <b>Daily Transaction Limit</b>: Nu. 2,000
  - <b>Daily Balance Limit</b>: Nu. 5,000
  - <b>Aggregated Monthly Limit</b>: Nu. 10,000

* <b>Full KYC (KYC verified)</b>:
  - <b>Daily Transaction Limit</b>: Nu. 30,000
  - <b>Daily Balance Limit</b>: Nu. 50,000
  - <b>Aggregated Monthly Limit</b>: Nu. 100,000

* <b>Tourist and Non-tourist (KYC verified with Dept. of Immigration)</b>:
  - <b>Daily Transaction Limit</b>: Nu. 10 million
  - <b>Daily Balance Limit</b>: Nu. 20 million
  - <b>Aggregated Monthly Limit</b>: Nu. 50 million""",
        "buttons": [{"title": "Back To Menu", "payload": "FLOW_GOBOB"}, {"title": "Main Menu", "payload": "MAIN_MENU"}]
    },

    # ATS FAQs
    "ATS_FAQ_WHAT": {
        "text": """<b>What is ATS?</b>

Automated Transfer System configures standing instructions for automated loan or bill clearings.""",
        "buttons": [{"title": "Back To Menu", "payload": "FLOW_ATS"}, {"title": "Main Menu", "payload": "MAIN_MENU"}]
    },
    "ATS_AVAIL": {
        "text": """<b>Avail ATS</b>

You can configure ATS standing instruction directly inside internet banking or by visiting a branch.""",
        "buttons": [{"title": "Back To Menu", "payload": "FLOW_ATS"}, {"title": "Main Menu", "payload": "MAIN_MENU"}]
    },
    "ATS_FAQ_LIMIT": {
        "text": """<b>ATS Limit</b>

ATS transactional limit is dictated by your savings or current account balance standing.""",
        "buttons": [{"title": "Back To Menu", "payload": "FLOW_ATS"}, {"title": "Main Menu", "payload": "MAIN_MENU"}]
    },
    "ATS_CASH": {
        "text": """<b>ATS Cash</b>

Standing instructions can trigger cash accumulation sweeps to designated savings categories automatically.""",
        "buttons": [{"title": "Back To Menu", "payload": "FLOW_ATS"}, {"title": "Main Menu", "payload": "MAIN_MENU"}]
    },
    "ATS_FAQ_CARD": {
        "text": """<b>ATS Add to Card</b>

Link your credit card bill payments directly to ATS for automated monthly clearing sweeps.""",
        "buttons": [{"title": "Back To Menu", "payload": "FLOW_ATS"}, {"title": "Main Menu", "payload": "MAIN_MENU"}]
    },
    "ATS_FAQ_MINOR": {
        "text": """<b>ATS for Minor</b>

ATS is valid for minor savings accounts when authenticated by natural guardians in writing.""",
        "buttons": [{"title": "Back To Menu", "payload": "FLOW_ATS"}, {"title": "Main Menu", "payload": "MAIN_MENU"}]
    },
    "ATS_FAQ_EXPIRY": {
        "text": """<b>ATS Expiry</b>

Standing instructions persist until specified cancellation criteria are met or the time period expires.""",
        "buttons": [{"title": "Back To Menu", "payload": "FLOW_ATS"}, {"title": "Main Menu", "payload": "MAIN_MENU"}]
    }
}
