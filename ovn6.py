from tabulate import tabulate
from math import pow

result = []

for i in range(0, 21):
	result.append([i, pow(i, 2), pow(i, 3)])

print(tabulate(result, headers=['i', 'i^2', 'i^3']))
