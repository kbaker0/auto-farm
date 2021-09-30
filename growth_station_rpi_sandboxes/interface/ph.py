import numpy as np


def phTest():
	mu, sigma = 7, 0.5 # mean and standard deviation
	s = np.random.normal(mu, sigma, 1000)
	print("[")
	counter = 0
	for item in s:
		# print({'ph':item,'tstamp':counter})
		# print(',')
		counter += 1
	# print("]")