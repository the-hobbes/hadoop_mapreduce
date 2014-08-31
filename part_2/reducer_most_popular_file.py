#!/usr/bin/env python

'''
	Answer the following with this reducer:

	3) Write a mapreduce to display most popular file on the website.

	Expected input is:
		filename	time

	Output should look like:
		most_popular_file	number_of_occurences
'''

import sys


def reducer():
	'''
		Calculate the total hits for a file.
		Compare it to the total hits for the previous file.
		Keep the highest one.
		Repeat until all files are examined. 
	'''

	current_most_popular_file = None
	current_most_hits = 0

	old_file = None
	hits_running_total = 0

	for line in sys.stdin:
		data = line.split('\t')
		if len(data) != 2:
			continue

		this_file, this_time = data
		if old_file and old_file != this_file:
			# check to see what is the highest
			if hits_running_total > current_most_hits:
				current_most_popular_file = old_file
				current_most_hits = hits_running_total

			hits_running_total = 0

		old_file = this_file
		hits_running_total += 1

	if old_file != None:
		print '{0}\t{1}'.format(current_most_popular_file, current_most_hits)


def main():
	reducer()

if __name__ == '__main__':
  main()