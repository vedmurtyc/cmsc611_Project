from sample1 import *
import math


ITER = 80
weights = [[-1]*BRANCH for _ in range(BRANCH)]
GHR = [0]*BRANCH
gradient = [0]*BRANCH

def logreg(x, y, branchNo):
	inp = x[0]
	actual = y
	eta = 0.3
	wx = 0

	for i in range(len(inp)):
		wx += inp[i]*weights[branchNo][i]

	wx = wx * -1
	prediction = 1 / (1 + math.exp(wx))

	prediction = -1 if prediction < 0.5 else 1

	error = actual - prediction

	for i in range(len(inp)):
		gradient[i] += error*inp[i]

	for i in range(len(weights[branchNo])):
		weights[branchNo][i] += eta*gradient[i]
		eta *= 0.99

	for i in range(len(inp)):
		GHR[i] += inp[i]


	# print ("GHR : ", GHR, "Weights : ", weights, "Prediction : ", prediction, "Actual : ", actual)
	# print ("Prediction : ", prediction)
	return (prediction, actual)

scores = [0]*BRANCH
for j in range(ITER):
	x = runCode()
	# branchNo = 0
	for branchNo in range(BRANCH):
		y = x[0][branchNo]
		p, a = logreg(x, y, branchNo)
		if p == a:
			scores[branchNo] += 1


# accuracy = 
print ("Accuracy : ", [(s / float(ITER)) * 100 for s in scores])
