password = 'lolpass123€'

user_input = input('Enter password: ')

if user_input == password:
	print('PASSWORD OK')
	exit()

if user_input:
	print('WORNG PASSWORD')
	exit()
