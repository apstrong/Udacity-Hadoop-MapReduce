#!/usr/bin/python

#Post and Answer Length
#We are interested to see if there is a correlation between the length of a post and the length of answers.

#Write a mapreduce program that would process the forum_node data and output the length of the post and the average answer (just answer, not comment) length for each post. You will have to decide how to write both the mapper and the reducer to get the required result.

#To make sure your code is running properly, we have put together a smaller data set and set of expected outputs for you to use to check your work. Please click here to access the instructions to use it.

# DATA FORMAT
#id	title	tagnames	author_id	body	node_type	parent_id	abs_parent_id	added_at	score	state_string	last_edited_id	last_activity_by_id	last_activity_at	active_revision_id	extra	extra_ref_id	extra_count	marked

# final output
# question node id | question length | average answer length

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')

for line in reader:

	# skip the first line (data format line)	
	if line[0] == "id" or line[5] == "comment":
		continue
	
	# print the ID, node_type, and length of the body
		else:	
		if line[5] == "answer":
			print line[7], "A", "\t", len(line[4])
			#ABS_PARENT_ID	NODE_TYPE	LEN(BODY)
		if line[5] == "question":
			print line[0], "Q", "\t", len(line[4])
			#ID	NODE_TYPE	LEN(BODY)
