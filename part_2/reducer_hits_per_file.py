#!/usr/bin/env python

'''
	Answer the following with this reducer:

	1) Write a mapreduce to display thenumber of hits for each different file 
		on the website

	Expected input is:
		filename	timestamp

	Output should look like:
		filename	total(number_of_hits)
'''

import sys

def reducer():
	'''
		Sum the total instances of each filename.
	'''

	hit_total = 0
	old_file = None

	for line in sys.stdin:
		data = line.strip().split('\t')
		if  len(data) != 2:
			continue


		this_file, this_hit = data
		if old_file and old_file != this_file:
			print '{0}\t{1}'.format(old_file, hit_total)

			hit_total = 0

		old_file = this_file
		hit_total += 1

	if old_file != None:
		print old_file, '\t', hit_total

def main():
	reducer()

if __name__ == '__main__':
	'''
		remember, this allows you to use the same file both as a library 
		(by importing it) or as the starting point for an application by calling
		it.

		http://stackoverflow.com/questions/8228257/what-does-if-name-main-mean-in-python
	'''
	main()