import itertools

PHISH_KEYWORDS = ["login", "secure", "verify", "account", "update", "support"]

def generate_domains(brand):
    tlds = ["com", "net", "org", "co", "info"]
    domains = set()

    # Basic typos
    domains.add(brand)
    domains.add(brand.replace("o", "0"))
    domains.add(brand.replace("i", "1"))

    for k in PHISH_KEYWORDS:
        for t in tlds:
            domains.add(f"{brand}-{k}.{t}")
            domains.add(f"{k}-{brand}.{t}")
            domains.add(f"{brand}{k}.{t}")

    return list(domains)
