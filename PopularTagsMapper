#!/usr/bin/python

#Top Tags

#We are interested seeing what are the top tags used in posts.
#Write a mapreduce program that would output Top 10 tags, ordered by the number of questions they appear in.
#For an extra challenge you can think how to get a top 10 list of tags, where they are ordered by some weighted score by your choice.
#To make sure your code is running properly, we have put together a smaller data set and set of expected outputs for you to use to check your work. Please click here to access the instructions to use it.
#Please note that you should only look at tags appearing in questions themselves (i.e. nodes with node_type "question"), not on answers or comments.


import sys
import csv
import re

reader = csv.reader(sys.stdin, delimiter='\t')

for line in reader:
	
	# skip first line (data format line)
	if line[0] == "id":  # ignore first line
		continue
	
	# pull all the tags where node_type is a question
	if line[5] == "question":
		tags = line[2].strip().split()

		# print out tags on separate lines
		for word in tags:
			word = word.lower()
			print "{0}\t{1}".format(word, "1")
        
        
