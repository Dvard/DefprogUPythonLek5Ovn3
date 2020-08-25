from tabulate import tabulate


def c_to_f(c):
	return str((9 / 5) * c + 32) + ' F'


results = []

i = 41

while i > -41:
	i -= 1
	results.append([str(i) + '°C', c_to_f(i)])


print(tabulate(results, headers=['°C', 'F']))
