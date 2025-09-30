# Wireshark Common Filters Reference

This file contains useful display filters for Wireshark. Copy & paste them into the filter bar when analyzing packet captures.

---

## 🔒 HTTPS / TLS

* Show only HTTPS traffic (default port 443):

  ```
  tcp.port == 443
  ```
* TLS handshakes (Client Hello):

  ```
  tls.handshake.type == 1
  ```
* TLS handshakes (Server Hello):

  ```
  tls.handshake.type == 2
  ```

---

## 🌍 DNS

* Show only DNS traffic (default port 53):

  ```
  dns
  ```
* Show DNS queries only:

  ```
  dns.flags.response == 0
  ```
* Show DNS responses only:

  ```
  dns.flags.response == 1
  ```

---

## 📡 ARP

* Show all ARP traffic:

  ```
  arp
  ```
* Show only ARP requests:

  ```
  arp.opcode == 1
  ```
* Show only ARP replies:

  ```
  arp.opcode == 2
  ```

---

## 📩 ICMP

* Show all ICMP (ping) traffic:

  ```
  icmp
  ```
* Show ICMP Echo requests:

  ```
  icmp.type == 8
  ```
* Show ICMP Echo replies:

  ```
  icmp.type == 0
  ```

---

## 💻 IP

* Filter packets by specific IP address:

  ```
  ip.addr == 192.168.1.10
  ```
* Exclude packets from a specific IP:

  ```
  !(ip.addr == 8.8.8.8)
  ```
* Source IP only:

  ```
  ip.src == 192.168.1.10
  ```
* Destination IP only:

  ```
  ip.dst == 192.168.1.10
  ```

---

## 🔀 TCP / UDP

* Show all TCP traffic:

  ```
  tcp
  ```
* Show all UDP traffic:

  ```
  udp
  ```
* Show TCP packets with retransmissions:

  ```
  tcp.analysis.retransmission
  ```
* Show TCP packets with SYN flag (handshake start):

  ```
  tcp.flags.syn == 1
  ```

---

## 🎯 Compound Filters

* HTTPS traffic excluding a specific IP:

  ```
  (tcp.port == 443) and !(ip.addr == 8.8.8.8)
  ```
* HTTP or HTTPS traffic only:

  ```
  tcp.port == 80 or tcp.port == 443
  ```

---

## 🧰 References

* [Wireshark Display Filters](https://wiki.wireshark.org/DisplayFilters)
* [Wireshark Cheat Sheet (PacketLife.net)](https://packetlife.net/media/library/13/Wireshark_Display_Filters.pdf)

---
