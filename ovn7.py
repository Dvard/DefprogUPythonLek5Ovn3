from tabulate import tabulate


def c_to_f(c):
	return str((9 / 5) * c + 32) + ' F'


results = []

for i in range(40, -41, -1):
	results.append([str(i) + '°C', c_to_f(i)])

print(tabulate(results, headers=['°C', 'F']))
