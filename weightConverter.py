#The purpose of this program is to convert weight in pounds to weight in kilos
#Get user input
#Convert pounds to kilograms
#Display result in kilograms rounded to one decimal place

#Get user weight in pounds
weightInPounds=float(input('Enter your weight in pounds. '))

#One pound equals 2.2046226218 kilograms
weightInKilos=weightInPounds/2.2046226218

print('Your weight in kilograms is: '+format(weightInKilos, '.1f'))
