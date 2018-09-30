#For use with TempCalc.py

#This module must contain two functions:
#toF converts from Celsius to Fahrenheit
#F=C*9/5+32
#toC converts from Fahrenheit to Celsius
#C=(F-32)*5/9

def toF(C):    
    F=C*9/5+32
    return F
    
def toC(F):
    C=(F-32)*5/9
    return C
