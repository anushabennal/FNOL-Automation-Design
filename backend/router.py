def route_claim(fields):
    missing = [k for k, v in fields.items() if not v]

    desc = fields.get("description", "")
    damage = fields.get("estimatedDamage")

    if any(w in desc for w in ["fraud", "staged", "inconsistent"]):
        return "Investigation Flag", missing, "Suspicious keywords detected"

    if missing:
        return "Manual Review", missing, "Mandatory fields missing"

    if fields.get("claimType") == "injury":
        return "Specialist Queue", missing, "Injury-related claim"

    if damage and int(damage.replace(",", "")) < 25000:
        return "Fast-track", missing, "Low estimated damage"

    return "Standard Processing", missing, "Default routing"
