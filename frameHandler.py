#!/usr/bin/python

from scapy.all import *
import binascii

def sendCovertMsg(msgArray, targetIP, port):
	os.system("ethtool --offload eno1 rx off tx off")
	for msgPart in msgArray:		
		#msgPart.encode("hex")		
		#msgHex = hex(ord(msgPart))
		msgHex = binascii.hexlify(msgPart)
		msg = "0x"+msgHex		
		#print msgHex
		pkt=IP(dst=targetIP)/UDP(dport=port, chksum=msg)
		send(pkt)

