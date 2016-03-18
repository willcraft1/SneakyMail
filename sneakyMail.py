#!/usr/bin/python

import argparse
import sys
import time
from msgHandler import *
from frameHandler import *

def getArgs():
    parser = argparse.ArgumentParser(prog="SneakyMail")
    parser.add_argument("-p", "--port", default="80", type=str, help="sending and receiving, the port to use, must match")
    parser.add_argument("-t", "--targetIP", help="if sending, input the target's IP")
    parser.add_argument("-m", "--msg", help="if sending, the message you want to send")
    parser.add_argument("-d", "--delay", type=float, default=0, help="if sending, the delay in seconds between packets sent")
    return parser.parse_args()

def main(args):
    targetIP = args.targetIP
    port = args.port
    msg = args.msg
    delay = args.delay

    if (
          targetIP == None and \
          msg      == None and \
          delay    == 0    
       ):
		print ("Waiting for convert message on port " +port+"...")
		recieveCovertMsg(port)
		print ("End Of Message code received.")
    if (
          targetIP != None and \
          msg      != None 
       ):
		msgArray = getMsgArray(msg)
		timeToSend = len(msgArray) * delay
		print ("Transmitting the text:\n\""+msg+"\"\nto "+targetIP+":"+port+" with a "+str(delay)+" second delay between packet transmissions.\nThe estimated time to completion is "+str(timeToSend)+" seconds.")
		sendCovertMsg(msgArray, targetIP, port, delay)
		print ("Message transmission complete.")
    else:
		print ("To transmit, include: -t targetIP -m message -p port.\nTo receive, only include -p port.")

#main thread execution with arguments from the command line
main(getArgs())

