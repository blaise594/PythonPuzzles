#This program reads the grades.txt file
#Create while loop
#Output all of the course names and scores on file (one course per line)
#Display the overall average score calculated and (accurate to two decimal places)

#All logic contained within function
def gradebook_reader():
    #Set accumulator to add up grades
    total=0.0
    #Initialize variable to keep count of grades
    count=0
    #Open 'grades.txt'
    gradebook=open('grades.txt', 'r')

    #Read the first line of the file which is the initial course name
    course=gradebook.readline()
    #If the file is not blank proceed
    if course!='':
        print('Here are your grades')
        #Strip newline from first course
        course=course.rstrip('\n')
    #While course is not blank, keep reading
    while course!='':        
        #Add to count
        count+=1
        #Read the grade
        grade=gradebook.readline()
        #Print course next to ' score is ' ending with grade (stripped of newline)        
        print(course+' score is '+grade.rstrip('\n'))
        #Convert grade to float, add to running total
        total+=float(grade.rstrip('\n'))
        #Read another course
        course=gradebook.readline()
        #Strip newline from course
        course=course.rstrip('\n')    

    #Calculate grade average
    gradeAverage=total/count

    #Close the file    
    gradebook.close()    
    
    print('Average grade score is '+format(gradeAverage, '.2f'))

#Call the function    
gradebook_reader()    
