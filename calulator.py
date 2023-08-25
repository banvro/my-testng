print("""
      ::::Enter what you want to do:::::
    1) Print Anything
    2) Strat Calculator
    3) Do nothing
""")
    
choce = int(input("ENter what you wanat : "))

if choce == 1:
    print("I am anything..")

elif choce == 2:
    print("*****************calculator****************")

    num1 = int(input("Enter first number : "))
    num2 = int(input("Enter second number : "))

    print("""
        :::::::ENter what you wish to do::::::::
        1) Adation
        2) Subtraction 
        3) Multiplication 
        4) Devsion
    """)
        

    choice = input("Enter what you want : ")


    if choice == "1":
        sum = num1 + num2
        print("the sum is : ", sum)

    elif choice == "2":
        sub = num1 - num2
        print("the substraction is : ", sub)

    elif choice == "3":
        multi = num1 * num2
        print("the Multiplication is : ", multi)

    elif choice == "4":
        div = num1 / num2
        print("the devsion is : ", div)

    else:
        print("Something went wronng....")


else:
    print("do nothng....")



# while loop 