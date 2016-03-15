#!/usr/bin/python

import time
from scapy.all import *

def sendCovertMsg(msgArray, targetIP, port, delay):
	os.system("ethtool --offload eno1 rx off tx off")
	for msgPart in msgArray:		
		pkt=IP(dst=targetIP)/UDP(dport=int(port), chksum=ord(msgPart))
		send(pkt)
		time.sleep(delay)
	return None

def decodeMsg(pkt):
	char = chr(pkt['UDP'].chksum)
	print char

def recieveCovertMsg(port):
	os.system("ethtool --offload eno1 rx off tx off")
	sniff(filter="udp and port "+port, prn=decodeMsg)
	return None
	

