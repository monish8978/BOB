$flows = "D:\BOB\app\chatbot\flows.py"
$engine = "D:\BOB\app\chatbot\engine.py"

$flowsContent = Get-Content $flows -Raw
$flowsContent = [regex]::Replace($flowsContent, '"title": "(Back Menu|Back to GoBoB Menu|Back to mBoB Menu|Return to Main Menu|Back)", "payload": "MAIN_MENU"', '"title": "Main Menu", "payload": "MAIN_MENU"')
$flowsContent = [regex]::Replace($flowsContent, '"title": "(Back Menu|Back to GoBoB Menu|Back to mBoB Menu|Back)", "payload": "(FLOW_[A-Z_]+|CARD_[A-Z_]+|GOBOB_[A-Z_]+)"', '"title": "Back to Menu", "payload": "$2"')
Set-Content -Path $flows -Value $flowsContent -NoNewline

$engineContent = Get-Content $engine -Raw
$engineContent = [regex]::Replace($engineContent, '"title": "(Back Menu|Back to GoBoB Menu|Back to mBoB Menu|Return to Main Menu|Back)", "payload": "MAIN_MENU"', '"title": "Main Menu", "payload": "MAIN_MENU"')
$engineContent = [regex]::Replace($engineContent, '"title": "(Back Menu|Back to GoBoB Menu|Back to mBoB Menu|Back)", "payload": "(FLOW_[A-Z_]+|CARD_[A-Z_]+|GOBOB_[A-Z_]+)"', '"title": "Back to Menu", "payload": "$2"')
Set-Content -Path $engine -Value $engineContent -NoNewline

Write-Host "Replacement done."
