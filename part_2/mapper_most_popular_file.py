#!/usr/bin/env python

'''
	Provide data to the reducer to solve the following:
	
	3) Write a mapreduce to display most popular file on the website.
			
	Output to the reducer should be the filename and time, to identify each hit.
'''

import sys


def mapper():
	for line in sys.stdin: # read data in from stdin
		data = line.strip().split(' ')
		data = [item.strip('"').strip('[|]') for item in data]

		if len(data) != 10:
			continue
		
		ip, \
		client_id, \
		username, \
		time, \
		time_zone, \
		method, \
		file_name, \
		protocol, \
		response_code, \
		object_size = data

		# get rid of the http or https if there is one
		file_name = file_name.strip('http(s)://')
		print '{0}\t{1}'.format(file_name, time)


def main():
	mapper()
main()