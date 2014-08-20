#!/usr/bin/python

import sys

# initialize variables
oldID = ""
userHourCounts = [0] * 24 	#set an array with length of 24, initialized to 0. [(0,2),(1,1)...etc] hour, count

for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	if len(data_mapped) !=2:
	# Something has gone wrong. Skip this line.
		continue
	
	# map out data
	thisID, thisHour = data_mapped

	# switch between IDs- print hour with max counts for old ID, reset variables
	if oldID and oldID != thisID:
		maxHourCount = max(userHourCounts)
		for i,j in enumerate(userHourCounts): 
			if j == maxHourCount:
				print oldID, "\t", i
		userHourCounts = [0] * 24
		
	userHourCounts[int(thisHour)] += 1
	oldID = thisID
	
	
# last line
if oldID != "":
	maxHourCount = max(userHourCounts)
	for i,j in enumerate(userHourCounts):
		if j == maxHourCount :
			print oldID, "\t", i
