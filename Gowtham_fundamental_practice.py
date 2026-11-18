#1



name= str(input('Please enter your name :'))
age = int(input('Please enter your age:' ))
height = float(input('Please enter your height:'))
enrolled = bool(input('Are you Currently enrolled'))
subjects = list(input(" Enter the subjects you are currently enrolled  :"))
dob = tuple(input('Please enter you date of birth'))
skill = set(input('Skills you currently possess :'))
course = str(input('Enter your course :'))



print(name)
print(age)
print(height)
print(enrolled)
print(subjects)
print(dob)
print(skill)

student_details = {"Name": name,
                    "Age": age,
                    "Course": course}
                    
                    
                    
                   
print('These are the student details')
print(student_details)
      #These are the student details
      #{'Name': 'Gowtham', 'Age': 22, 'Course': 'PGP'}



#2


subjects = dict

mark1 = float(input('Enter the mark of Python  :' ))
mark2 = float(input('enter the mark of Mathematics  :'))
mark3 = float(input('ENter the mark of Science :'))

subjects = {"Python": mark1, "Mathematics" : mark2 ,"Science": mark3}

total = sum(subjects.values())

print("Total marks are : ",total)


Average_score = total/len(subjects.items())
print(" Average mark of the student :",Average_score)

mark = (mark1, mark2,mark3)  # this is a tuple,thats why these program ran
Highest_mark = max(mark)
lowest_mark = min(mark)

print('The highest mark of the student is :',Highest_mark)
print('The lowest mark of the student is :',lowest_mark)

if(mark1 and mark2 and mark3 > 40):
    print('The student has score more than 40')
else:
    print('No the student didnt even scored 40')



#3

print("90 and above"'\t',"A",'\n','75-89','\t',"B",'\n',"60-74",'\t',"C",'\n',"40-59",'\t',"D","\n","Below40",'\t','Fail')



marks1=(100,100,100)

marks = float(input("Please enter the mark for python"))
marksx = float(input("Please enter the mark for Mathemathics"))
marksz = float(input("Please enter the mark for science"))

if(marks>=90):
    print("A")
elif(marks>=75):
    print("B")
elif(marks>=60):
    print("C")
elif(marks>=40):
    print("D")
elif(marks<=40):
    print("Fail")





if(marksx>=90):
    print("A")
elif(marksx>=75):
    print("B")
elif(marksx>=60):
    print("C")
elif(marksx>=40):
    print("D")
elif(marksx<=40):
    print("Fail")


    
if(marksz>=90):
    print("A")
elif(marksz>=75):
    print("B")
elif(marksz>=60):
    print("C")
elif(marksz>=40):
    print("D")
elif(marksz<=40):
    print("Fail")



average_mark = sum(marks1)/3
print(average_mark)

if(average_mark>=60 and marks>=40 and marksx>=40 and marksz>=40 ):
    print("The student is eligible to receive certificate :")
else:
    print("The student is not eligable to receive certificate")

#90 and above     A 
 #75-89   B 
 #60-74   C 
 #40-59   D 
 #Below40         Fail
#Please enter the mark for python50
#Please enter the mark for Mathemathics50
#Please enter the mark for science50
#D
#D
#D
#100.0
#The student is eligible to receive certificate :



#4

marks_1 = int(input("Please enter the mark received for History :"))
marks_2 = int(input("Please enter the mark received for Maths :"))
marks_3 = int(input("Please enter the mark received for Physics :"))
marks_4 = int(input("Please enter the mark received for Malayalam :"))
marks_5 = int(input("Please enter the mark received for Science :"))

student_bond = [marks_1,marks_2,marks_3,marks_4,marks_5]

for i in range(1):
    print("These are the marks received on the subjects")
    print('*********************************************')
    print(marks_1)
    print(marks_2)
    print(marks_3)
    print(marks_4)
    print(marks_5)



total_marks = sum(student_bond)
print("Total Marks :",total_marks)


count = 0

for i in student_bond:
    if (i >= 40):
        count += 1

print("Number of subjects passed:", count)
        

count = 0
for i in student_bond:
    if(i<=40):
        count += 1
print("number of subjects Failed ",count)

#lease enter the mark received for History :56
#Please enter the mark received for Maths :54
#Please enter the mark received for Physics :85
#Please enter the mark received for Malayalam :20
#Please enter the mark received for Science :10
#These are the marks received on the subjects
#*********************************************
#56
#54
#85
#20
#10
#Total Marks : 225
#Number of subjects passed: 3
#number of subjects Failed  2


#5
num = 1
even_sum = 0
odd_sum = 0

print("All numbers from 1 to 50:")

while (num <= 50):
    print(num)
    
    if (num % 2 == 0):
        print("Even:", num)
        even_sum = even_sum + num
    else:
        print("Odd:", num)
        odd_sum = odd_sum + num

    num = num + 1

print("Sum of even numbers:", even_sum)
print("Sum of odd numbers:", odd_sum)







#6


learn = input("Please enter skills known by you")

set = {"VIDEO editing","finance","Dancing","Gaming"}

set.add(learn)

set.remove("finance")

do = input('IS this student skilled in python  :  Y/N   :')

print(set)

#Please enter skills known by youcommunication
#IS this student skilled in python  :  Y/Nyes
#{'Gaming', 'vIDEO editing', 'communication', 'Dancing'}

#7

student = str(input("please enter your name : "))
age = int(input("Please enter your age :"))
course = str(input("please enter your current course : "))
Total = float(input("pleae enter the total mark received : "))
average = float(input("Please enter the average mark received : " ))
grade = str(input("Please enter the grade you have received : " ))
certificate = str(input("Are you eligible for certiificate : y/n : "))


dictionary = {"Student_name":student,
              "Age":age,
              "Course":course,
              "Total Marks": Total,
              "Average Marks":average,
              "Grade":grade,
              "Certificate Eligibility":certificate}
print("The details of this student id : ")
print(dictionary)



#please enter your name : Gowtham
#Please enter your age :22
#please enter your current course : PGP
#pleae enter the total mark received : 500
#Please enter the average mark received : 450
#Please enter the grade you have received : A
#Are you eligible for certiificate : y/n : yes
#The details of this student id : 
#{'Student_name': 'Gowtham', 'Age': 22, 'Course': 'PGP', 'Total Marks': 500.0, 'Average Marks': 450.0, 'Grade': 'A', 'Certificate Eligibility': 'yes'}




    




