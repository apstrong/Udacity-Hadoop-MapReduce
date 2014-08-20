#!/usr/bin/python

# output
# question ID | student IDs

import sys

# initialize variables
oldQuestionID = None
oldStudentID = None
studentList = []

for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	if len(data_mapped) !=2:
	# Something has gone wrong. Skip this line.
		continue
	
	# map out data
	thisQuestionID, thisStudentID = data_mapped
	
	# switch between IDs- print oldID and student list, reset variables
	if oldQuestionID and oldQuestionID != thisQuestionID:
		print oldQuestionID, studentList
		studentList = []
	
	oldQuestionID = thisQuestionID
	
	# add studentID to list of studentIDs 
	studentList.append((thisStudentID))
	
# print last set of values	
if oldQuestionID != None:
	print oldQuestionID, studentList
