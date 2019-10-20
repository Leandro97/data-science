import numpy as np 
import random as random
import matplotlib.pyplot as plt
from scipy.stats import norm, pareto, kstest

def showHistogram(v1, v2):
	fig, axs = plt.subplots(1, 2, sharey = True, tight_layout = True)

	axs[0].hist(v1, bins = 100, density = True)
	axs[0].set_title("V1")
	axs[1].hist(v2, bins = 100, density = True)
	axs[1].set_title("V2")

	plt.show()

def testNormality(sampleForTesting):
	test = kstest(sampleForTesting, "norm") # null hypothesis: sampleForTesting is normally distributed 

	if test.pvalue < 0.05: #null hypothesis rejected
		return "is not normal"
	else:				   #failed to reject null hypothesis
		return "is normal"


def main():		
	#a lot of elements with small values, making median smaller than mean
	v1a = np.random.normal(500, 5, 2000)
	v1b = np.random.normal(50, 5, 8000) 
	v1  = np.concatenate((v1a, v1b), axis = 0)

	#a lot of elements with large values, making median bigger than mean
	v2a = np.random.normal(50, 5, 2000)
	v2b = np.random.normal(500, 5, 8000)
	v2  = np.concatenate((v2a, v2b), axis = 0)

	showHistogram(v1, v2)
	print("V1 {}".format(testNormality(v1)))
	print("V2 {}".format(testNormality(v2)))

main()