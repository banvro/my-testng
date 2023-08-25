# function:::



#

# for i in range(1, 23, 23)



# def sum(*args):
#     total = 0
#     for i in args:
#         total += i 

#     return total


# a = sum(1, 2, 3, 45, 6)


# print("the sum is : ", a)

# print(total)
print("this is a calculator")
def add(*args):
    total=0
    for i in args:
        total+=i
    
    return total

def substract(*args):
    subs=0
    for i in args:
        subs= subs-1
        return subs
    
def multiply(*args):
    mul= 1
    for i in args:
        mul= mul * i
    return mul

def divide(*args):
    div=0
    for i in args:
      if div !=0:
        return divide
    else:
        return("cannot divide by zero")
    
print("select operation ")
print("1.add")
print("2.substract")
print("3.multipy")
print("4.divide")

choice =input("enter choice(1/2/3/4)")

def inputnumbers(*args):
       num=[]
       for i in args:
          num=num.append(i)
       return inputnumbers

if choice == '1':
    print("result",add)
elif choice== '2':
 
 print("result",substract(10,4,5))
elif choice=='3':

    z = multiply(2,2,2)
    print("result",z)

elif choice=='4':
 print("result",divide(50,25,2))



