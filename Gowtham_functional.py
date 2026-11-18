def mark():
    m = int(input("please enter the mark :"))
    return m

def calculate_grade(mark):
    if(mark>=90):
        print("A")
    elif(mark>=75):
        print("B")
    elif(mark>=60):
        print("C")
    elif(mark>=40):
        print("D")
    elif(mark<40):
        print("Fail")



scores = mark()
print("you scored",calculate_grade(scores), "This garde in this semester")



#2

def calculation_input():
    c = float(input("Please enter the first number :"))
    a = float(input("Please enter the Second number :"))
   
    return c,a


def calculation_operator():
    u = str(input("Please enter operator u want to use from this (+,-,*,/) :"))
    return u






def calculator(calc,c,a):
    if(calc == "+"):
        print(a+c)
    elif(calc == "-"):
        print(a-c)
    elif(calc == "*"):
        print(a*c)
    elif(calc == "/"):
        print(a/c)
    else:
        print("invalid operator entered")


numbers = calculation_input()
operators = calculation_operator()

calculator(operators,numbers[0],numbers[1])

#3


def principle():
    p = float(input("Please enter the principle amount :"))
    return p

def rate():
    r = float(input("please enter the Rate of interest :"))
    return r

def time():
    t = int(input("please enter the time"))
    return t

def simple_interst(p,r,t):
    print(p*r*t/100)


simple_interst(principle(),rate(),time())



#4

def name():
    i = str(input("Please enter the word "))
    return i


def last_character(i):
    print(i[-1])
    return i


i = name()
last_character(i)



#5
def bill():
    b = float(input("please enter the amount of electricty consumed :"))
    return b

def calculate_bill(b):
    if(b<=100):
        print("Your electricity bill is ",b*5)
    elif(b<=200):
        print("Your electricity bill is ",500+(b-100)*7)
    elif(b<=300):
        print("Your electricity bill is ",1400+(b-200)*10)
    else:
        print("Electricity consumption exceeded 300 ")
    return b


b = bill()

calculate_bill(b)

#6





def count_even(t):
    count = 0

    for i  in t:
        if(i%2==0):
            count += 1
    return count

t = [10,12,13,46,59,2,3,4,6,5,6,8]
count_even(t)
print(count_even(t))


