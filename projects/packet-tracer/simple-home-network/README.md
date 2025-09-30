# 📡 Simple Home Network – Cisco Packet Tracer

## 📖 Overview
This project demonstrates the setup of a **simple home network** using Cisco Packet Tracer.  
It includes a PC, a laptop, a wireless router, a cable modem, and an internet cloud.  
The goal is to learn how to configure devices, connect them correctly, and verify connectivity.

---

## 🎯 Objectives
- Build a small home network topology in Packet Tracer.  
- Configure devices to use **DHCP** for automatic IP addressing.  
- Verify connectivity by pinging an external server (`cisco.srv`).  
- Explore **logical vs physical topologies**.  
- Understand cabling types (Ethernet, coaxial, console). 

---

## 🖼️ Topology
### Logical View  
![Preview](packet-tracer/simple-home-network/images) 

---

## ⚙️ Steps Performed
1. Added devices to the workspace (PC, Laptop, Wireless Router, Cable Modem, Cloud).  
2. Connected devices using appropriate cables:  
   - PC → Router (Ethernet straight-through)  
   - Router → Cable Modem (Ethernet straight-through)  
   - Cable Modem → Cloud (Coaxial)  
3. Configured **DHCP** on the PC and Laptop.  
4. Verified IP configuration with:  
   ```bash
   ipconfig /all
   ping cisco.srv

---

## 🧠 Key Learnings
Difference between logical topology (how devices are connected) and physical topology (where devices are placed).
How DHCP assigns IP addresses dynamically.
Correct cabling choices for different device types.
Troubleshooting DNS and connectivity issues in a simulated environment.

---

## 📂 Files
home_network.pkt → The Packet Tracer project file.
screenshot1.png → Logical topology diagram.
screenshot2.png → Physical topology (optional).

## 🚀 How to Use
Download the .pkt file from this repo.
Open it in Cisco Packet Tracer (v8.2.2 or later recommended).
Explore the topology and configurations.

---

## 📌 Notes
This lab is part of my ongoing learning journey in networking. More projects will be added to this repository to showcase progress in areas such as:
- LAN/WAN setup
- Routing & switching
- VLANs
- Wireless networks
- Security basics
