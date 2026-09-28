# Basic Network Sniffer

## Description

This project captures live network packets using Python and the Scapy library.

The program displays:

- Source IP Address
- Destination IP Address
- Protocol
- TCP/UDP Ports
- Packet Length
- Payload

## Requirements

- Python 3.x
- Scapy

Install:

```bash
pip install -r requirements.txt
```

or

```bash
pip install scapy
```

## Run

Linux/macOS

```bash
sudo python network_sniffer.py
```

Windows

Open Command Prompt as Administrator.

```bash
python network_sniffer.py
```

## Example Output

```
======================================================================
Source IP      : 192.168.1.10
Destination IP : 142.250.183.206
Protocol Number: 6
Packet Length  : 74 bytes
Protocol Name  : TCP
Source Port    : 52630
Destination Port: 443

Payload:
GET / HTTP/1.1
======================================================================
```

## Features

- Captures live packets
- Detects TCP, UDP and ICMP
- Displays IP addresses
- Shows packet length
- Prints payload
- Simple Python implementation using Scapy

## Technologies Used

- Python
- Scapy

## Learning Outcomes

- Packet sniffing
- TCP/IP protocol analysis
- Understanding network packets
- Basic cybersecurity concepts

## Author

Your Name