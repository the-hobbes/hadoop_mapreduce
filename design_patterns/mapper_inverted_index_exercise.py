#!/usr/bin/python
"""
Write a mapreduce program that creates an index of all words that can be found 
in the body of a forum post and the node id they can be found in. 
Don't parse the HTMl, just split the text on all whitespace as well as the 
following characters: 
	.,!?:;"()<>[]#$=-/

Answer these questions:
	1) How many times was the word 'fantastic' used in the forums?
	2) Give the list of comma separated nodes the word 'fantastically' can be
		found in (Please list the nodes in ascending order, i.e. 1,2,3,4,5...)
"""

import sys
import re

def mapper():
	'''
		We want the output to be node_id, word. 
		So, we work through each line, pull out the node id and the list of
		words that correspond to that node id, 
		and for every word in that list, print node id and the word
	'''
	bodies = []
	old_node = None

	for line in sys.stdin: # read data in from stdin
		# the first line of the input in this dataset are the headings

		data = re.findall(r'[\w]+', line) # \w == [a-zA-Z0-9_]
		if not data:
			continue
			
		this_node = data[0]
		if this_node.isdigit():
			old_node = this_node
			for word in data[1:]:
				print '{0}\t{1}'.format(old_node, word)
		elif old_node: 
			# skip as the first line of the input in this dataset are headings
			for word in data:
				print '{0}\t{1}'.format(old_node, word)

def main():
	mapper()
main()