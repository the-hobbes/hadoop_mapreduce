#!/usr/bin/env python

'''
	Provide data to the reducer to solve the following:
	
	3) Find the total sales value across all the stores, and the total number 
		of sales. Assume there is only one reducer.

	Output to the reducer should be the time and cost of each item pulled
	from every line of the input. The key doesn't matter so much in this case.
	as the number of sales and the total cost is what matters. The time will
	do just fine in this case.
'''

import sys


def mapper():
	'''
		data is in format:
			date, time, city, item, price, payment method
	'''
	for line in sys.stdin: # read data in from stdin
		data = line.strip().split("\t")
		
		if len(data) != 6:
			continue

		date, time, store, category, cost, payment = data
		print '{0}\t{1}'.format(time, cost) # output for reducer (tab between)


def main():
	mapper()
main()