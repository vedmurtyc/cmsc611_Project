import random
from globalVars import *

def branches(i):
	arr = [-1]*NUM_OF_BRANCHES
	
	if (i%3) == 0:
		i += 1
		arr[0] = 1

		if (i%4) == 1:
			i *= 2
			arr[1] = 1

	if (i * 3 == 2):
		i = 1
		arr[2] = 1

	if (i//2 == 0):
		i *= 4
		arr[3] = 1

		if (i* 3 == 15):
			i = 2
			arr[4] = 1

	if ((i+4)%2 == 1):
		i = i + 3
		arr[5] = 1
	
	return arr

def runCode():
	allPredictions = []
	for _ in range(ITERATION):
		iVal = random.randint(0,100)
		allPredictions.append(branches(iVal))
	return allPredictions