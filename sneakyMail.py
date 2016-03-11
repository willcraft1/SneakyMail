#!/usr/bin/python

from scapy.all import *
import argparse
import sys
import time

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

main(getArgs())
