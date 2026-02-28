import Levenshtein

HOMOGLYPHS = {
    "0": "o",
    "1": "l",
    "3": "e",
    "5": "s",
    "@": "a"
}

def normalize(domain):
    for k, v in HOMOGLYPHS.items():
        domain = domain.replace(k, v)
    return domain

def levenshtein_score(domain, brand):
    return Levenshtein.distance(domain, brand)

def looks_like_brand(domain, brand):
    norm = normalize(domain)
    return brand in norm or levenshtein_score(norm, brand) <= 2

def typosquat(domain, brand):
    return levenshtein_score(domain, brand) <= 2
