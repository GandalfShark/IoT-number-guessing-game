
# number guessing game for IoT class
low = 0
high = 1024
test = True
number_entered = -1
print('*** number guessing game *** \n')
number_entered = int(input('enter a number between 0 and 1024:'))
guess_range = [_ for _ in range(0, 1025)]
# for each _ set a value counting from 0 to 1024
# create a list of these values as guess_range
# this also prevents entering of floats as the numbers are all ints
# print(guess_range)

while number_entered not in guess_range:
	try:
		number_entered = int(input('Please enter a number between 0 and 1024!'))
	except ValueError:
		continue
# make sure the number is in the given range, do not exit loop until it is

if number_entered == 0:
	print('Your number is 0.')
# first guess is zero

else:
	if number_entered == 1024:
		print('Your number is 1024.')
		# 2nd guess is 1024
		test = False
	while test:
		guess = int((low + high)/2)
		if guess == number_entered:
			print(f'Your number is {guess}.')
			test = False
		if guess < number_entered:
			low = guess
		else:
			high = guess

