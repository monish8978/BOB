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
        {"title": "Create Support Ticket", "payload": "CREATE_SUPPORT_TICKET"},
    ]
}

# mBoB Menu
MBOB_MENU = {
    "text": "Please select your mBoB concern.",
    "buttons": [
        {"title": "Registration", "payload": "MBOB_REGISTRATION"},
        {"title": "Login Access Blocked", "payload": "MBOB_LOGIN_BLOCKED"},
        {"title": "Other bank txn failed", "payload": "MBOB_TX_FAILED"},
        {"title": "Device Change", "payload": "MBOB_DEVICE_CHANGE"},
        {"title": "Fund Transfer Limit", "payload": "MBOB_LIMIT"},
        {"title": "Check/Change Category", "payload": "MBOB_CATEGORY"},
        {"title": "Main Menu", "payload": "MAIN_MENU"}
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
        {"title": "Login Access Blocked", "payload": "GOBOB_BLOCKED"},
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
        {"title": "ATS to Third person", "payload": "ATS_FAQ_THIRD_PERSON"},
        {"title": "ATS Expiry", "payload": "ATS_FAQ_EXPIRY"},
        {"title": "Main Menu", "payload": "MAIN_MENU"}
    ]
}

# Static FAQ Content (Aligned to copy specifications)
FAQS = {
    "MBOB_REGISTRATION": {
        'text': '<b>Registration</b>\n\nAn account with Bank of Bhutan and a registered Mobile/Email address is required to avail this service.\n\n* <b>Thumb Print Accounts</b>: Please visit the nearest BoB branch for registration.\n* <b>Signature Accounts</b>: Please register from the mBoB app by following the below steps:\n\n1. Tap <b>"Sign-Up"</b> option on the main mBoB app screen.\n2. Enter your <b>BoB Account Number</b> and your <b>CID/License/Work Permit/Passport number</b> registered with the bank and tap <b>"Submit"</b>.\n   *Note: You will need to agree to the mBoB Terms and Conditions to use the app.*\n3. An <b>OTP</b> will be sent to the registered email ID and mobile number for confirmation.\n4. Enter the <b>OTP</b> received and proceed.\n5. Your <b>mBoB User ID</b> and <b>MPIN (Login PIN)</b> will be sent to you.\n\nPlease let us know if you are satisfied with the resolution.',
        'buttons': [
            {'title': 'Yes', 'payload': 'RESOLVED_YES'},
            {'title': 'No', 'payload': 'RESOLVED_NO'},
        ]
    },
    "MBOB_LOGIN_BLOCKED": {
        'text': '<b>Login Access Blocked</b>\n\nTo reset MPIN or unblock login access to mBoB:\n\n1. <b>Open mBoB App</b>\n2. Tap <b>"Forgot"</b> option on the login page\n3. Enter your <b>User ID, Registered Mobile number and CID Number</b> and Submit. (An OTP will be sent to your registered email address and mobile number)\n4. Enter the <b>OTP</b> received via SMS or email to reset your MPIN\n5. A <b>new MPIN</b> will be sent to your registered email address and mobile number\n6. Enter the <b>New MPIN</b> received on the main login page\n7. Once done, it will take you to the <b>"Reset M-PIN"</b> page where you will have to enter the MPIN received on the <b>"Enter Default M-PIN"</b> field.\n8. On the <b>"New M-PIN"</b> field, enter the PIN of your choice and repeat the same on <b>"Confirm New M-PIN"</b>\n9. Your M-PIN will be successfully reset.\n\nPlease let us know if you are satisfied with the resolution.',
        'buttons': [
            {'title': 'Yes', 'payload': 'RESOLVED_YES'},
            {'title': 'No', 'payload': 'RESOLVED_NO'},
        ]
    },
    "MBOB_TX_FAILED": {
        'text': 'As per the RMA and force credit policy, all interbank failed transactions will be credited to the beneficiary’s account on the next working day if the beneficiary account is valid and active. Hence please allow us time for the payment to process.\n\nPlease let us know if you are satisfied with the resolution.',
        'buttons': [
            {'title': 'Yes', 'payload': 'RESOLVED_YES'},
            {'title': 'No', 'payload': 'RESOLVED_NO'},
        ]
    },
    "MBOB_DEVICE_CHANGE": {
        'text': '<b>mBoB Device Change</b>\n\nAn individual mBoB user can only access mBoB from one device at a time. If\nyou have changed your device and wish to access mBoB on a new device,\nplease call us at our Toll-Free Number 1095 (Within Bhutan) or visit the nearest\nBoB branch. For customers residing abroad, please call us at +975-2-349903\nor email the duly filled mBoB Change Request form to mbob@bob.bt\n\nPlease let us know if you are satisfied with the resolution.',
        'buttons': [
            {'title': 'Yes', 'payload': 'RESOLVED_YES'},
            {'title': 'No', 'payload': 'RESOLVED_NO'},
        ]
    },
    "MBOB_LIMIT": {
        'text': '<b>Fund Transfer Limit</b>\n\nFollowing are the details:\n\n1. <b>Within BoB Accounts (Accounts with Signature)</b>: Unlimited. However, it depends on your mBoB Category:\n   - <b>Gold Category</b>: Unlimited\n   - <b>Silver Category</b>: Nu. 500,000 (Daily Limit)\n   - <b>General Category</b>: Nu. 100,000 (Daily Limit)\n\n2. <b>Within BoB Accounts (Thumbprint Account)</b>:\n   - <b>Daily Limit</b>: Nu. 5,000\n   - <b>Transaction Limit</b>: Nu. 3,000\n\n3. <b>BoB to Other Banks</b>:\n   - <b>Daily Limit</b>: Nu. 1 Million per day (as per RMA guidelines)\n\nPlease let us know if you are satisfied with the resolution.',
        'buttons': [
            {'title': 'Yes', 'payload': 'RESOLVED_YES'},
            {'title': 'No', 'payload': 'RESOLVED_NO'},
        ]
    },
    "MBOB_CATEGORY": {
        'text': '<b>Check/Change Fund Transfer Category</b>\n\nTo check your mBoB fund transfer category, follow the steps below:\n1. Login to <b>mBoB</b>\n2. Tap on the drop-down menu on the top left corner after successful login\n3. Tap “Change Category”. Your current category will be displayed at the top\nfollowed by the option to change your new Category.\n\n\nPlease let us know if you are satisfied with the resolution.',
        'buttons': [
            {'title': 'Yes', 'payload': 'RESOLVED_YES'},
            {'title': 'No', 'payload': 'RESOLVED_NO'},
        ]
    },
    "CC_FRAUD": {
        'text': 'To prevent unauthorized or fraudulent activity, cardholders may immediately block their card via mBoB or request a card replacement.\n\nPlease let us know if you are satisfied with the resolution.',
        'buttons': [
            {'title': 'Yes', 'payload': 'RESOLVED_YES'},
            {'title': 'No', 'payload': 'RESOLVED_NO'},
        ]
    },
    "CC_ELIGIBILITY": {
        'text': 'Any Bhutanese between the age of 18 to 70 years with a legitimate repayment source. Salaried employees with minimum net take home pay of Nu.10,040/-.\n\nPlease let us know if you are satisfied with the resolution.',
        'buttons': [
            {'title': 'Yes', 'payload': 'RESOLVED_YES'},
            {'title': 'No', 'payload': 'RESOLVED_NO'},
        ]
    },
    "CC_TYPES": {
        'text': '<b>Types of Credit Cards</b>\n\n* <b>Visa Domestic Credit card</b>: Valid in Bhutan, India & Nepal.\n* <b>Visa International Credit card</b>: Valid outside Bhutan, India & Nepal.\n* <b>Corporate Credit card</b>: Valid in all countries.\n\nPlease let us know if you are satisfied with the resolution.',
        'buttons': [
            {'title': 'Yes', 'payload': 'RESOLVED_YES'},
            {'title': 'No', 'payload': 'RESOLVED_NO'},
        ]
    },
    "CC_ISSUANCE_FEE": {
        'text': 'The issuance Fee of credit card is Nu.525 Per Card.\n\nPlease let us know if you are satisfied with the resolution.',
        'buttons': [
            {'title': 'Yes', 'payload': 'RESOLVED_YES'},
            {'title': 'No', 'payload': 'RESOLVED_NO'},
        ]
    },
    "CC_ANNUAL_FEE": {
        'text': 'The credit card will be charged with Nu.1048.95 annually as annual Fee.\n\nPlease let us know if you are satisfied with the resolution.',
        'buttons': [
            {'title': 'Yes', 'payload': 'RESOLVED_YES'},
            {'title': 'No', 'payload': 'RESOLVED_NO'},
        ]
    },
    "CC_REPLACEMENT_FEE": {
        'text': 'The Fee for Credit card Replacement/Renewal is Nu.315 Per Card. You can apply this using mBoB.\n\nPlease let us know if you are satisfied with the resolution.',
        'buttons': [
            {'title': 'Yes', 'payload': 'RESOLVED_YES'},
            {'title': 'No', 'payload': 'RESOLVED_NO'},
        ]
    },
    "CC_LIMIT": {
        'text': 'The Maximum Card limit is up to Nu.150,000/-. You can increase your card limit against a collateral such as fixed assets, lien against deposit in CASA account, Fixed Deposit or Recurring Deposit account.\n\nPlease let us know if you are satisfied with the resolution.',
        'buttons': [
            {'title': 'Yes', 'payload': 'RESOLVED_YES'},
            {'title': 'No', 'payload': 'RESOLVED_NO'},
        ]
    },
    "CC_BILL": {
        'text': 'There are two payment options:\n1. <b>FAD (Full Amount Due)</b>: Total Due amount.\n2. <b>MAD (Minimum Amount Due)</b>: 10% of the FAD.\n\nThe cardholder can either opt to pay FAD or MAD. The cardholder can make the re-payment through mBoB or Choose for Auto debit (SI) from Savings account.\n\nPlease let us know if you are satisfied with the resolution.',
        'buttons': [
            {'title': 'Yes', 'payload': 'RESOLVED_YES'},
            {'title': 'No', 'payload': 'RESOLVED_NO'},
        ]
    },
    "CC_BLOCK": {
        'text': 'To prevent unauthorized or fraudulent activity, cardholders may immediately block their card via mBoB or request a card replacement. To block your credit card, call 1095 or send email to creditcard@bob.bt. However, transaction controls can be turned OFF/ON via mbob. Login to mbob app > select cards > select card > manage card > card controls > turn off the toggle switch for ATM/Online/POS. Your credit card will be temporarily blocked for further transactions.\nNavigation path: 1. Ans: To block your credit card, call 1095 or send email to creditcard@bob.bt. However, transaction controls can be turned OFF/ON via mbob. Login to mbob app -> 2. select cards -> 3. select card -> 4. manage card -> 5. card controls -> 6. turn off the toggle switch for ATM/Online/POS. Your credit card will be temporarily blocked for further transactions.\n\nPlease let us know if you are satisfied with the resolution.',
        'buttons': [
            {'title': 'Yes', 'payload': 'RESOLVED_YES'},
            {'title': 'No', 'payload': 'RESOLVED_NO'},
        ]
    },
    "CC_ACTIVATE": {
        'text': 'Ans: You can activate your new/ replaced issued credit cards using the MBOB app.\nTo activate the card, login to mbob > select cards > credit card > activate>set card pin > enter four-digit pin of your choice > submit.\nNavigation path: 1. To activate the card, login to mbob -> 2. select cards -> 3. credit card -> 4. activate -> 5. set card pin -> 6. enter four-digit pin of your choice -> 7. submit.\n\nPlease let us know if you are satisfied with the resolution.',
        'buttons': [
            {'title': 'Yes', 'payload': 'RESOLVED_YES'},
            {'title': 'No', 'payload': 'RESOLVED_NO'},
        ]
    },
    "DC_ISSUANCE_FEE": {
        'text': 'The issuance Fee of debit card is Nu.315 Per Card.You can apply this using mBoB.\n\nPlease let us know if you are satisfied with the resolution.',
        'buttons': [
            {'title': 'Yes', 'payload': 'RESOLVED_YES'},
            {'title': 'No', 'payload': 'RESOLVED_NO'},
        ]
    },
    "DC_REPLACEMENT_FEE": {
        'text': 'The Fee for debit card Replacement/Renewal is Nu.315 Per Card. You can apply this using mBoB.\n\nPlease let us know if you are satisfied with the resolution.',
        'buttons': [
            {'title': 'Yes', 'payload': 'RESOLVED_YES'},
            {'title': 'No', 'payload': 'RESOLVED_NO'},
        ]
    },
    "DC_FRAUD": {
        'text': 'To prevent unauthorized or fraudulent activity, cardholders may immediately block their card via mBoB or request a card replacement.\n\nPlease let us know if you are satisfied with the resolution.',
        'buttons': [
            {'title': 'Yes', 'payload': 'RESOLVED_YES'},
            {'title': 'No', 'payload': 'RESOLVED_NO'},
        ]
    },
    "DC_TYPES": {
        'text': '<b>Types of Debit Cards</b>\n\nProprietary Debit card – Valid within Bhutan only.\nVisa Domestic debit card – Valid in Bhutan, India & Nepal.\nVisa International debit card (Public) – Valid outside Bhutan, India & Nepal.\nVisa International debit card (Student) – Valid outside Bhutan, India & Nepal.\n\nPlease let us know if you are satisfied with the resolution.',
        'buttons': [
            {'title': 'Yes', 'payload': 'RESOLVED_YES'},
            {'title': 'No', 'payload': 'RESOLVED_NO'},
        ]
    },
    "DC_STUDENT": {
        'text': 'The student card is issued to suffice your living expenses abroad. Therefore, upon issuance of the card, bank will not remit or bank transfer your monthly living allowance and vice versa. Card validity is based on applicant student’s study period up to 4 years.\n\nPlease let us know if you are satisfied with the resolution.',
        'buttons': [
            {'title': 'Yes', 'payload': 'RESOLVED_YES'},
            {'title': 'No', 'payload': 'RESOLVED_NO'},
        ]
    },
    "DC_DOCS_STUDENT": {
        'text': '<b>Documentation - Visa International debit card (Student)</b>\n\n• Valid passport copy\n• Duly filled application or renewal forms\n• University admission/enrollment letter\n• Valid visa/permits (for future students)\n• Valid visa/permits (for current students).\n• Student ID\n\nPlease let us know if you are satisfied with the resolution.',
        'buttons': [
            {'title': 'Yes', 'payload': 'RESOLVED_YES'},
            {'title': 'No', 'payload': 'RESOLVED_NO'},
        ]
    },
    "DC_ELIGIBILITY_DOM": {
        'text': 'All savings bank account holders with BoB and account with Individual, Either or Survivor (E OR S) are eligible. Thumb impression/Joint account holders & Non-Bhutanese Nationals are NOT ELIGIBLE.\n\nPlease let us know if you are satisfied with the resolution.',
        'buttons': [
            {'title': 'Yes', 'payload': 'RESOLVED_YES'},
            {'title': 'No', 'payload': 'RESOLVED_NO'},
        ]
    },
    "DC_LIMIT_DOM": {
        'text': '<b>Withdrawal Limit on Domestic debit card</b>\n\nCardholders may utilize funds up to their available account balance, subject to the transaction limit as below.\n\nCash Withdrawal:\n• Nu. 15,000 per transaction. Up to Nu.40,000 per day in BOB ATMs & Nu.30,000 per day in BFS ATMs.\n• INR 10,000 Per day and up to INR 15,000 per month in India/Nepal.\n\nPOS:\n• Nu. 500,000 Per transaction in BOB - POS Terminals with unlimited daily/monthly limit.\n• INR 50,000 per month in POS - Visa Network Terminals in India/Nepal.\n\nPlease let us know if you are satisfied with the resolution.',
        'buttons': [
            {'title': 'Yes', 'payload': 'RESOLVED_YES'},
            {'title': 'No', 'payload': 'RESOLVED_NO'},
        ]
    },
    "DC_ELIGIBILITY_INTL": {
        'text': 'All savings bank account holders with BoB and account with Either or Survivor (E OR S) are eligible. Thumb impression/Joint account holders are NOT ELIGIBLE.\n\nPlease let us know if you are satisfied with the resolution.',
        'buttons': [
            {'title': 'Yes', 'payload': 'RESOLVED_YES'},
            {'title': 'No', 'payload': 'RESOLVED_NO'},
        ]
    },
    "DC_LIMIT_INTL": {
        'text': '<b>Withdrawal Limit on International debit card</b>\n\nCardholders may utilize funds up to their available account balance, subject to a maximum annual expenditure limit.\n\nVisa International debit card (Public): USD 1,000 + ATS (If ATS is added) in a year.\nVisa International debit card (Student): USD 1,200/- (Approx. AUD 1,730/- Per month). & USD 10,000 + ATS (if ATS is added) in a year.\n\nPlease let us know if you are satisfied with the resolution.',
        'buttons': [
            {'title': 'Yes', 'payload': 'RESOLVED_YES'},
            {'title': 'No', 'payload': 'RESOLVED_NO'},
        ]
    },
    "DC_NEW_REQUEST": {
        'text': 'To avail a new card, you are required to visit our nearest Bank of Bhutan branch office.\n\nPlease let us know if you are satisfied with the resolution.',
        'buttons': [
            {'title': 'Yes', 'payload': 'RESOLVED_YES'},
            {'title': 'No', 'payload': 'RESOLVED_NO'},
        ]
    },
    "DC_BLOCK": {
        'text': 'To prevent unauthorized or fraudulent activity, cardholders may immediately block their card via mBoB or request a card replacement. To block your debit card, call 1095 or Login to mbob app > select cards > select account > select card > manage card > card ON/OFF\nNavigation path: 1. Ans: To block your debit card, call 1095 or Login to mbob app -> 2. select cards -> 3. select account -> 4. select card -> 5. manage card -> 6. card ON/OFF\n\nPlease let us know if you are satisfied with the resolution.',
        'buttons': [
            {'title': 'Yes', 'payload': 'RESOLVED_YES'},
            {'title': 'No', 'payload': 'RESOLVED_NO'},
        ]
    },
    "DC_ACTIVATE": {
        'text': 'Ans: You can activate your new/ replaced issued debit cards using the MBOB app.\nTo activate the card, login to mbob > select cards > debit card > Select Account and activate > set card pin > enter four-digit pin of your choice > submit.\nNavigation path: 1. To activate the card, login to mbob -> 2. select cards -> 3. debit card -> 4. Select Account and activate -> 5. set card pin -> 6. enter four-digit pin of your choice -> 7. submit.\n\nPlease let us know if you are satisfied with the resolution.',
        'buttons': [
            {'title': 'Yes', 'payload': 'RESOLVED_YES'},
            {'title': 'No', 'payload': 'RESOLVED_NO'},
        ]
    },
    "GOBOB_FAQ_WHAT": {
        'text': '<b>What is GoBoB</b>\n\nGoBoB is a digital wallet service offered by the Bank of Bhutan. It enables users to securely store funds and perform various financial transactions without the need to open a savings or current account.\n\nPlease let us know if you are satisfied with the resolution.',
        'buttons': [
            {'title': 'Yes', 'payload': 'RESOLVED_YES'},
            {'title': 'No', 'payload': 'RESOLVED_NO'},
        ]
    },
    "GOBOB_BLOCKED": {
        'text': '<b>Login Access Blocked - GoBoB</b>\n\nTo reset MPIN or unblock login access to goBoB:\n1. Open <b>goBoB App</b>\n2. Tap <b>“Forgot M-PIN”</b> option on the login page and login with OTP. \n\n<i>Note: If you receive an error message such as “Entered details are not valid”, please prepare a copy of your CID or family tree (in case of a minor) and visit the nearest BoBL branch.</i>\n\nPlease let us know if you are satisfied with the resolution.',
        'buttons': [
            {'title': 'Yes', 'payload': 'RESOLVED_YES'},
            {'title': 'No', 'payload': 'RESOLVED_NO'},
        ]
    },
    "GOBOB_REG": {
        'text': '<b>Registration - goBoB</b>\n\nAnyone can register and use goBoB wallet including minors with a mobile number, email address & CID/Passport/Work permit. However, minors between the age of 10 and under 18 can use goBoB with minimal transaction rights only.\n\nPlease let us know if you are satisfied with the resolution.',
        'buttons': [
            {'title': 'Yes', 'payload': 'RESOLVED_YES'},
            {'title': 'No', 'payload': 'RESOLVED_NO'},
        ]
    },
    "GOBOB_HOW_TO_REG": {
        'text': '<b>How to Register</b>\n\nYou can download the goBoB application and can register instantly. However, you can also visit nearest BoB branch offices to register for the service.\n\nPlease let us know if you are satisfied with the resolution.',
        'buttons': [
            {'title': 'Yes', 'payload': 'RESOLVED_YES'},
            {'title': 'No', 'payload': 'RESOLVED_NO'},
        ]
    },
    "GOBOB_TOURIST": {
        'text': '<b>Registration for Tourist</b>\n\nTourists can conveniently register for the goBoB wallet even before arriving in Bhutan. They can also load funds into the wallet using their cards, ensuring a safe and hassle-free travel experience. This allows tourists to connect and resolve any issue with banks prior to the travel to Bhutan. Providing the correct information during the registration will be critical to ensuring seamless experience.\n\nPlease let us know if you are satisfied with the resolution.',
        'buttons': [
            {'title': 'Yes', 'payload': 'RESOLVED_YES'},
            {'title': 'No', 'payload': 'RESOLVED_NO'},
        ]
    },
    "GOBOB_TOURIST_KYC": {
        'text': '<b>KYC verification for Tourist Customers</b>\n\nThe tourist customer can load money into the wallet but will not be able to initiate any transactions from the wallet unless KYC is verified. The Tourist KYC is verified with the Department of Immigration (DOI). Verification needs to be initiated by the customer through ‘Verify KYC’ option available under App’s settings. KYC verification with DOI is instant. However, the customer must ensure that their personal information is correctly provided during the registration. Upon successful KYC verification, the customer can initiate transactions in a seamless manner.\n\nPlease let us know if you are satisfied with the resolution.',
        'buttons': [
            {'title': 'Yes', 'payload': 'RESOLVED_YES'},
            {'title': 'No', 'payload': 'RESOLVED_NO'},
        ]
    },
    "GOBOB_KYC": {
        'text': '<b>KYC Verification</b>\n\nKYC verification elevates your transaction limit categories, requiring a physical verification visit to your nearest branch.\n\nPlease let us know if you are satisfied with the resolution.',
        'buttons': [
            {'title': 'Yes', 'payload': 'RESOLVED_YES'},
            {'title': 'No', 'payload': 'RESOLVED_NO'},
        ]
    },
    "GOBOB_LOST": {
        'text': '<b>Block goBoB if lost Device</b>\n\nYou may call us at your toll free 1095 (Within Bhutan) or +975-2-349903 (Calling from Abroad) to temporarily block the transaction access for goBoB incase of device/phone lost.\n\nPlease let us know if you are satisfied with the resolution.',
        'buttons': [
            {'title': 'Yes', 'payload': 'RESOLVED_YES'},
            {'title': 'No', 'payload': 'RESOLVED_NO'},
        ]
    },
    "GOBOB_CHARGES": {
        'text': '<b>Charges</b>\n\nRegistration is free. There are no charges for other services except for adding money from cards and transfer to bank accounts. A convenience fee of 3.68% will be charged while loading your wallet using cards and 2.1% will be charged while sending money to the bank accounts.\n\nPlease let us know if you are satisfied with the resolution.',
        'buttons': [
            {'title': 'Yes', 'payload': 'RESOLVED_YES'},
            {'title': 'No', 'payload': 'RESOLVED_NO'},
        ]
    },
    "GOBOB_QR": {
        'text': '<b>QR Scan</b>\n\nThe QR Scan to Pay payment from goBoB is free and there are no charges for it.\n\nPlease let us know if you are satisfied with the resolution.',
        'buttons': [
            {'title': 'Yes', 'payload': 'RESOLVED_YES'},
            {'title': 'No', 'payload': 'RESOLVED_NO'},
        ]
    },
    "GOBOB_DEACTIVATE": {
        'text': '<b>Deactivate goBoB</b>\n\ngoBoB wallet deactivation is not available through the App. Customers are required to fill out goBoB wallet deactivation form available at our website and submit to the nearest branch. In the event that the customer needs to reuse the wallet, customer will be required to re-register for the goBoB wallet.\n\nPlease let us know if you are satisfied with the resolution.',
        'buttons': [
            {'title': 'Yes', 'payload': 'RESOLVED_YES'},
            {'title': 'No', 'payload': 'RESOLVED_NO'},
        ]
    },
    "GOBOB_REFUND": {
        'text': '<b>Wallet balance refund request</b>\n\nThe refund will be accepted & processed only if the amount was previously loaded using your card.\n\nPlease let us know if you are satisfied with the resolution.',
        'buttons': [
            {'title': 'Yes', 'payload': 'RESOLVED_YES'},
            {'title': 'No', 'payload': 'RESOLVED_NO'},
        ]
    },
    "GOBOB_LIMIT": {
        'text': '<b>Different type of Customer Limit category</b>\n\n* <b>Minimal KYC (KYC not verified) & Minor (10 years to less than 18 years)</b>:\n  - <b>Daily Transaction Limit</b>: Nu. 2,000\n  - <b>Daily Balance Limit</b>: Nu. 5,000\n  - <b>Aggregated Monthly Limit</b>: Nu. 10,000\n\n* <b>Full KYC (KYC verified)</b>:\n  - <b>Daily Transaction Limit</b>: Nu. 30,000\n  - <b>Daily Balance Limit</b>: Nu. 50,000\n  - <b>Aggregated Monthly Limit</b>: Nu. 100,000\n\n* <b>Tourist and Non-tourist (KYC verified with Dept. of Immigration)</b>:\n  - <b>Daily Transaction Limit</b>: Nu. 10 million\n  - <b>Daily Balance Limit</b>: Nu. 20 million\n  - <b>Aggregated Monthly Limit</b>: Nu. 50 million\n\nPlease let us know if you are satisfied with the resolution.',
        'buttons': [
            {'title': 'Yes', 'payload': 'RESOLVED_YES'},
            {'title': 'No', 'payload': 'RESOLVED_NO'},
        ]
    },
    "ATS_FAQ_WHAT": {
        'text': '<b>What is ATS?</b>\n\nThe ATS is an additional Spending quota/opportunity (beyond the standard USD 1,000 limit) to do international transactions.\n\nPlease let us know if you are satisfied with the resolution.',
        'buttons': [
            {'title': 'Yes', 'payload': 'RESOLVED_YES'},
            {'title': 'No', 'payload': 'RESOLVED_NO'},
        ]
    },
    "ATS_AVAIL": {
        'text': '<b>Avail ATS</b>\n\nTo avail ATS on Card, you need to provide valid passport copy and confirmed air ticket to Third Countries one week prior to your departure date.\nATS requests on card submitted post-departure shall not be accepted.\n\nPlease let us know if you are satisfied with the resolution.',
        'buttons': [
            {'title': 'Yes', 'payload': 'RESOLVED_YES'},
            {'title': 'No', 'payload': 'RESOLVED_NO'},
        ]
    },
    "ATS_FAQ_LIMIT": {
        'text': '<b>ATS Limit</b>\n\nThe yearly limit is USD 3,000 per individual (USD 1,000 in cash & USD 2,000 can be added to international cards).\n\nPlease let us know if you are satisfied with the resolution.',
        'buttons': [
            {'title': 'Yes', 'payload': 'RESOLVED_YES'},
            {'title': 'No', 'payload': 'RESOLVED_NO'},
        ]
    },
    "ATS_CASH": {
        'text': '<b>For ATS - Cash</b>\n\nYou can avail USD 1,000 Cash from the Paro International Airport, BoB counter during the departure time.\n\nPlease let us know if you are satisfied with the resolution.',
        'buttons': [
            {'title': 'Yes', 'payload': 'RESOLVED_YES'},
            {'title': 'No', 'payload': 'RESOLVED_NO'},
        ]
    },
    "ATS_FAQ_CARD": {
        'text': '<b>For ATS – Add to Cards</b>\n\nEmail the details and documents to:\n• <b>International Debit Card</b>: debitcard@bob.bt\n• <b>International Credit Card</b>: creditcard@bob.bt\n\nPlease let us know if you are satisfied with the resolution.',
        'buttons': [
            {'title': 'Yes', 'payload': 'RESOLVED_YES'},
            {'title': 'No', 'payload': 'RESOLVED_NO'},
        ]
    },
    "ATS_FAQ_MINOR": {
        'text': '<b>ATS to minors who do not have a card</b>\n\nMinors below the age of 18 can avail the Annual Travel Scheme of USD 2,000 or USD 3,000 through their parent’s or guardian’s card, upon submission of the family tree, passport, and latest air ticket.\n\nPlease let us know if you are satisfied with the resolution.',
        'buttons': [
            {'title': 'Yes', 'payload': 'RESOLVED_YES'},
            {'title': 'No', 'payload': 'RESOLVED_NO'},
        ]
    },
    "ATS_FAQ_THIRD_PERSON": {
        'text': '<b>ATS to Third person</b>\n\nThe ATS cannot be added to another person’s card. Currently it\'s only approved for minors below 18 through their parent’s or guardian\'s card.\n\nPlease let us know if you are satisfied with the resolution.',
        'buttons': [
            {'title': 'Yes', 'payload': 'RESOLVED_YES'},
            {'title': 'No', 'payload': 'RESOLVED_NO'},
        ]
    },
    "ATS_FAQ_EXPIRY": {
        'text': '<b>ATS Expiry</b>\n\nATS is only valid for the current year. Unused ATS shall not be carried forward to the next calendar year.\n\nPlease let us know if you are satisfied with the resolution.',
        'buttons': [
            {'title': 'Yes', 'payload': 'RESOLVED_YES'},
            {'title': 'No', 'payload': 'RESOLVED_NO'},
        ]
    }
}
