#******************************
#**********Slicing*************
#********************************

S1 = "Trivandrum"
print(S1[6])       #will display 7th character 
print(S1[-4])

print(S1[0:5])      #slicing. start index=0, end index =4. 'triva'
print(S1[6:10])     # slicing. 'drum'
#print(S1[10])      # this causes error. indexation, index out of range

print(S1[4:7])      #getting value from middle


print(S1[:5])       # to get final numbers correctly when we give first and alst num it just assumes we are taking to the end.
print(S1[6:])        

print(S1[:5:2])    # default steps are 1, if we want to increase the steps, specify it like this then we would get,our desired steps, like in this code we would get "TIA",because the steps are listed as 2,the computer would jump 2 alphebets at a time
print(S1[0:5:2])
print(S1[:8:3])

string_demo= "join our offline programs in kerala IT PARKS" 

print(string_demo[5:])
print(string_demo[5::2])        #using starting index and giving steps to getdesired answer

#string REversing 

print(S1[::-1])                 #this is used to reverse the string in this answer will come out as'murdnavirt'
print(string_demo[12::-1])      # this is an example where we combine slicing and reversing.
print(string_demo[25::-3])      # few other examples of reversing
print(string_demo[:0:-1])
print(string_demo[:-27:-1])
print(string_demo[:3:-1])

#****************************************
#***********Functions*******************
#**************************************

S1 = 'tRIVANDUM'

print(S1)
print(S1.lower())        #coversion of letter formats to capital to small letters and vise versa
print(S1.upper())
print(S1.swapcase())
print(S1.capitalize())   #this one capitaize the first letter de-capitalize the rest

#********************************************
#*************
