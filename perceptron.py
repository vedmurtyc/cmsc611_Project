from globalVars import *

WEIGHTS 	    = [[0] * NUM_OF_BRANCHES for _ in range(NUM_OF_BRANCHES)]
BIAS            = [0] * NUM_OF_BRANCHES

def PPredict(x):
    y_cap = [0] * NUM_OF_BRANCHES

    for i in range(NUM_OF_BRANCHES):
        W = WEIGHTS[i]
        B = BIAS[i]

        dot_p = sum([x[i] * W[i] for i in range(len(x))])
        dot_p = dot_p + B * 1
        y_cap[i] = 1 if dot_p > 0 else -1

    return y_cap

def PLearn(x, y):
    for i in range(NUM_OF_BRANCHES):
        W = WEIGHTS[i]
        B = BIAS[i]

        dot_p = sum([x[i] * W[i] for i in range(len(x))])
        dot_p = dot_p + B * 1
        y_cap = 1 if dot_p > 0 else -1

        if (y[i] * y_cap) == -1:
            W = [W[i] + y[i] * x[i] for i in range(len(x))]
            B = B + y[i]
