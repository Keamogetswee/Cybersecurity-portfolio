📡 Simple Home Network – Cisco Packet Tracer
📖 Overview

This project demonstrates the setup of a simple home network using Cisco Packet Tracer. The network consists of a PC, a laptop, a wireless router, a cable modem, and an internet cloud. It showcases how to configure devices, connect them with the correct cabling, and verify connectivity.

🎯 Objectives

Build a small home network topology.

Configure devices to use DHCP for automatic IP addressing.

Verify connectivity by pinging an external server (cisco.srv).

Explore logical vs physical topologies in Packet Tracer.

Understand cabling types (Ethernet, coaxial, console).

🖼️ Topology
Logical View

(Insert screenshot of your logical workspace here)

Physical View

(Optional: screenshot of physical mode with rack/table/shelf if relevant)

⚙️ Steps Performed

Added devices to the workspace (PC, Laptop, Wireless Router, Cable Modem, Cloud).

Connected devices using appropriate cables:

PC → Router (Ethernet straight-through)

Router → Cable Modem (Ethernet straight-through)

Cable Modem → Cloud (Coaxial)

Configured DHCP on the PC and Laptop to automatically obtain IP addresses.

Verified IP configuration with ipconfig /all.

Tested connectivity with ping cisco.srv.

🧠 Key Learnings

Difference between logical topology (how devices are connected) and physical topology (where devices are placed).

How DHCP assigns IP addresses dynamically.

Correct cabling choices for different device types.

Troubleshooting DNS and connectivity issues in a simulated environment.

📂 Files

home_network.pkt → The Packet Tracer project file.

screenshot1.png → Logical topology diagram.

screenshot2.png → Physical topology (optional).

🚀 How to Use

Download the .pkt file from this repo.

Open it in Cisco Packet Tracer (v8.2.2 or later recommended).

Explore the topology and configurations.

📌 Notes

This lab is part of my ongoing learning journey in networking. More projects will be added to this repository to showcase progress in areas such as:

LAN/WAN setup

Routing & switching

VLANs

Wireless networks

Security basics
