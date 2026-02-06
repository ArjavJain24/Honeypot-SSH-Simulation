# Honeypot-SSH-Simulation
A Python-based SSH Honeypot to detect and log unauthorized connection attempts

# SSH Honeypot Project 🐝

## 📌 Project Overview
This project implements a **Python-based SSH Honeypot** designed to simulate an SSH service and capture unauthorized connection attempts. The honeypot logs attacker IP addresses, timestamps, and SSH banner data for security analysis.

---

## 🎯 Objective
- To deploy a fake SSH service
- To detect unauthorized access attempts
- To log attacker behavior for threat analysis

---

## 🛠 Tools & Technologies
- Python 3
- Kali Linux
- SSH Client
- Socket Programming

---

## ⚙ How It Works
1. The honeypot listens on a fake SSH port (2222)
2. When an attacker connects, the connection is immediately closed
3. Attacker IP and SSH banner are logged
4. Logs are stored locally for analysis

---

## 🚀 Usage

### Run the Honeypot
```bash
python3 honeypot.py

Simulate an Attack
ssh test@localhost -p 2222

View Logs
cat honeypot.log

📂 Output

The honeypot records:

Timestamp

Attacker IP Address

SSH Banner Information

📚 Learning Outcomes

Honeypot deployment techniques

Network monitoring

Threat intelligence collection

Python socket programming

⚠ Disclaimer

This project is intended strictly for educational purposes. Do not deploy on production systems.

👨‍💻 Author

Arjav Jain
Cybersecurity Intern
