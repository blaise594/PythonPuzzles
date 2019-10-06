# a. Ask the player to think about an integer number between 0 and 128.
print('Think about an integer number between 0 and 128')

# b. Set a as the lower end. Set initial value,  a = 0
a=0
#    Set b as the high end. Set initial value, b = 128 
b=128
#    Set t as the time of calculation c. Set initial value, t = 0
t=0
userInput=''
# continue loop as long as number of guesses (t) is less than or equal to 6 and userInput is not equal to yes
while t<=6 and userInput!='yes':
	# d. Calculate the average number between a and b. Set it as M.
	M=(a+b)/2
	# e. Set t = t + 1
	t=t+1
	# f. Ask the player if M is the correct number:
	userInput=raw_input('Is '+str(M)+' the correct number? ')
	# Else
	# If yes, print "The number you thought of is M and I guessed it t tries."
	if userInput=='yes':
		print('The number you thought of is '+str(M)+' and I guessed it in '+str(t)+' tries.')
	# If t=6, print "I am sorry that I cannot guess it after 6 attempts." End the process. 
	elif t>=6:
		print('I am sorry that I cannot guess it after 6 attempts.')
	# Else Ask the player if M is larger than the correct number: 
	elif t<6:
		userHint=raw_input('Is '+str(M)+' larger than the correct number? ')
		# If yes, set a = M, jump to Step d.
		if userHint=='yes':
			a=M
		# Else Set b = M, jump to Step d.
		else:
			b=M
			print(M)

