import math
from sample1 import *

NUM_BRANCHES= 10
weights 	= [[-1]*NUM_BRANCHES for _ in range(NUM_BRANCHES)]
gradient 	= [0]*NUM_BRANCHES

def getGHR(ghr):
	GHR = []
	GHR = ghr
	return GHR

def helperPredict(GHR, branchNo):
	inp = GHR
	wx = 0

	for i in range(len(inp)):
		wx += inp[i]*weights[branchNo][i]

	wx = wx * -1
	prediction = 1 / (1 + math.exp(wx))

	prediction = -1 if prediction < 0.5 else 1

	return prediction

def LRPredict(GHR):
	return [helperPredict(GHR, i) for i in range(NUM_BRANCHES)]

def helperLearn(actual, pred, x, branchNo):
	eta = 0.3
	inp = x[0]
	error = actual - pred

	for i in range(len(inp)):
		gradient[i] += error*inp[i]

	for i in range(len(weights[branchNo])):
		weights[branchNo][i] += eta*gradient[i]
		eta *= 0.99


def LRLearn(x, y):
	predictions = LRPredict(GHR)

	for branchNo in range(NUM_BRANCHES):
		actual = y[branchNo]
		pred = predictions[branchNo]
		helperLearn(actual, pred, x, branchNo)


ghr = [0]*NUM_BRANCHES
GHR = getGHR(ghr)

x = runCode()
y = x[0]
LRLearn(x, y)
print "Weights: ", weights







