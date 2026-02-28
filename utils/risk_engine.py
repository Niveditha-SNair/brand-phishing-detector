from utils.similarity import looks_like_brand, typosquat

def calculate_risk(domain, brand, dns, ssl):
    score = 0
    reasons = []

    if brand and looks_like_brand(domain, brand):  # <-- check brand exists
        score += 30
        reasons.append("Brand name or look-alike present")

    if "-" in domain:
        score += 15
        reasons.append("Hyphenated domain")

    if brand and typosquat(domain, brand):        # <-- check brand exists
        score += 20
        reasons.append("Possible typosquatting")

    if dns == "active":
        score += 15
        reasons.append("Active DNS records")

    if not ssl:
        score += 20
        reasons.append("No SSL certificate")

    if score >= 80:
        level = "High"
    elif score >= 50:
        level = "Medium"
    else:
        level = "Low"

    return score, level, reasons
