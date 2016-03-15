#!/usr/bin/python

import re

def getMsgArray(msg):
	msgArray = re.findall('.', msg)
	return msgArray
