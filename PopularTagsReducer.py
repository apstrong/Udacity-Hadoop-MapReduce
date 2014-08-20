#!/usr/bin/python

import sys
import csv
import re

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t')

# initialize variables
oldWord = None
wordCount = 0
myList = []
  
for line in reader:
	
	# map out data
	thisWord = line[0]
	thisCount = line[1]
	
	# switch between words
	if oldWord and oldWord != thisWord:
		
		# if the length of the list is less than 10, add the next word and sort by the count (second value)
		if len(myList) < 10:
			myList.append((oldWord, wordCount))
			myList.sort(key=lambda x: x[1])
		
		# if the count of the next word is larger than the smallest on the list, remove that word and add the new one
		else:
			if wordCount > myList[0][1]:
				myList.pop(0)
				myList.append((oldWord, wordCount))
				myList.sort(key=lambda x: x[1])	
		wordCount = 0	


	oldWord = thisWord
	wordCount += 1

# handles last set of values, reverse order of list to get words with highest counts on top
if oldWord != None:
	if len(myList) < 10:
		myList.append((oldWord, wordCount))
		myList.sort(key=lambda x: x[1])
		myList.reverse()
		
	else:
		if wordCount > myList[0][1]:
			myList.pop(0)
			myList.append((oldWord, wordCount))
			myList.sort(key=lambda x: x[1])	
			myList.reverse()

# print list
for item in myList:
	writer.writerow(item)
