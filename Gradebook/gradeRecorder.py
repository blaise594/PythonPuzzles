#Purpose of program is to take course number and grades from user and write to a text file
#Takes input from user
#If user provides input proceed
#Open a file named 'grades.txt'
#Write initial input into file
#Create while loop that takes in course and grade and writes to file
#Once user creates null input by hitting enter, loop exits
#Close file
#Print 'File was created and closed'

#Encapsulate logic within function    
def grade_recorder():
    #Initial user input for course
    course=input('Enter course or Enter to quit ')

    #If user inputs something proceed
    if course!='':    
        #Opens the 'grades.txt' file to be written to; if it doesn't yet exist it will create it
        gradefile=open('grades.txt', 'a')

        #Writes initial course input to file, add new line for readability
        gradefile.write(course+'\n')
    
        #While input is not null, run loop
        while course!='':
            #Gets user to input grade 
            grade=input('Enter percent achieved ')
            #Writes grade input next to course previously entered to file, adds newline for readability
            gradefile.write(grade+'\n')
            #Gets user to input additional course
            course=input('Enter course or Enter to quit ')
            #If user inputs something proceed
            if course!='':
                #Writes additional couse to file, add newline for readability
                gradefile.write(course+'\n')

        #Closes the file
        gradefile.close()

        print('File was created and closed')

#Call function
grade_recorder()
