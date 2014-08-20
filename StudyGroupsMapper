#!/usr/bin/python

#Study Groups
#We might want to help students form study groups. But first we want to see if there are already students on forums that communicate a lot between themselves.
#As the first step for this analysis we have been tasked with writing a mapreduce program that for each forum thread (that is a question node with all it's answers and comments) would give us a list of students that have posted there - either asked the question, answered a question or added a comment. If a student posted to that thread several times, they should be added to that list several times as well, to indicate intensity of communication.
#To make sure your code is running properly, we have put together a smaller data set and set of expected outputs for you to use to check your work. Please click here to access the instructions to use it.


# DATA FORMAT
#id	title	tagnames	author_id	body	node_type	parent_id	abs_parent_id	added_at	score	state_string	last_edited_id	last_activity_by_id	last_activity_at	active_revision_id	extra	extra_ref_id	extra_count	marked

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')

for line in reader:
	
	# skip first line (data format line)
	if line[0] == "id":
		continue

	# print post ID and author ID for questions, answers, and comments
	else:	
		if line[5] == "answer" or line[5] == "comment":
			print line[7],"\t", line[3]
			#ABS_PARENT_ID	author_id
		if line[5] == "question":
			print line[0], "\t", line[3]
			#ID	author_id
