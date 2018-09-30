#The purpose of this program is to demonstrate use of the modulus operator
#Get numerator from user
#Get denominator from user
#Use integer division, divide numerator by denominator
#Use modulus operation to calculate remainder
#Display the results to show the mixed number in a sentence

numerator=input('Please enter the numerator. ')
denominator=input('Please enter the denominator. ')

#Converts to int
num=int(numerator)
den=int(denominator)


#Calculates whole part of mixed number, converts to string
wholeNum=str(num//den)

#Calculates numerator of mixed number, converts to string
fractionalPt=str(num%den)

print('The mixed number is: '+wholeNum+' and '+fractionalPt+'/'+denominator)
