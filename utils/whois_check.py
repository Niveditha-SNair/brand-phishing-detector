import whois
from datetime import datetime

def domain_age(domain):
    try:
        w = whois.whois(domain)
        cd = w.creation_date

        if isinstance(cd, list):
            cd = cd[0]

        if cd:
            return (datetime.now() - cd).days
        return "unknown"

    except Exception:
        return "unknown"
