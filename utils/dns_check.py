import dns.resolver

def check_dns(domain):
    try:
        dns.resolver.resolve(domain, 'A')
        return "active"
    except:
        return "not_registered"
