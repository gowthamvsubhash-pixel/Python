# ubjects = dict

# # mark1 = float(input('Enter the mark of Python  :' ))
# # mark2 = float(input('enter the mark of Mathematics  :'))
# # mark3 = float(input('ENter the mark of Science :'))

# subjects = {"Python": mark1, "Mathematics" : mark2 ,"Science": mark3}

# def total_sum():
#     total = sum(subjects.values())

#     print("Total marks are : ",total)
#     return total
# # total_sum()

# def average_mark():
#     Average_score = total_sum()/len(subjects.items())
#     print(" Average mark of the student :",Average_score)
#     return Average_score
# # average_mark()

# def Maximum_and_minimum():
#     mark = (mark1, mark2,mark3)  # this is a tuple,thats why these program ran
#     print("Higest mark is :",max(mark))
#     print("Lowest mark is :",min(mark))


# # Maximum_and_minimum()


# def Eligibility():
#     if(mark1 and mark2 and mark3 > 40):
#         print('The student has score more than 40')
#     else:
#         print('No the student didnt even scored 40')


# Eligibility()


#3

def Score_card():
    print("90 and above"'\t',"A",'\n','75-89','\t',"B",'\n',"60-74",'\t',"C",'\n',"40-59",'\t',"D","\n","Below40",'\t','Fail')



marks1=(100,100,100)

# marks = float(input("Please enter the mark for python"))
# marksx = float(input("Please enter the mark for Mathemathics"))
# marksz = float(input("Please enter the mark for science"))


# def marks_score(): 
#    if(marks>=90):
#         print("A")
#    elif(marks>=75):
#         print("B")
#    elif(marks>=60):
#         print("C")
#    elif(marks>=40):
#         print("D")
#    elif(marks<=40):
#        print("Fail")

#        return marks

# def marks1_score():
#     if(marksx>=90):
#         print("A")
#     elif(marksx>=75):
#         print("B")
#     elif(marksx>=60):
#        print("C")
#     elif(marksx>=40):
#        print("D")
#     elif(marksx<=40):
#        print("Fail")
#        return marksx


# def mark2_score():
#     if(marksz>=90):
#        print("A")
#     elif(marksz>=75):
#        print("B")
#     elif(marksz>=60):
#        print("C")
#     elif(marksz>=40):
#        print("D")
#     elif(marksz<=40):
#        print("Fail")
#        return marksz


# marks_score()
# marks1_score()
# mark2_score()



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

def check_pass():
    count = 0

    for i in student_bond:
      if (i >= 40):
        count += 1
        return i
    print("Number of subjects passed:", count)
        
def check_Fail():
    count = 0
    for i in student_bond:
       if(i<=40):
        count += 1
        return i
    print("number of subjects Failed ",count)


check_pass()
check_Fail()
