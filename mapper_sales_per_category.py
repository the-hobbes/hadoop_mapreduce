#!/usr/bin/env python

'''
	Provide data to the reducer to solve the following:

	1) Instead of breaking the sales down by store, instead give us a sales 
		breakdown by product category across all of our stores.

	Output to the reducer should be the category and cost of each item pulled
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
		print '{0}\t{1}'.format(category, cost) # output for reducer (tab between)


def main():
	mapper()

if __name__ == '__main__':
	''' 
		This allows you to use the same file both as a library (by importing it) 
		or as the starting point for an application.
		This is because a special variable called __name__ which python will,
		set based on whether the library is imported or run directly by the 
		interpreter.

		If run directly it will be set to __main__. If imported it will be set 
		to the library name. For example, the direct run:
			$ python hello.py
			hello, __main__
		versus the library import:
			from hello import hello
			print hello("world") 
		See:
		http://stackoverflow.com/questions/8228257/what-does-if-name-main-mean-in-python
	'''
	main()