"""
Basic Network Sniffer
Author: Your Name

Description:
Captures live network packets and displays:
- Source IP
- Destination IP
- Protocol
- Packet Length
- Payload (if available)

Requirements:
pip install scapy

Run:
sudo python network_sniffer.py
Windows:
Run Command Prompt as Administrator.
"""

from scapy.all import sniff, IP, TCP, UDP, ICMP, Raw


def packet_callback(packet):
    print("=" * 70)

    if packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = packet[IP].proto
        length = len(packet)

        print(f"Source IP      : {src_ip}")
        print(f"Destination IP : {dst_ip}")
        print(f"Protocol Number: {protocol}")
        print(f"Packet Length  : {length} bytes")

        if packet.haslayer(TCP):
            print("Protocol Name  : TCP")
            print(f"Source Port    : {packet[TCP].sport}")
            print(f"Destination Port: {packet[TCP].dport}")

        elif packet.haslayer(UDP):
            print("Protocol Name  : UDP")
            print(f"Source Port    : {packet[UDP].sport}")
            print(f"Destination Port: {packet[UDP].dport}")

        elif packet.haslayer(ICMP):
            print("Protocol Name  : ICMP")

        else:
            print("Protocol Name  : Other")

        if packet.haslayer(Raw):
            payload = packet[Raw].load
            print("\nPayload:")
            try:
                print(payload.decode(errors="ignore"))
            except:
                print(payload)

    print("=" * 70)


def main():
    print("\nBasic Network Sniffer Started...")
    print("Press CTRL+C to stop.\n")

    sniff(
        prn=packet_callback,
        store=False
    )


if __name__ == "__main__":
    main()