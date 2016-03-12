#!/usr/bin/python

import argparse
import sys
import time
from msgHandler import *
from frameHandler import *

def getArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument("-t", "--targetIP")
    parser.add_argument("-p", "--port")
    parser.add_argument("-m", "--msg")
    return parser.parse_args()

def main(args):
    targetIP = args.targetIP
    port = args.port
    msg = args.msg

    if msg != None:
	print ("sending " + targetIP + ":" + port + " -- " + msg)
    	sendCovertMsg(getMsgArray(msg), targetIP, port)
    else:
	print ("waiting for message on port " + port + "...")
	recieveCovertMsg(port)


main(getArgs())

