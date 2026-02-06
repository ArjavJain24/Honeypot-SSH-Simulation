import socket
import datetime

HOST = "0.0.0.0"
PORT = 2222  # Fake SSH port

log_file = "honeypot.log"

def log_attack(addr, data):
    with open(log_file, "a") as f:
        f.write(f"[{datetime.datetime.now()}] IP: {addr[0]} | Data: {data}\n")

def start_honeypot():
    print(f"[+] Honeypot running on port {PORT}...")
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(5)

    while True:
        conn, addr = s.accept()
        print(f"[!] Connection from {addr[0]}")

        conn.send(b"SSH-2.0-OpenSSH_7.4\r\n")
        data = conn.recv(1024)

        log_attack(addr, data.decode(errors="ignore"))
        conn.close()

start_honeypot()
