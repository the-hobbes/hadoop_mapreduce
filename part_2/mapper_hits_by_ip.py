#!/usr/bin/env python

'''
	Provide data to the reducer to solve the following:
	
	1) Write a mapreduce which determines the number of hits to the site made b
		each different ip address.
			
	Output to the reducer should be the just the ip address.
'''

import sys


def mapper():
	for line in sys.stdin: # read data in from stdin
		data = line.strip().split(' ')

		if len(data) != 10:
			continue
		
		ip = data[0]

		print ip


def main():
	mapper()
main()