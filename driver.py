import os
import pickle
import numpy as np
import logisticRegression as lr
import perceptron as pt
import learningVectorQuantization as lvq
from globalVars import *
from collections import deque


class BranchPredictor(object):
	
	def __init__(self):
		self.GHR          = [0]*NUM_OF_BRANCHES
		self.GHR_HISTORY  = [deque([-1]*HISTORY) for _ in range(NUM_OF_BRANCHES)]
		self.p_pred       = [0]*NUM_OF_BRANCHES
		self.lr_pred      = [0]*NUM_OF_BRANCHES
		self.lvq_pred     = [0]*NUM_OF_BRANCHES
		self.accuracy     = {"perceptron" : 0, 
		                     "logistic"   : 0,
		                     "LVQ"        : 0
							}

	def perceptron_predict(self):
		self.p_pred = pt.PPredict(self.GHR)

	def perceptron_learn(self, actualOutput):
		pt.PLearn(self.GHR, actualOutput)

	def lr_predict(self):
		self.lr_pred = lr.LRPredict(self.GHR)

	def lr_learn(self, actOutput):
		lr.LRLearn(self.GHR, actOutput)

	def lvq_predict(self):
		self.lvq_pred = lvq.LVQPredict(self.GHR_HISTORY)

	def lvq_learn(self, actualOutput):
		lvq.LVQLearn(self.GHR_HISTORY, actualOutput)

	def updateGHR(self, output):
		for i in range(NUM_OF_BRANCHES):
			self.GHR[i] += output[i]
			self.GHR_HISTORY[i].append(output[i])
			self.GHR_HISTORY[i].popleft()
		if(DEBUG):
			print(self.GHR_HISTORY[0])

	def calculateDiff(self, output):
		if(DEBUG):
			print("ACTUAL ",   self.p_pred)
			print("EXPECTED ", output     )
		self.accuracy["perceptron"] += sum(map(lambda x, y : x*y==1, self.p_pred,   output)) / NUM_OF_BRANCHES
		self.accuracy["logistic"]   += sum(map(lambda x, y : x*y==1, self.lr_pred,  output)) / NUM_OF_BRANCHES
		self.accuracy["LVQ"]        += sum(map(lambda x, y : x*y==1, self.lvq_pred, output)) / NUM_OF_BRANCHES

	def calculateAccuracy(self, iterations):
		print("The Accuracies of the models for ",iterations, " iterations are: ")
		print(" Perceptron                   : ", self.accuracy["perceptron"] / iterations)
		print(" Logistic Regression          : ", self.accuracy["logistic"]   / iterations) 
		print(" Learning Vector Quantization : ", self.accuracy["LVQ"]        / iterations)
		# print (self.accuracy)

bp = BranchPredictor()

for s in range(NUM_OF_SAMPLES):
	sampleName = "sample" + str(s+1)
	module = __import__(sampleName)

	for _ in range(ITERATION):

		# Get the 3 predictions
		bp.perceptron_predict()
		bp.lr_predict()
		bp.lvq_predict()
		
		# Run the actual Code
		actualOutput = module.runCode()[0]
		
		# Send the actual O/P to model for updation
		bp.perceptron_learn(actualOutput)
		bp.lr_learn(actualOutput)
		bp.lvq_learn(actualOutput)
		bp.calculateDiff(actualOutput)

		# Update GHR for next iterations
		bp.updateGHR(actualOutput)

bp.calculateAccuracy(ITERATION*NUM_OF_SAMPLES)
