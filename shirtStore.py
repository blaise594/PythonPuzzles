#This program is a demonstration of if else statements

#Get user to input the quantity of thier order
#Calculate charge for t-shirt(s)
#Determine discount if any
#Mulitply charge by inverse of discount converted to decimal
#Display final t-shirt charge

#Calculate shipping charge
#Display shipping charge

#Add final t-shirt charge to shipping charge for total
#Display total

quantity=int(input('How many shirts would you like? '))

if quantity>=15:
    finalCost=(quantity*9.99)*0.6
    print('Cost of T-shirts: $'+format(finalCost, ',.2f'))
    shipping=quantity*1.05
    print('Cost of shipping: $'+format(shipping, ',.2f'))
    total=finalCost+shipping
    print('Total: $'+format(total, ',.2f'))

elif quantity>=10:
    finalCost=(quantity*9.99)*0.7
    print('Cost of T-shirts: $'+format(finalCost, ',.2f'))
    shipping=quantity*1.05
    print('Cost of shipping: $'+format(shipping, ',.2f'))
    total=finalCost+shipping
    print('Total: $'+format(total, ',.2f'))

elif quantity>=4:
    finalCost=(quantity*9.99)*0.8
    print('Cost of T-shirts: $'+format(finalCost, ',.2f'))
    shipping=quantity*1.05
    print('Cost of shipping: $'+format(shipping, ',.2f'))
    total=finalCost+shipping
    print('Total: $'+format(total, ',.2f'))
   
else:
    finalCost=quantity*9.99
    print('Cost of T-shirts: $'+format(finalCost, ',.2f'))
    shipping=quantity*1.05
    print('Cost of shipping: $'+format(shipping, ',.2f'))
    total=finalCost+shipping
    print('Total: $'+format(total, ',.2f'))
