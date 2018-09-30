#The purpose of this program is to demonstrate the use of an accumulator and while loop
#Get first user input
#Create a variable to count accumulated entries, set to 0
#Create a variable to keep accumulated total of integers, set to zero
#Create while loop with condition that input != 0
#Within while loop add 1 to accumulated entry ticker everytime it loops around
#Within loop add the total to itself + new entry each time it loops around
#Print results of the total/accumulation ticker to determine average

integer=int(input('Enter an integer (press 0 to see average of entered values). '))
accumulator=0
total=0
while integer!=0:
    accumulator+=1    
    total+=integer
    integer=int(input('Enter an integer (press 0 to see average of entered values). '))
print('The average is '+str(total/accumulator))
