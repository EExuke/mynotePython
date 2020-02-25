############################################################################# ##
# Copyright (C) 2019-2020 Cameo Communications, Inc.
############################################################################# ##
#
# --------------------------------------------------------------------------
#     AUTHOR                   : EExuke
#     FILE NAME                : 3_subClass.py
#     FILE DESCRIPTION         : Python file
#     FIRST CREATION DATE      : 2020/02/12
# --------------------------------------------------------------------------
#     Version                  : 1.0
#     Last Change              : 2020/02/12
## ************************************************************************** ##

#-----------------------------------------------------------
#                  MAIN PROCESS
#-----------------------------------------------------------
# 继承：由父类创建特殊子类
class Car() :
    """父类：汽车类"""
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

# 定义子类，继承自父类
class ElectricCar(Car) :
    """子类：继承自父类Car"""
    def __init__(self, make, model, year) :
        """
        初始化父类的属性，并添加子类自己独特的属性
        """
        super().__init__(make, model, year)
        self.battery_size = 70

    def describe_battery(self) :
        """子类自己独特的方法"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.\n")


my_tesla = ElectricCar('tesla', 'model s', 2020)
my_tesla.get_descriptive_name()
my_tesla.describe_battery()


# 实例battery作为属性
class Battery() :
    """电瓶属性归为一个实例"""
    def __init__(self, battery_size = 70) :
        """初始化电瓶属性"""
        self.battery_size = battery_size

    def describe_battery(self) :
        """定义电瓶的方法"""
        print("This car has a " + str(self.battery_size) + "-kWh battery.\n")

    def get_range(self) :
        """显示电瓶的续航里程"""
        if self.battery_size == 70 :
            range = 240
        elif self.battery_size == 85 :
            range = 270
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message)


class ElecCar(Car) :
    """使用实例作属性"""
    def __init__(self, make, model, year) :
        """初始化父类的属性，并使用属性实例添加子类自己独特的属性"""
        super().__init__(make, model, year)
        self.battery = Battery()

my_tesla = ElecCar('tesla', 'model 3', 2020)
my_tesla.get_descriptive_name()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

#-----------------------------------------------------------
# 9_6
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


privileges = ['can add post', 'can delete post', 'can ban user',]
class Privileges() :
    """权限类"""
    def __init__(self) :
        self.privileges = privileges

    def show_privileges(self) :
        """方法：显示管理员权限"""
        for privilege in self.privileges :
            print(" " + privilege + " ")


class Admin(User) :
    """管理员用户"""
    def __init__(self, first_name, last_name, city) :
        """初始化父类的属性"""
        super().__init__(first_name, last_name, city)
        self.privileges = Privileges()


admin = Admin('EE', 'xuke', 'chengdu')
admin.privileges.show_privileges()

