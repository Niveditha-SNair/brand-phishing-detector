from flask import Flask, render_template, request, jsonify, send_file
import io
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

# utils imports (VERY IMPORTANT)
from utils.domain_generator import generate_domains
from utils.dns_check import check_dns
from utils.ssl_check import check_ssl
from utils.domain_age import domain_age
from utils.risk_engine import calculate_risk

app = Flask(__name__)

# -----------------------------
# CORE ANALYSIS FUNCTION
# -----------------------------
def analyze_domain(domain, brand=None):
    dns = check_dns(domain)
    ssl = check_ssl(domain)
    age = domain_age(domain)

    score, level, reasons = calculate_risk(
        domain=domain,
        brand=brand,
        dns=dns,
        ssl=ssl
    )

    return {
        "domain": domain,
        "dns": dns,
        "ssl": "Valid" if ssl else "Invalid",
        "age": age,
        "risk": score,
        "level": level,
        "findings": reasons
    }

# -----------------------------
# ROUTES
# -----------------------------
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/scan", methods=["POST"])
def scan():
    data = request.get_json()
    mode = data.get("mode")

    results = []

    # 🔹 MODE 1: Brand Monitoring
    if mode == "brand":
        brand = data.get("brand", "").strip().lower()
        if not brand:
            return jsonify({"results": []})

        domains = generate_domains(brand)   # MANY domains here
        for d in domains:
            results.append(analyze_domain(d, brand))

    # 🔹 MODE 2: Manual Domain Investigation
    elif mode == "manual":
        raw = data.get("domains", "")
        domains = [d.strip() for d in raw.split(",") if d.strip()]

        for d in domains:
            results.append(analyze_domain(d))

    return jsonify({"results": results})

# -----------------------------
# PDF REPORT
# -----------------------------
@app.route("/download-report", methods=["POST"])
def download_report():
    data = request.get_json()

    buffer = io.BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=A4)
    text = pdf.beginText(40, 800)

    text.setFont("Helvetica-Bold", 14)
    text.textLine("Advanced Brand Phishing Scanner Report")
    text.textLine("")

    text.setFont("Helvetica", 10)

    for r in data:
        text.textLine(f"Domain: {r['domain']}")
        text.textLine(f"Risk Score: {r['risk']} ({r['level']})")
        text.textLine(f"DNS: {r['dns']} | SSL: {r['ssl']} | Age: {r['age']}")
        for f in r["findings"]:
            text.textLine(f" - {f}")
        text.textLine("")

    pdf.drawText(text)
    pdf.save()

    buffer.seek(0)
    return send_file(
        buffer,
        as_attachment=True,
        download_name="phishing_report.pdf",
        mimetype="application/pdf"
    )

# -----------------------------
if __name__ == "__main__":
    app.run(debug=True)
