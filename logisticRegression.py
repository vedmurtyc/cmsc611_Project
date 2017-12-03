import math
from globalVars import *

weights 	= [[0]*NUM_OF_BRANCHES for _ in range(NUM_OF_BRANCHES)]
gradient 	= [0]*NUM_OF_BRANCHES

def getGHR(ghr):
	GHR = []
	GHR = ghr
	return GHR

def sigmoid(val):
	if val < 0:
		return 1 - 1/float(1+math.exp(val))
	val = -1*val
	return 1 /float(1 + math.exp(val))


def helperPredict(GHR, branchNo):
	inp = GHR
	wx = 0

	for i in range(len(inp)):
		wx += inp[i]*weights[branchNo][i]

	# wx = wx * -1
	# prediction = 1 / (1 + math.exp(wx))
	# https://stackoverflow.com/questions/36268077/overflow-math-range-error-for-log-or-exp
	prediction = sigmoid(wx)

	prediction = -1 if prediction < 0.2 else 1

	return prediction

def LRPredict(GHR):
	return [helperPredict(GHR, i) for i in range(NUM_OF_BRANCHES)]

def helperLearn(actual, pred, x, branchNo):
	eta = 0.5
	inp = x
	error = actual - pred

	for i in range(len(inp)):
		gradient[i] += error*inp[i]

	for i in range(len(weights[branchNo])):
		weights[branchNo][i] += eta*gradient[i]
		# eta *= 0.99


def LRLearn(x, y):
	predictions = LRPredict(x)

	for branchNo in range(NUM_OF_BRANCHES):
		actual = y[branchNo]
		pred = predictions[branchNo]
		helperLearn(actual, pred, x, branchNo)
