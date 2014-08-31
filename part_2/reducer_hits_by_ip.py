#!/usr/bin/env python

'''
	Answer the following with this reducer:

	1) Write a mapreduce which determines the number of hits to the site made b
		each different ip address.

	Expected input is:
		ip_address

	Output should look like:
		ip_address	total(ip_address_instances)
'''

import sys

def reducer():
	'''
		Sum the total appearances of each ip address.
	'''

	hit_total = 0
	old_ip = None

	for line in sys.stdin:
		data = line.strip().split('\n')
		if  len(data) != 1:
			continue


		this_ip = data
		if old_ip and old_ip != this_ip:
			print '{0}\t{1}'.format(old_ip, hit_total)

			hit_total = 0

		old_ip = this_ip
		hit_total += 1

	if old_ip != None:
		print old_ip, '\t', hit_total

def main():
	reducer()

if __name__ == '__main__':
	'''
		remember, this allows you to use the same file both as a library 
		(by importing it) or as the starting point for an application by calling
		it.

		http://stackoverflow.com/questions/8228257/what-does-if-name-main-mean-in-python
	'''
	main()