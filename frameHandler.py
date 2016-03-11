#!/usr/bin/python

from scapy import *

def sendCovertMsg(msgArray, targetIP, port):
	for msgPart in msgArray:
		msgHex = msgPart.encode("hex")
		pkt = IP(dst=targetIP)/UDP(dport=port, chksum=msgHex)
		send(pkt)

