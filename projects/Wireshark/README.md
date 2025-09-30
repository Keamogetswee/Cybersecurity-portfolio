# Wireshark for Beginners: Capture Packets

This project demonstrates my ability to set up and use **Wireshark** on Ubuntu to capture, filter, and analyze network traffic. The tasks were part of a guided lab, and I expanded on them to build practical cybersecurity skills.

---

## 🚀 Project Overview

Wireshark is a widely used packet analyzer that allows security professionals and network engineers to inspect traffic at a granular level.
In this project, I:

* Installed Wireshark on Ubuntu
* Configured non-root access for safer packet capturing
* Captured traffic on a wired interface
* Applied display filters to analyze HTTPS and TLS traffic
* Used conditional filters to exclude or include specific IPs

---

## 🛠️ Setup & Configuration

### Installation

```bash
sudo add-apt-repository ppa:wireshark-dev/stable
sudo apt update
sudo apt install wireshark
```

### Secure Configuration

During setup, Wireshark asks:
👉 *Should non-superusers be able to capture packets?*

* Selected **Yes** (best practice).
* Added user to the `wireshark` group:

  ```bash
  sudo usermod -aG wireshark $USER
  ```
* Logged out and back in.

This follows the **principle of least privilege**, ensuring Wireshark can capture packets without root access, minimizing security risks.

---

## 📋 Tasks Completed

### 1️⃣ Start a packet capture

* Captured traffic on the `en*` wired interface.
* Saved the capture to a `.pcap` file.

### 2️⃣ Detect HTTPS packets

* Applied filter:

  ```wireshark
  tcp.port == 443
  ```

### 3️⃣ Identify website IPs

* Detected TLS handshake packets:

  ```wireshark
  tls.handshake.type == 1
  ```
* Filtered by IP:

  ```wireshark
  ip.addr == 142.251.163.105
  ```

### 4️⃣ Exclude IPs from capture

* Applied conditional filter:

  ```wireshark
  !(ip.addr == 8.43.85.97) and (tcp.port == 80 or tcp.port == 443)
  ```

---

## 📚 Key Learnings

* How to securely configure Wireshark on Linux
* Importance of running packet captures as non-root
* Use of **display filters** to narrow down traffic (HTTPS, TLS, IP-based)
* Conditional filtering for advanced packet analysis
* Improved understanding of how HTTPS/TLS traffic appears in real packet traces

---

## 📂 Files in this Project

* `capture1.pcapng` → Example packet capture
* `filters.md` → Notes on useful Wireshark filters
* `README.md` → Project documentation (this file)

---

## 🔑 Skills Demonstrated

* Network traffic analysis
* Linux system administration
* Security best practices (least privilege)
* Wireshark filtering and capture techniques

---
