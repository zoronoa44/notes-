# 🌐 Week 2 — Networking Notes
> By Atharva | Pre-College Roadmap

---

## 📡 DAY 1 — How Internet Works + IP

### What is the Internet?
- A global network of computers connected together
- Data travels in **packets** — small chunks of data
- Every device has an **IP address** — its unique identity

### Public vs Private IP
| Type | Example | Who assigns it |
|------|---------|---------------|
| Private | 192.168.x.x | Your router |
| Public | 103.21.x.x | Your ISP |

```
Your PC (192.168.1.5) → Router → ISP → Internet
Private IP              Public IP
```

### Terminal Commands
```bash
ping google.com          # test connection
traceroute google.com    # see every hop to destination
curl ifconfig.me         # see your public IP
ip addr                  # see your local IP
```

### Key Concepts
- **Packet** = chunk of data traveling on network
- **TTL (Time To Live)** = max hops before packet dies
- **ISP** = Internet Service Provider — gives you internet

---

## 🤝 DAY 2 — TCP/IP + Wireshark

### TCP 3-Way Handshake
```
Your PC                    Server
   │                          │
   │ ──── SYN ──────────────► │   "Hey, can we talk?"
   │ ◄─── SYN-ACK ─────────── │   "Yeah, I'm here"
   │ ──── ACK ──────────────► │   "Cool, let's go"
   │ ════ DATA FLOWS ════════ │
```

| Flag | Meaning |
|------|---------|
| SYN | Synchronize — want to connect |
| SYN-ACK | Accepted + I also want to connect |
| ACK | Acknowledge — confirmed |

### Wireshark UI
```
┌─────────────────────────────────┐
│  FILTER BAR                     │
├─────────────────────────────────┤
│  PACKET LIST                    │
├─────────────────────────────────┤
│  PACKET DETAILS                 │
├─────────────────────────────────┤
│  PACKET BYTES (hex)             │
└─────────────────────────────────┘
```

### Wireshark Filters
```
tcp                        → TCP packets only
udp                        → UDP packets only
dns                        → DNS packets only
http                       → HTTP packets only
icmp                       → Ping packets only
ip.addr == 8.8.8.8         → specific IP
tcp.port == 80             → specific port
tcp.flags.syn == 1         → only SYN packets
```

### Wireshark Colors
| Color | Meaning |
|-------|---------|
| Light blue | UDP |
| Light purple | TCP |
| Black + red text | TCP errors |
| Green | HTTP |
| Yellow | Broadcast |

### Key Concepts
- **Wireshark** = packet sniffer — captures all network traffic
- **Interface** = door where data enters/exits your PC
- **Follow TCP Stream** = read full HTTP conversation
- Right click packet → Follow → TCP Stream

---

## 🌍 DAY 3 — DNS

### What is DNS?
> DNS = Internet ka Phone Book
> Translates domain names → IP addresses

```
You type: google.com
              ↓
DNS returns: 142.250.183.14
              ↓
Browser connects to that IP
```

### DNS Resolution Flow
```
Browser Cache → OS Cache → Recursive Resolver
→ Root Server → TLD Server (.com)
→ Authoritative Server → IP returned ✅
```

### DNS Record Types
| Record | Meaning |
|--------|---------|
| A | domain → IPv4 |
| AAAA | domain → IPv6 |
| CNAME | alias → another domain |
| MX | mail server |
| NS | name server |
| TXT | verification |
| PTR | IP → domain (reverse) |

### Terminal Commands
```bash
nslookup google.com              # basic DNS lookup
nslookup google.com 8.8.8.8      # ask specific DNS server
dig google.com                   # detailed DNS lookup
dig google.com MX                # mail servers
dig google.com +trace            # full DNS tree walk
dig -x 8.8.8.8                   # reverse DNS lookup
cat /etc/resolv.conf             # your DNS server
```

### /etc/hosts File
```
# Local override — checked BEFORE DNS
127.0.0.1    localhost
1.2.3.4      fakegoogle.com   ← DNS never consulted
```

**Used for:**
- Local development 🧪
- Malware redirects 😈
- Ad blocking 🚫

### DNS Security
| Attack | What happens |
|--------|-------------|
| DNS Spoofing | Fake response → wrong IP |
| Cache Poisoning | Corrupt resolver cache |
| DNS Hijacking | ISP redirects your DNS |
| Protection | Use DoH (DNS over HTTPS) |

### Key Concepts
- DNS uses **UDP port 53** (fast, small packets)
- **TTL** = how long to cache the answer
- **Transaction ID** = matches query to response
- Change DNS to `1.1.1.1` (Cloudflare) for privacy

---

## 🌐 DAY 4 — HTTP/HTTPS

### Request/Response Cycle
```
Browser ──── HTTP REQUEST ────► Server
Browser ◄─── HTTP RESPONSE ──── Server
```

### HTTP Methods
| Method | Use |
|--------|-----|
| GET | Fetch data |
| POST | Send data |
| PUT | Update data |
| DELETE | Delete data |

### Status Codes
```
2xx = Success ✅
3xx = Redirect
4xx = YOUR fault 💀
5xx = Server's fault 💀
```

| Code | Meaning |
|------|---------|
| 200 | OK |
| 301 | Moved Permanently |
| 404 | Not Found |
| 500 | Server Error |

> **Memory trick:**
> 4 = you're the 4ool who typed wrong URL 😭
> 5 = Server ki 5itting broke 💀

### Terminal Commands
```bash
curl http://example.com           # fetch page
curl -v http://example.com        # verbose — see everything
curl -I https://google.com        # headers only
curl -L http://github.com         # follow redirects
```

### HTTP vs HTTPS
```
HTTP  → plaintext → anyone can read 😱
HTTPS → encrypted via TLS → unreadable 🔒
```

### Cookies
```
First visit  → server sends: Set-Cookie: session=abc
Next visit   → browser sends: Cookie: session=abc
Server: "Oh it's you, you're logged in" ✅
```

### Important Headers
```
Request:                     Response:
Host: google.com             Content-Type: text/html
User-Agent: Mozilla          Set-Cookie: session=abc
Cookie: session=abc          Location: https://...
Authorization: Bearer xyz    Cache-Control: max-age=300
```

---

## 🔐 DAY 5 — Ports + SSH

### What is a Port?
```
IP Address = apartment building 🏢
Port       = flat number inside 🚪

192.168.1.5:80  = building, flat 80 (HTTP)
192.168.1.5:22  = building, flat 22 (SSH)
```

### Important Ports
| Port | Protocol |
|------|----------|
| 22 | SSH |
| 53 | DNS |
| 80 | HTTP |
| 443 | HTTPS |
| 3306 | MySQL |
| 8080 | Dev server |

### Terminal Commands
```bash
netstat -tulpn          # see all listening ports
nmap localhost          # scan your own ports
nmap scanme.nmap.org    # scan legal practice target
nmap -sV scanme.nmap.org # detect service versions
```

### SSH — Secure Shell
```
Your Laptop ══ encrypted tunnel ══► Server
Type commands → execute on remote server
```

**SSH vs Telnet:**
```
Telnet = postcard 📮 (plaintext, anyone reads)
SSH    = sealed envelope 📨 (encrypted) ✅
```

### SSH Key Pair
```
Public Key  = Lock 🔒 (put on server, share freely)
Private Key = Key  🗝️ (NEVER share)
```

```bash
# Generate key
ssh-keygen -t ed25519 -C "email@gmail.com"

# See keys
ls ~/.ssh/
cat ~/.ssh/id_ed25519.pub    # public key

# Connect to server
ssh -i key.pem ubuntu@YOUR-IP

# Fix permissions
chmod 400 key.pem
```

### Nmap Rules ⚠️
```
✅ nmap localhost
✅ nmap scanme.nmap.org
✅ nmap YOUR-OWN-SERVER
❌ nmap random websites (illegal)
❌ nmap google.com
```

---

## 🐍 DAY 6 — Python + Networking

### Socket Basics
```python
import socket

# Create socket
s = socket.socket()

# Set timeout
s.settimeout(0.5)

# Try connecting
result = s.connect_ex(("target.com", 80))
# 0 = OPEN ✅
# 1 = CLOSED ❌

# Close socket
s.close()

# Get service name from port
service = socket.getservbyport(80)  # "http"

# Domain → IP
ip = socket.gethostbyname("google.com")
```

### Port Scanner
```python
import socket
from datetime import datetime

def scan_port(target, port):
    s = socket.socket()
    s.settimeout(0.5)
    result = s.connect_ex((target, port))
    s.close()
    return result == 0

def scan_target(target, start_port, end_port):
    print("-" * 50)
    try:
        ip = socket.gethostbyname(target)
        print(f"Target: {target} ({ip})")
    except socket.gaierror:
        print("Could not resolve hostname")
        return

    open_ports = []
    start_time = datetime.now()

    for port in range(start_port, end_port + 1):
        if scan_port(target, port):
            try:
                service = socket.getservbyport(port)
            except:
                service = "unknown"
            print(f"[OPEN] Port {port} → {service}")
            open_ports.append(port)

    elapsed = datetime.now() - start_time
    print(f"\nDone in {elapsed}. {len(open_ports)} open ports.")

scan_target("scanme.nmap.org", 1, 1024)
```

### Python Code Quality Rules
```
✅ Input validation — always wrap int(input()) in try/except
✅ Remove unused variables (k=0, no_list=[])
✅ DRY — don't repeat code
✅ Magic numbers → use constants (MAX_LIVES = 3)
✅ Spelling matters — "remaining" not "remaning"
```

---

## 📋 MASTER CHEATSHEET

### Units
```
1s   = 1000ms  (milliseconds)
1ms  = 1000μs  (microseconds)
1μs  = 1000ns  (nanoseconds)

20ms = 0.02 seconds (NOT 0.2) 💀
```

### OSI Model (Quick)
```
7. Application  → HTTP, DNS, FTP
4. Transport    → TCP, UDP
3. Network      → IP
2. Data Link    → Ethernet, MAC
1. Physical     → Cables, WiFi
```

### Security Mindset
```
/etc/hosts edited    → malware sign 🚨
Pirated software     = root access to stranger 💀
Public WiFi + HTTP   = readable by everyone 😱
SSH > Telnet         always
HTTPS > HTTP         always
ed25519 > RSA        for SSH keys
1.1.1.1 > ISP DNS   for privacy
```

### Git Commands
```bash
git init                          # start repo
git add file.py                   # stage file
git commit -m "message"           # save
git remote add origin URL         # link to github
git push -u origin main           # upload
git remote -v                     # check where pushing
git branch -M main                # rename branch
git push origin main --force      # force push
```

---

## 🎯 Interview Questions

**Q: What is DNS?**
> Translates domain names to IP addresses. Uses UDP port 53.

**Q: What is TCP 3-way handshake?**
> SYN → SYN-ACK → ACK. Establishes connection before data transfer.

**Q: HTTP vs HTTPS?**
> HTTP = plaintext. HTTPS = HTTP + TLS encryption.

**Q: 404 vs 500?**
> 404 = client's fault (wrong URL). 500 = server's fault (crash).

**Q: What is SSH?**
> Encrypted remote access protocol. Uses port 22. Replaces Telnet.

**Q: Public vs Private IP?**
> Private = local network (192.168.x.x). Public = internet-facing IP assigned by ISP.

**Q: What is a socket?**
> Endpoint for communication between two computers. Foundation of all networking.

---

*Week 2 Complete 🔥 | Next: Week 3*
