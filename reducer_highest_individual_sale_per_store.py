#!/usr/bin/env python

'''
	Answer the following with this reducer:

	2) Find the monetary value for the highest individual sale for each separate
	 store

	Expected input is:
		store	cost

	Output should look like:
		store	max(cost)
'''

import sys


def reducer():
	# remember, the data comes into the reducer in order, so we can process it
	# as such. 

	highest_sale_so_far = None
	old_store = None

	for line in sys.stdin:
		data = line.strip().split('\t') # remove whitespace and split on tab
		if len(data) != 2: # something is wrong
			continue

		this_store, this_sale = data
		if old_store and old_store != this_store:
			# print the result of the highest sale in the previous store
			print '{0}\t{1}'.format(old_store, highest_sale_so_far)
			# then begin work on the highest total for this_store
			highest_sale_so_far = float(this_sale)

		# otherwise the store is the same, so we see which sale is higher
		old_store = this_store
		highest_sale_so_far = max(float(this_sale), highest_sale_so_far)

	# if it is the last line, print the store and max so we don't miss them
	if old_store != None:
		print '{0}\t{1}'.format(old_store, highest_sale_so_far)

def main():
	reducer()

if __name__ == '__main__':
  main()