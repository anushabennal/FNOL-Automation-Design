import re

def extract_fields(text):
    def find(pattern):
        m = re.search(pattern, text)
        return m.group(1) if m else None

    return {
        "policyNumber": find(r"policy number[:\s]*([a-z0-9-]+)"),
        "policyholderName": find(r"name of insured[:\s]*([a-z\s]+)"),
        "dateOfLoss": find(r"date of loss[:\s]*([0-9/]+)"),
        "location": find(r"location of loss[:\s]*([a-z0-9,\s]+)"),
        "description": find(r"description of accident[:\s]*(.+)"),
        "estimatedDamage": find(r"estimate amount[:\s]*([0-9,]+)"),
        "claimType": "injury" if "injur" in text else "auto",
        "attachments": "attached" if "attachment" in text else None
    }
