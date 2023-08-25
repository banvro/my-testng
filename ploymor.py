# 1) Polymorphism :
    
# poly  => Many
# morphism => Forms

# 1) Duck Type
# 2) Operator overridding
# 3) Method Overloading
# 4) Method Overriding

# Operator overridding:

# 12 + 10

# a = 10
# b = 20

# c = a + b

# operands ( a, b)
# + => operator +, -, *, /, ++(inccrement operator), --(decrement operator) +=

# a = 10

# a+=1
# a = a+1
# print(a)

# + 

# 10 + 20 + 30
# concatination=> to join two string..

# a = "hlo"
# b = "mydata"

# print(a+b)



# class Myclass:
#     def __init__(self, x, y):
#         self.var1 = x
#         self.var2 = y
    
#     def mymthd(self):
#         print("i am a method..")
    
#     def __add__(abc, xyz):
#         m1 = abc.var1 + xyz.var1
#         m2 = abc.var2 + xyz.var2
#         sum = Myclass(m1, m2)
#         return sum

# obj1 = Myclass(12, 10)
# obj2 = Myclass(30, 40)

# sum = obj1 + obj2


# print(sum.var1)
# # print(type(obj2))

# print(10 - 20)


class Myclass:
    def __init__(self):
        pass

    def xyz(self, a = None, b = None, c = None):
        if a != None and b != None and c !=None:
            d = a + b +c
            print(d)
        elif a != None and b != None:
            x = a + b
            print(x)
        else:
            print(a)
        
    
obj = Myclass()

obj.xyz(12)











