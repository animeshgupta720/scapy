# Automation with Scapy

Scapy is a powerful interactive packet manipulation program. It is able to forge or decode packets of a wide number of protocols, send them on the wire, capture them, match requests and replies, and much more. It can easily handle most classical tasks like scanning, tracerouting, probing, unit tests, attacks or network discovery

It also performs very well at a lot of other specific tasks that most other tools can't handle, like sending invalid frames, injecting your own 802.11 frames, combining technics (VLAN hopping+ARP cache poisoning, VOIP decoding on WEP encrypted channel, ...), etc.
This repo explores python automation use cases with the Scapy module in Python language.


```
(scapy_arp) agupta@network_automation_topics % python3 /Users/agupta/topics/network_automation_topics/arp_scapy.py
WARNING: No IPv4 address found on en5 !
WARNING: No IPv4 address found on ap1 !
WARNING: more No IPv4 address found on awdl0 !
.
Sent 1 packets.
.
```
