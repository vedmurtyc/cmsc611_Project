import numpy as np
# srcCode = "D:/Study/ACA/project/sample1.py"
from sample1 import runCode
import os
import pickle
import logisticRegression as lr

DEBUG     = 0
ITERATION = 5
NUM_OF_BRANCHES = 10

class BranchPredictor(object):
	
	def __init__(self):
		self.GHR          = [0]*NUM_OF_BRANCHES
		self.p_pred       = [0]*NUM_OF_BRANCHES
		self.lr_pred      = [0]*NUM_OF_BRANCHES
		self.lvq_pred     = [0]*NUM_OF_BRANCHES
		self.accuracy     = {"perceptron" : 0, 
		                     "logistic"   : 0,
		                     "LVQ"        : 0
							}

	def perceptron_predict(self):
		self.p_pred = [1]*NUM_OF_BRANCHES # Give call to Perceptron
		pass 

	def perceptron_learn(self):
		pass

	def lr_predict(self):
		self.lr_pred = lr.LRPredict(self.GHR)

	def lr_learn(self, actOutput):
		lr.LRLearn([self.GHR], actOutput)

	def lvq_predict(self):
		pass

	def lvq_learn(self):
		pass

	def updateGHR(self, output):
		for i in range(NUM_OF_BRANCHES):
			self.GHR[i] += output[i]

	def calculateDiff(self, output):
		print("ACTUAL VS EXPECTED ", self.lr_pred, output)
		self.accuracy["perceptron"] += sum(map(lambda x, y : x*y==1, self.p_pred,   output)) / NUM_OF_BRANCHES
		self.accuracy["logistic"]   += sum(map(lambda x, y : x*y==1, self.lr_pred,  output)) / NUM_OF_BRANCHES
		self.accuracy["LVQ"]        += sum(map(lambda x, y : x*y==1, self.lvq_pred, output)) / NUM_OF_BRANCHES

	def calculateAccuracy(self, iterations):
		print("The Accuracies of the models for ",iterations, " iterations are: ")
		print(" Perceptron                   : ", self.accuracy["perceptron"] / iterations)
		print(" Logistic Regression          : ", self.accuracy["logistic"]   / iterations) 
		print(" Learning Vector Quantization : ", self.accuracy["LVQ"]        / iterations)


bp = BranchPredictor()

for _ in range(ITERATION):

	# Get the 3 predictions
	bp.perceptron_predict()
	bp.lr_predict()
	bp.lvq_predict()
	
	# Run the actual Code
	actualOutput = runCode()[0]

	# Send the actual O/P to model for updation
	# bp.perceptron_learn(actualOutput)
	bp.lr_learn(actualOutput)
	# bp.lvq_learn(actualOutput)
	bp.calculateDiff(actualOutput)

	# Update GHR for next iterations
	bp.updateGHR(actualOutput)

bp.calculateAccuracy(ITERATION)

