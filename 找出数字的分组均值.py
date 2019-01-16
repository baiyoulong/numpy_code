import numpy as np

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')
names = ('sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species')


# Solution
# No direct way to implement this. Just a version of a workaround.
numeric_column = iris[:, 1].astype('float')  # sepalwidth
grouping_column = iris[:, 4]  # species

# List comprehension version
[[group_val, numeric_column[grouping_column==group_val].mean()] for group_val in np.unique(grouping_column)]

# For Loop version
output = []
for group_val in np.unique(grouping_column):
    output.append([group_val, numeric_column[grouping_column==group_val].mean()])

print(output)