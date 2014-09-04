#!/usr/bin/env python

"""
Answer this question:
	1) what is the mean value of sales on sunday?

	Input is in the form of:
		day, sales
"""
import sys

def reducer():
	sales_total = 0
	total_sundays = 0
	sunday = '6'

	for line in sys.stdin:
		data = line.strip().split('\t')
		if  len(data) != 2:
			continue
		
		this_day, this_sale = data
		if this_day != sunday: # only matters if it is sunday
			continue

		sales_total += float(this_sale)
		total_sundays += 1
		
	mean_value = sales_total / total_sundays
	print mean_value
	
def main():
	reducer()

if __name__ == '__main__':
	main()