#******************************************
#*****************************************
#***********File handeling****************
#*****************************************

#
#file = open('students.txt','r') 



filepath = "C:/PGP_AI_ML/Python/sample.txt"
relative_filepath = 'test.txt'


def read_file_filepath():
    file = open(filepath,'r')   #assign the file in reading mode
    content = file.read()   #contents of the file is assigned to 'content'.
    print(content)



def read_file_rela_filepath():
    file_1 = open(relative_filepath,'r')
    content_1 = file_1.read()
    print(content_1)


#file.read() will return all the values as a single string

# print(type(content_1)) #a single string


def read_line_by_line():
    file = open(relative_filepath,'r')
    content = file.readline()
    print(content)
    print(type(content))

read_line_by_line()



def read_lines_():
    file = open(relative_filepath,'r')
    content = file.readlines()            # read all lines and populates the list called content
    print(content)
    for line in content:
        print(line)
    print(type(content))


read_lines_()