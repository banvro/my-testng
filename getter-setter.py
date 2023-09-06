# # class cls1:
# #     def __init__(self, a, b):
# #         self.name = a
# #         self.__age = b
    
# #     def get_name(self):
# #         return self.name
        
# #     def sdet_name(self, new_name):
# #         if new_name and len(new_name) == 3:
# #             self.name = new_name
    
# #     def delete_name(self):
# #         del self.name
        
# # obj = cls1("moris", 20)

# # obj.sdet_name("oke")
# # obj.delete_name()
# # print(obj.get_name())

# # # del self.n/ame
        

# class xyz:
#     def __init__(self, x, y):
#         self._name = x
#         self.age = y 
    
#     @property
#     def name(self):
#         return self._name
    
#     @name.setter
#     def name(self, new_name):
#         if new_name and len(new_name) == 4:
#             self._name = new_name
    
#     def __str__(self):
#         return f"name is {self._name}"


# obj = xyz("kriss", 20)
# obj.name = "good"
# print(obj)
# # print(obj.name())


class MyClass:
    def __init__(self):
        self.__privadte = 42

    def __private_method(self):
        return "This is a private method"

obj = MyClass()
# Accessing private members from outside the class would typically raise an AttributeError.
# Uncommenting the following lines would result in an AttributeError:
print(obj.__privadte)
# print(obj.__private_method())
