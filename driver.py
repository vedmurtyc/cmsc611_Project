import numpy as np
# import matplotlib.pyplot as plt
from sklearn import linear_model

# srcCode = "D:/Study/ACA/project/sample1.py"
from sample1 import runCode
import os
import pickle

DEBUG = 0
BRANCHES = 10
selectedBranch = 0

def logisticRegression(x, y):
	modelFile = "lr_model.sav"
	
	if (not os.path.isfile(modelFile)):
		lr = linear_model.LogisticRegression()
		prediction = [-1]*BRANCHES
	else:
		lr = pickle.load(open(modelFile, 'rb'))
		prediction = lr.predict(x)
	
	print("Current GHR : ", x, " Predicted Value :", prediction, " Actual Value : ", y)

	lr.fit(x, y)
	pickle.dump(lr, open(modelFile, 'wb'))


GHR = [0] * BRANCHES

for _ in range(10):
	# Actual Output (All branches)
	x = runCode()
	# Actual Output (Selected branch)
	y = [x[0][selectedBranch]]

	# TODO Send current GHR to predictor to get the prediction for this branch.
	logisticRegression(GHR, y)

	# Update the GHR with actual outcome
	GHR = [GHR[i] + x[0][i] for i in range(BRANCHES)]



# createInputData()

def createInputData():
	x = runCode()
	branchNo = 0
	y = [b[branchNo] for b in x]

	if(DEBUG):
		print(x, y)

	logisticRegression(x, y)
