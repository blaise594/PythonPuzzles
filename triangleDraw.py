#Draws a pattern with zeros based on user input
#Get number of rows from user
#Use for loop to iterate number of rows indicated by user
#Nest another for loop within first for loop
#In nested loop use modulus to find the remainder of the rows (r) and the base size
#Use this value to calculate number of spaces needed in column
#Use last statement to calculate and print zeros needed to draw pattern

baseSize=int(input('How many lines would you like your triangle to be? '))

for r in range(baseSize):
    for c in range(r%baseSize):
        print(' ', end='')
    print((baseSize-r)*'0')
