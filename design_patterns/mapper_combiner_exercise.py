#!/usr/bin/python
"""
Write a mapreduce program that processes the purchases.txt file and outputs
the sum of sales for each weekday (not sat or sun, so not 5 or 6).

output of the mapper will be:
	"day": sales_amount
"""

import sys
from datetime import datetime

def mapper():

	for line in sys.stdin: # read data in from stdin
		data = line.strip().split("\t")
		if len(data) != 6:
			continue
		date = data[0]
		sales = data[4]
		weekday = datetime.strptime(date, "%Y-%m-%d").weekday()
		print '{0}\t{1}'.format(weekday, sales)

def main():
	mapper()
main()