#!/usr/bin/env python

'''
	Answer the following with this reducer:

	3) Find the total sales value across all the stores, and the total number 
		of sales. Assume there is only one reducer.

	Expected input is:
		time	cost

	Output should look like:
		#rows	total(cost)
'''

import sys


def reducer():
	'''
		For this reducer, we will have two phases (really two reducers
		might be a good idea but the problem statement says use one). 
		1st, we will break down the total sales and number of entries
		for each time slot.
		2nd, we will add all the total sales from all time slots, and
		all time slots together to produce a final output of 
			total number of sales
			total value of sales
	'''

	sales_per_key = []
	rows_of_key = []

	sales_running_total = 0
	rows_running_total = 0
	old_time = None

	for line in sys.stdin:
		data = line.strip().split('\t') # remove whitespace and split on tab
		if len(data) != 2: # something is wrong
			continue

		this_time, this_sale = data

		if old_time and old_time != this_time:
			# we've reached the end of a time block, lets aggregate & reset
			sales_per_key.append(sales_running_total)
			rows_of_key.append(rows_running_total)
			# print '{0}\t{1}'.format(sales_running_total, rows_running_total)

			sales_running_total = 0
			rows_running_total = 0

		# add to running totals and update time
		old_time = this_time
		sales_running_total += float(this_sale)
		rows_running_total += 1

	# handle last line
	if old_time != None:
		sales_per_key.append(sales_running_total)
		rows_of_key.append(rows_running_total)
		# print '{0}\t{1}'.format(sales_running_total, rows_running_total)

	# finish by summing the totals
	print '{0}\t{1}'.format(sum(sales_per_key), sum(rows_of_key))

def main():
	reducer()

if __name__ == '__main__':
  main()