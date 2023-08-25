# # Online Python compiler (interpreter) to run Python online.
# # Write Python 3 code in this online editor and run it.
# print("Hello world")
# print("*******calculator*********")
# num1= int(input("Enter the first digit:"))
# num2= int(input("Enter the second digit:"))
# print("""
# .........kindly choose from the option below.....
#           1)addition
#           2)subtraction
#           3)mutiplication
#           4)division
#   """)
# choose=input("enter the command")
#   #2
#   #2=="1"
# if choose=="1":
#           sum= num1+ num2
#           print("the sum is:",sum)
# elif choose=="2" : 
#           sub= num1-num2
#           print("the answer is:" ,sub)
# elif choose=="3" :   
#           mul=num1*num2
#           print("the product is:" ,mul)
# elif choose=="4" :
#           div=num1/num2
#           print("the answer is:" ,div)
# else:
#           print("something went wrong")
          
# Data Types:

# 1) Integer
# 2) String
# 3) Float 
# 4) Boolean
# 5) List 
# 6) Tuple 
# 7) Set 
# 8) Dictionry
# type()


# List : are used to colect data of diirent types....
# []
# x = [1, 2, 2.8, "stri", 12]

# print(type(x))

# slicing : 

# [start:end:inncrement]

# print(x[1:3])


# Tuple:
# ()

# x = (1, 12, "17238713y1823")

# print(type(x))

# Dictionary: key : pair relationship
# {}
# x = {"name" : "xyz", "age" : 10, "city" : "mohali"}


# print(x['age'])

# Set
# {}

# xyz = {"uuu", 12, "90", 12}

# print(xyz)

# print(type(xyz))











# Loops: are used to itreation

# a = [12, "xyz", "pqt", 82]

# for i in a:
#     print('aaaaaaaaaaaaa')
#     print(i)

# xyz = [1, 3, 2, 1, 3, 7]

# total = 0

# for y in xyz:
#     total = total + y
#     print(total)


    

# break
# continue
# pass
# abc= [11, 2 , 3, 54, 56, 12, 23 ,343, 23] 
# total= 0

# for y in abc:
  
#   if y == 56:
#     #   break
#     continue
#   print(y)
    #   print("ddddddddddd")
  

# a = "i am a human"

# for y in a:
#     if y == "a":
#         continue
#     print(y)







# a = "i am a human"

# for y in a:
#     pass

# 1) For Loop
# 2) While Loop

# range(start, end, increment)
# total = 0
# for x in range(1, 12):
#     total = total + x
#     print(total)
    
# total=0
# for x in range(66,144):
#     total= total + x
# print(total)

# y=" the weather is good"

# for i in y:
#     if i == "o":
#         continue
#     print(i)
    



# range(start, end, increment)

# start = 0
# end = n-1
# inrement default 1

# for i in range(1,10, 2):
#     print(i)






# functions::::::::
# functions: are used  for code optimization


# decleartion of function
def abc():
    print("hlo ok ")
    
# call a function
abc()

abc()

abc()


abc()







# def abc():
#     print("ok")
    
    
# 1) Perameters
# 2) Arguments

# def sum(a, b):
#     # print("a is : ", a)
#     c = a + b
#     print("The sum is : ", c)
    
# sum(12, 10)

# sum(10, 50)


# arbitrary arguments

# *args

def sumthis(*args):
    total = 0
    for i in args:
        total = total + i
    return total
# return
abc = sumthis(12, 23, 34, 45)

print(abc)
# print(total)
