#!/usr/bin/env python

"""
Answer these questions:
	1) How many times was the word 'fantastic' used in the forums?
	2) Give the list of comma separated nodes the word 'fantastically' can be
		found in (Please list the nodes in ascending order, i.e. 1,2,3,4,5...)

	Input is in the form of:
		node_id, word
"""
import sys

def reducer():
	fantastic_count = 0
	fantastic_nodes = []

	for line in sys.stdin:
		data = line.strip().split('\t')
		if  len(data) != 2:
			continue

		node_id = data[0]
		node_word = data[1]
		if node_word.lower() == 'fantastic':
			fantastic_count += 1

		if node_word.lower() == 'fantastically':
			fantastic_nodes.append(node_id)

	print 'Fantastic was used %s times in the forum.' % fantastic_count
	print 'Fantastically appeared in these nodes:'
	print fantastic_nodes

def main():
	reducer()

if __name__ == '__main__':
	main()