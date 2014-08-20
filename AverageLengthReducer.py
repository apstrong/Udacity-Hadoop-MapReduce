#!/usr/bin/python

# final output
# question node id | question length | average answer length

import sys

# initialize variables
oldID = None
oldType = None
avgAnsLength = 0
ansCount = 0
bodyLenTotal = 0
questionLength = 0

# map out data
for line in sys.stdin:
	thisType = line.split(' ')[1]
	thisID = line.split(' ')[0]
	bodyLength = int(line.split("\t")[1])
	
	# switch between IDs. print the oldID and question/answer length, then re-initialize variables for the next ID 
	if oldID and oldID != thisID:
		print oldID, "\t", questionLength, "\t", avgAnsLength
		oldID = thisID
		oldType = thisType		
		ansCount = 0
		bodyLenTotal = 0
		avgAnsLength = 0
		questionLength = 0
	
	oldID = thisID
	oldType = thisType
	
	# if the post type is an 'answer,' increment the count of answers for this ID, and calculate avg answer length
	if oldType == "A":
		ansCount += 1
		bodyLenTotal += bodyLength
		avgAnsLength = float(bodyLenTotal / ansCount)
	# if the post type is a 'question,' set the bodyLength = questionLength
	if oldType == "Q":
		questionLength = bodyLength

# print last set of values
if oldID != None:
	print oldID, "\t", questionLength, "\t", avgAnsLength
