#The purpose of this program is to calculate the commission rate of a transaction
#Get selling price of property from user
#Get percent commission rate from user, convert to decimal
#Calculate commission
#Display commission amount in dollars, format to use commas for thousands, format to 2 decimal places

#Get user input, converts to float
sellingPrice=float(input('Please enter the property selling price. '))

#Get user input, converts to float
percentCommission=float(input('Please enter the percent commission rate. '))

#Converts percent commision to decimal
commissionRate=percentCommission/100

#Selling price multiplied by commission rate equals commission amount
commission= sellingPrice*commissionRate

print('$'+format(commission, ',.2f'))

