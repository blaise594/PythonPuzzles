#Purpose of program is to demonstrate the random module
#import random module
#call numbers function in main function
#set accumulator to zero before loop- within numbers function
#make for loop that uses random module to display and add 5 random numbers- within numbers function
#call main function

import random

def main():
    numbers()

def numbers():
    numSum=0    
    for count in range(5):
        randomNums=random.randint(11, 29)
        
        numSum+=randomNums                                
        print(str(randomNums)+' ', end='' )
        
    print('The total is',numSum)                
        
main()
