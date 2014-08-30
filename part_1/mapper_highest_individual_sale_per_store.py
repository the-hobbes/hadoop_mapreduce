#!/usr/bin/env python

'''
	Provide data to the reducer to solve the following:
	
	2) Find the monetary value for the highest individual sale for each separate
	 store

	Output to the reducer should be the store and cost of each item pulled
	from every line of the input.
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
		print '{0}\t{1}'.format(store, cost) # output for reducer (tab between)


def main():
	mapper()
main()