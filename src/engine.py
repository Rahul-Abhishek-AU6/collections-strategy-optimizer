def get_recommendation(borrower):
    if borrower.get("hardship_indicator"):
        return "hardship_support", "Hardship indicator detected."
    if borrower.get("days_past_due") > 60:
        return "escalation", "Delinquency exceeds 60 days."
    if borrower.get("days_past_due") > 30:
        return "agent_call", "Habitual late payer; requires personal outreach."
    return "sms_reminder", "Early delinquency stage; low-touch reminder."