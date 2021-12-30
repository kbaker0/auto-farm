import numpy as np


def phTest():
	mu, sigma = 7, 0.5 # mean and standard deviation
	c = np.random.normal(34, sigma, 1)
	s = np.random.normal(mu, sigma, 1)
	h = np.random.normal(67, sigma, 1)
	w = np.random.normal(50, sigma, 1)
	l = np.random.normal(78, sigma, 1)
	print("[")
	counter = 0
	for item in range(100):
		s = np.random.normal(mu, sigma, 1)
		h = np.random.normal(40, sigma, 1)
		l = np.random.normal(50, sigma, 1)
		t = np.random.normal(78, sigma, 1)
		print({'ph':s[0],'humidity':h[0], 'temperature':t[0], 'water_level':l[0], 'conductivity':c[0], 'tstamp':counter})
		print(',')
		counter += 1
	print("]")
phTest()