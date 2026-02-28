# 🔐 Advanced Brand Phishing Detector

A proactive threat intelligence tool designed to detect brand abuse, typosquatting, and phishing domains using similarity analysis, DNS validation, SSL inspection, and WHOIS intelligence.

---

## 🚀 Overview

The Advanced Brand Phishing Detector is a cybersecurity-focused web application that identifies potentially malicious domains targeting brands. 

It supports:

- 🔎 Brand Monitoring Mode (automatic domain generation)
- 🛠 Manual Domain Investigation Mode
- 📊 Risk scoring with detailed findings
- 📄 Automated PDF report generation

This project simulates real-world brand protection and threat intelligence workflows used by security companies.

---

## 🧠 Detection Techniques Implemented

- ✔️ Typosquatting Detection (Levenshtein Distance)
- ✔️ Homoglyph Detection (g00gle → google)
- ✔️ Keyword Abuse Detection (login, secure, verify)
- ✔️ Hyphen-based Deception Detection
- ✔️ DNS A-record Validation
- ✔️ SSL Certificate Verification
- ✔️ WHOIS-based Domain Age Analysis
- ✔️ Risk Scoring Engine

---

## 🏗 Architecture


User Input (Brand / Domains)
↓
Domain Generator (Typos + Keywords + TLDs)
↓
DNS Check | SSL Check | WHOIS Age
↓
Similarity Engine (Levenshtein + Homoglyph)
↓
Risk Engine (Score + Risk Level)
↓
Web Dashboard + PDF Report


---

## 🛠 Tech Stack

- Python
- Flask
- JavaScript (Frontend)
- DNS (dnspython)
- WHOIS
- SSL Inspection
- python-Levenshtein
- ReportLab (PDF generation)

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/yourusername/brand-phishing-detector.git
cd brand-phishing-detector
2️⃣ Create virtual environment
python -m venv venv
source venv/bin/activate   # Linux / Kali
3️⃣ Install dependencies
pip install -r requirements.txt

Or manually:

pip install flask dnspython python-whois reportlab python-Levenshtein
4️⃣ Run the application
python app.py

Visit:

http://127.0.0.1:5000
🎯 Features
🔹 Brand Monitoring Mode

Enter a brand name (e.g., google)
The system generates potential phishing variations and analyzes them.

🔹 Manual Investigation Mode

Input specific domains:

google-login.com, g00gle.net

The system evaluates risk in real-time.

📊 Risk Scoring Model

Risk is calculated based on:

Similarity to brand

Suspicious keywords

Domain age

DNS presence

SSL validity

Each domain is categorized as:

🟢 Low Risk

🟡 Medium Risk

🔴 High Risk

📄 Automated Report

Generates downloadable PDF reports including:

Domain details

Risk score

Risk level

Detection findings

🔐 Use Case

Brand protection teams

Threat intelligence analysts

SOC teams

Cybersecurity researchers

Internship portfolio project

📌 Future Improvements

API integration for threat intelligence feeds

VirusTotal integration

Email alert system

Dashboard analytics charts

Background scheduled scanning

⚠ Disclaimer

This tool is intended for educational and defensive cybersecurity purposes only.
