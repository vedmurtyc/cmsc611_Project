import random
from globalVars import *

def branches(i):
	arr = [-1]*NUM_OF_BRANCHES
	
	if (i*4) == 100:
		i = i ** 2
		arr[0] = 1

		if (i%3) == 1:
			i += 1
			arr[1] = 1

			if (i%6) == 1:
				i *= 2
				arr[2] = 1

				if (i+3*2) // 4 == 36:
					i = i*4
					arr[3] = 1

					if (i * 2 == 26):
						i = 1
						arr[4] = 1


						if (i//2 == 0):
							i *= 4
							arr[5] = 1

							if (i* 4 == 16):
								i = 2
								arr[6] = 1


								if (i+16-12) == 67:
									i += 4
									arr[7] = 1

									if ((i-1)%10 != 0):
										i -= 1
										arr[8] = 1

										if ((i+3)%2 == 1):
											i = i + 3
											arr[9] = 1
		
	return arr

def runCode():
	allPredictions = []
	for _ in range(ITERATION):
		iVal = random.randint(25,100)
		allPredictions.append(branches(iVal))
	return allPredictions