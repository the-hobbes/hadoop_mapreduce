#!/usr/bin/env python

'''
	Answer the following with this reducer:

	1) Instead of breaking the sales down by store, instead give us a sales 
		breakdown by product category across all of our stores.

	Expected input is:
		category	cost

	Output should look like:
		category	sum(cost)
'''

import sys


def reducer():
	# remember, the data comes into the reducer in order, so we can process it
	# as such. 

	sales_total = 0 # running total
	old_key = None # the category, in this case

	for line in sys.stdin: # read from stdin
		data = line.strip().split('\t') # remove whitespace and split on tab
		if len(data) != 2: # something is wrong
			continue

		this_key, this_sale = data
		if old_key and old_key != this_key: # we want to see if the key has changed from the previous one
			print '{0}\t{1}'.format(old_key, sales_total) # if it has, send output 

			sales_total = 0 # reset running total for the next key

		# important aggregation work done here, outside if but inside loop
		# this is what happends when the key hasn't changed from the previous one
		old_key = this_key # set the key to the new row
		sales_total += float(this_sale) # increment the sales total

	# if it is the last line, print the key and total so we don't miss them
	if old_key != None:
		print old_key, "\t", sales_total

def main():
	reducer()

if __name__ == '__main__':
  main()