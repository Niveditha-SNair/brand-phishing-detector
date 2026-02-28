import whois
from datetime import datetime

def domain_age(domain):
    try:
        data = whois.whois(domain)
        created = data.creation_date

        if isinstance(created, list):
            created = created[0]

        if not created:
            return "unknown"

        return (datetime.now() - created).days

    except Exception:
        return "unknown"
