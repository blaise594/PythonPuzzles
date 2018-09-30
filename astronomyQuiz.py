#This program is a simple quiz game

#Get user to input answer to questions
#Test if user input is correct by comparing strings
#If correct, let them know 
#Else display the correct answer

answer1=input('On average what is the closest planet to Earth? ')

if answer1=='Venus' or answer1=='venus':
    print('You are correct!')
    print('On average, Venus is the closest planet to Earth.')

elif answer1=='Mars' or answer1=='mars':
    print('You are incorrect. On average, Venus is the closest planet to Earth.')
    print('Although,there are times when Mars is actually the closest planet to Earth.')
    
else:
    print('Sorry, you are incorrect.')
    print('On average, Venus is the closest planet to Earth.')

answer2=input('Enter a planet in our solar system to find out how many moons it has. ')

if answer2=='Mercury' or answer2=='mercury' or answer2=='Venus' or answer2=='venus':
    print(answer2+' has 0 moons.')

elif answer2=='Earth' or answer2=='earth':
    print(answer2+' has 1 moon.')

elif answer2=='Mars' or answer2=='mars':
    print(answer2+' has 2 moons.')

elif answer2=='Jupiter' or answer2=='jupiter':
    print(answer2+' has 69 known moons.')

elif answer2=='Saturn' or answer2=='saturn':
    print(answer2+' has 62 known moons.')

elif answer2=='Uranus' or answer2=='uranus':
    print(answer2+' has 27 known moons.')

elif answer2=='Neptune' or answer2=='neptune':
    print(answer2+' has 69 known moons.')
    
else:
    print('That is not a planet in our solar system!')




