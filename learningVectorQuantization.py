from random import randint
from globalVars import *

REF_VECTORS = 2
ETA        = 0.5

weights = [ [ [-1]*HISTORY, [1]*HISTORY ] for _ in range(NUM_OF_BRANCHES) ] 

def euclideanSqrDist(v1, v2):
	return sum([(x-y)**2 for x,y in zip(v1,v2)])

def closestVector(branch, i):
	return (1 , -1)[euclideanSqrDist(branch, weights[i][0]) < euclideanSqrDist(branch, weights[i][1])]

def LVQPredict(bHist):
	predictions = [0]*NUM_OF_BRANCHES
	
	for i,branch in enumerate(bHist):
		predictions[i] = closestVector(branch, i)
	
	if(LVQ_DEBUG):
		print(predictions)
	return predictions

def LVQLearn( bHist, actualOutput ):
	
	if(LVQ_DEBUG):
		print(weights)
	for i,branch in enumerate(bHist):
		pred = closestVector(branch, i)
		
		if(actualOutput[i] == pred):
			pred = 0 if (pred == -1) else 1
			etaDiff = [ETA*(x-y) for x,y in zip(branch, weights[i][pred])]

			weights[i][pred] = [x+y for x,y in zip(weights[i][pred],etaDiff)]
		else:
			pred = 0 if (pred == -1) else 1
			etaDiff = [ETA*(x-y) for x,y in zip(branch, weights[i][pred])]

			weights[i][pred] = [x-y for x,y in zip(weights[i][pred],etaDiff)]

