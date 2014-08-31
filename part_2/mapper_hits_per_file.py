#!/usr/bin/env python

'''
	Provide data to the reducer to solve the following:
	
	1) Write a mapreduce to display thenumber of hits for each different file 
		on the website

	Input format:
		10.223.157.186 - - [15/Jul/2009:15:50:35 -0700] "GET /assets/js/lowpro.js HTTP/1.1" 200 10469
		%h is the IP address of the client
		%l is identity of the client, or "-" if it's unavailable
		%u is username of the client, or "-" if it's unavailable
		%t is the time that the server finished processing the request. The format is [day/month/year:hour:minute:second zone]
		%r is the request line from the client is given (in double quotes). It contains the method, path, query-string, and protocol or the request.
		%>s is the status code that the server sends back to the client. You will see see mostly status codes 200 (OK - The request has succeeded), 304 (Not Modified) and 404 (Not Found). See more information on status codes in W3C.org
		%b is the size of the object returned to the client, in bytes. It will be "-" in case of status code 304.
			
	Output to the reducer should be the file and time, to identify each hit.
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

		print '{0}\t{1}'.format(file_name, time)


def main():
	mapper()
main()