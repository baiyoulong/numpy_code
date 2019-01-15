import numpy as np

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')
sepallength = np.genfromtxt(url, delimiter=',', dtype='float', usecols=[0])

mu = np.mean(sepallength)
med = np.median(sepallength)
sd = np.std(sepallength)

print(mu, med, sd)