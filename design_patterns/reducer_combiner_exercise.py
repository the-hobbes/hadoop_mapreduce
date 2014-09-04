#!/usr/bin/env python

"""
Answer this question:
	1) what is the sum of sales on each day?

	Input is in the form of:
		day, sales
"""
import sys

def reducer():
	sales_total = 0
	old_day = None


	for line in sys.stdin:
		data = line.strip().split('\t')
		if  len(data) != 2:
			continue
		
		this_day, this_sale = data
		if old_day and old_day != this_day:
			print '{0}\t{1}'.format(old_day, sales_total)
			sales_total = 0

		old_day = this_day
		sales_total += float(this_sale)

	if old_day:
		print '{0}\t{1}'.format(old_day, sales_total)
	
def main():
	reducer()

if __name__ == '__main__':
	main()