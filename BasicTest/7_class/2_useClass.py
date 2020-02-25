############################################################################# ##
# Copyright (C) 2019-2020 Cameo Communications, Inc.
############################################################################# ##
#
# --------------------------------------------------------------------------
#     AUTHOR                   : EExuke
#     FILE NAME                : 2_useClass.py
#     FILE DESCRIPTION         : Python file
#     FIRST CREATION DATE      : 2020/02/11
# --------------------------------------------------------------------------
#     Version                  : 1.0
#     Last Change              : 2020/02/11
## ************************************************************************** ##

#-----------------------------------------------------------
#                  MAIN PROCESS
#-----------------------------------------------------------
# 例
class Car() :
    """汽车类"""
    def __init__(self, make, model, year) :
        """初始化属性,公里数默认为0"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self) :
        print("Make: " + self.make)
        print("Model: " + self.model)
        print("Made in: " + str(self.year))

    def read_odometer(self) :
        """打印公里数"""
        print("This car has " + str(self.odometer_reading) + "miles on it.")

    def update_odometer(self, mileage) :
        """修改公里数"""
        if mileage >= self.odometer_reading :
            self.odometer_reading = mileage
            print("odometer already update !\n")
        else :
            print("You can't roll back an odometer!\n")
            print("odometer update failed!\n")

    def increment_odometer(self, miles) :
        """增加公里数"""
        if miles >= 0 :
            self.odometer_reading += miles
            print("increment odometer Successfull! \n")
        else :
            print("increment odometer failed! Can not increment miles < 0 .\n")


new_car = Car('auid', 'a6', 2020)

new_car.get_descriptive_name()
new_car.read_odometer()
print("After 23 meters...\n")
new_car.odometer_reading = 23
new_car.read_odometer()

new_car.update_odometer(24)
new_car.read_odometer()
new_car.update_odometer(22)
new_car.increment_odometer(100)
new_car.increment_odometer(-50)

#-----------------------------------------------------------
# 9_5
print("\n 9_5 \n")
class User() :
    """用户类"""
    def __init__(self, first_name, last_name, city) :
        """初始化属性"""
        self.first_name = first_name
        self.last_name = last_name
        self.city = city
        self.login_attempts = 0

    def describe(self) :
        print("Name: " + self.first_name + self.last_name)
        print("Live City: " + self.city)

    def greet_user(self) :
        print("Hi, " + self.first_name + self.last_name + "!")

    def increment_login_attempts(self) :
        """累加登录次数"""
        self.login_attempts += 1

    def reset_login_attempts(self) :
        """重置登录次数记录"""
        self.login_attempts = 0

user1 = User('EE', 'xuke', 'chengdu')
print("login_attempts: " + str(user1.login_attempts))
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
print("login_attempts: " + str(user1.login_attempts))
user1.reset_login_attempts()
print("login_attempts: " + str(user1.login_attempts))

