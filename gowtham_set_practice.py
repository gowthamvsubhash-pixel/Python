
# #1

fruits = {'Apple', 'Banana', 'Orange', 'Mango', 'Grapes'}
print('These are the fruits and the number of fruits :',fruits,'No.offruits',fruits.__len__())
        #These are the fruits and the number of fruits : {'Banana', 'Grapes', 'Apple', 'Mango', 'Orange'} No.offruits 5


#  #2


numbers = [10, 20, 10, 30, 20, 40, 50, 30]

print(set(numbers))
          # {40, 10, 50, 20, 30}


# #3

colors = {"red", "blue", "green"}

colors.add("yellow")
colors.add("black")
colors.remove("blue" )

print(colors)
         #{'green', 'yellow', 'black', 'red'}


# #4


student1 = {"Python", "Java", "SQL", "HTML"}
student2 = {"Python", "C++", "SQL", "CSS"}

print(student1.intersection(student2))
#{'SQL', 'Python'}


# #5

student1 = {"Python", "Java", "SQL", "HTML"}
student2 = {"Python", "C++", "SQL", "CSS"}

print(student1.union(student2))
#{'CSS', 'C++', 'HTML', 'SQL', 'Java', 'Python'}

print(student1.difference(student2))
#{'Java', 'HTML'}

print(student2.difference(student1))
#{'C++', 'CSS'}


#6


student = {'name': 'Rahul',
           'age' : '20',
           'course' : 'Python',
           'city': 'Kochi'}


print(student)
#{'name': 'Rahul', 'age': '20', 'course': 'Python', 'city': 'Kochi'}

print(student['name'])
#Rahul

print(student['age'])
#20

print(student['course'])
#Python



#7


employee = { "name": "Anu", "age": 25, "salary": 25000}

employee['Department'] = "IT"

employee['salary']= 300000
employee['age']= 26

print(employee)
{'name': 'Anu', 'age': 26, 'salary': 300000, 'Department': 'IT'}


#8


marks = { "Maths": 80, "Science": 75, "English": 90,
"Computer": 85}

print(marks.keys())
#dict_keys(['Maths', 'Science', 'English', 'Computer'])

print(marks.values())
#dict_values([80, 75, 90, 85])

total = sum(marks.values())
print(total)
#330
average_mark = sum(marks.values())/len(marks.values()) # if we need to take an average while using dictionary try doing this.
print(average_mark)
82.5

#9


student = {"name": "Arun", "age": 21, "course": "Python",
"marks": 85}

print(student["name"],' :  Currently studining   :',student["course"])
#Arun  :  Currently studining   : Python

if(student['marks']>=50):
    print('Pass')
else:
    print('Fail')
#Pass

student["grade"] = "A"

for i in range(5):
    print(student)

#{'name': 'Arun', 'age': 21, 'course': 'Python', 'marks': 85, 'grade': 'A'}
#{'name': 'Arun', 'age': 21, 'course': 'Python', 'marks': 85, 'grade': 'A'}
#{'name': 'Arun', 'age': 21, 'course': 'Python', 'marks': 85, 'grade': 'A'}
#{'name': 'Arun', 'age': 21, 'course': 'Python', 'marks': 85, 'grade': 'A'}
#{'name': 'Arun', 'age': 21, 'course': 'Python', 'marks': 85, 'grade': 'A'}


#10

morning_batch = {"Anu", "Rahul", "Arun", "Meera"}
evening_batch = {"Rahul", "Meera", "John", "Priya"}

print('All the unique student names accross the batches :',morning_batch.union(evening_batch))
#All the unique student names accross the batches : {'Priya', 'John', 'Meera', 'Anu', 'Rahul', 'Arun'}

print('Students who attended Both batches :',morning_batch.intersection(evening_batch))
#Students who attended Both batches : {'Rahul', 'Meera'}

print('Students who attended only the morning Batches  :',morning_batch.difference(evening_batch))
#Students who attended only the morning Batches  : {'Anu', 'Arun'}

print('Students who attented only the evening batch :',evening_batch.difference(morning_batch))
#Students who attented only the evening batch : {'Priya', 'John'}