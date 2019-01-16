import numpy as np

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
species = np.genfromtxt(url, delimiter=',', dtype='str', usecols=4)
np.random.seed(100)
species_small = np.sort(np.random.choice(species, size=20))

output = [np.argwhere(np.unique(species_small) == s).tolist()[0][0] for val in np.unique(species_small) for s in species_small[species_small==val]]

# Solution: For Loop version
output = []
uniqs = np.unique(species_small)

for val in uniqs:  # uniq values in group
    for s in species_small[species_small==val]:  # each element in group
        groupid = np.argwhere(uniqs == s).tolist()[0][0]  # groupid
        output.append(groupid)

print(output)