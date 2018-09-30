#Get user to input integer
#Test if integer is divisable by 2 without a remainder using modulus
#If remainder is zero integer is even
#Else integer is odd

integer=int(input('Please enter an integer. '))

remainder=integer%2

if remainder==0:
    print('The number is even.')

else:
    print('The number is odd.') 
