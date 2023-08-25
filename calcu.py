print("******************Calculater**************")

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))

print("""
      ......PLease choose any of one........
    1) Adation
    2) Substraction
    3) Multiplication 
    4) Devsion
""")
      
choce = input("Enter what you want to do : ")
# 3
# "3" == "1"
if choce == "1":
    sum = num1 + num2
    print("the sum is : ", sum)

elif choce == "2":
    sub = num1 - num2
    print("The substraction is : ", sub)


elif choce == "3":
    mul = num1 * num2
    print("The multiplication is : ", mul)


elif choce == "4":
    div = num1 / num2
    print("The devsion is : ", div)

else:
    print("Something went wrong..")