#Purpose of program is to convert temperatures and demonstrate use of custom modules

#Import the tempconvert module.
#Ask user for scale they want to convert from
#Ask user what the temperature they want to convert is
#Perform the appropriate conversion accurate to two decimal places.

import tempconvert

print('Welcome to the temperature converter wizard.')
print('Which scale would you like to convert from today?')
userInput=input('Enter C for Celsius or F for Fahrenheit ')

if userInput=='C' or userInput=='c' or userInput=='Celsius' or userInput=='celsius':
    temp=input('Enter degrees in Celsius. ')
    Fahrenheit=tempconvert.toF(int(temp))
    print('In Fahrenheit, that is '+str(format(Fahrenheit, '.2f')))

elif userInput=='F' or userInput=='f' or userInput=='Fahrenheit' or userInput=='fahrenheit':
    temp=input('Enter degrees in Fahrenheit. ')
    Celsius=tempconvert.toC(int(temp))
    print('In Celsius, that is '+str(format(Celsius, '.2f')))

else:
    print('That is not a valid scale choice. ')


