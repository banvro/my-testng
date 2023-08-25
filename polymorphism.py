# Polymorphism:
    
#     Duck Typing
#     Method Overloading
#     Method Overriding
#     Operator overloading
    
    
# 1) Method Overloading:

# class name:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def sumis(self):
#         print(self.x + self.y)
    
#     def __add__(slef, other):
#         m1 = slef.x + other.x
#         m2 = slef.y + other.y

#         sumnow = name(m1, m2)
#         return sumnow

# obj1 = name(12, 23)
# obj2 = name(20, 40)

# # obj1.sumis()
# i = obj1 + obj2
# print(i.x)



# class calculator:

#     def __init__(self, var1, var2):
#         self.var1 = var1
#         self.var2 = var2 

#     def ender(self):
#         print("i am enter")
    
#     def __add__(self, other):
#         x = self.var1 + other.var1
#         y = self.var2 + other.var2
#         cum = calculator(x, y)

#         return cum

# obj1 = calculator(12, 19)
# obj2 = calculator(10, 20)

# c = obj1 + obj2

# print(c.var2)