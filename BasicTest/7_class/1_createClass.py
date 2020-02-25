############################################################################# ##
# Copyright (C) 2019-2020 Cameo Communications, Inc.
############################################################################# ##
#
# --------------------------------------------------------------------------
#     AUTHOR                   : EExuke
#     FILE NAME                : 1_createClass.py
#     FILE DESCRIPTION         : Python file
#     FIRST CREATION DATE      : 2020/02/11
# --------------------------------------------------------------------------
#     Version                  : 1.0
#     Last Change              : 2020/02/11
## ************************************************************************** ##

#-----------------------------------------------------------
#                  MAIN PROCESS
#-----------------------------------------------------------
# 定义类
class Dog() :
    """模拟小狗的类"""
    def __init__(self, name, age) :
        """初始化属性name和age"""
        self.name = name
        self.age = age

    def sit(self) :
        """方法：坐下"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self) :
        """方法：打滚"""
        print(self.name.title() + " rolled over!")

#-----------------------------------------------------------
# 用类创建实例对象
my_dog = Dog('mizai', 2)

print("My dog's name is " + my_dog.name.title() + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()
my_dog.roll_over()

#-----------------------------------------------------------
# 9_1
class Restaurant() :
    """餐厅类"""
    def __init__(self, restaurant_name, cuisine_type) :
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self) :
        print("There is " + self.restaurant_name + ".")
        print("we are main make " + self.cuisine_type + ".")

    def open_restaurant(self) :
        print("now is oppening, welcome!")

restaurant = Restaurant('one ice', 'ice fen')

print("name is " + restaurant.restaurant_name + ".")
print("main make " + restaurant.cuisine_type + ".")
restaurant.describe_restaurant()
restaurant.open_restaurant()

#-----------------------------------------------------------
# 9_3
class User() :
    """用户类"""
    def __init__(self, first_name, last_name, city) :
        self.first_name = first_name
        self.last_name = last_name
        self.city = city

    def describe(self) :
        print("Name: " + self.first_name + self.last_name)
        print("Live City: " + self.city)

    def greet_user(self) :
        print("Hi, " + self.first_name + self.last_name + "!")

user1 = User('xu', 'ke', 'chengdu')
user2 = User('gu', 'jialei', 'jiangying')
user3 = User('cheng', 'yijie', 'guangzhou')

user1.describe()
user1.greet_user()
user2.describe()
user2.greet_user()
user3.describe()
user3.greet_user()

