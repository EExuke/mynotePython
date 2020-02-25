############################################################################# ##
# Copyright (C) 2019-2020 Cameo Communications, Inc.
############################################################################# ##
#
# --------------------------------------------------------------------------
#     AUTHOR                   : EExuke
#     FILE NAME                : car.py
#     FILE DESCRIPTION         : Python file 类封装成模块
#     FIRST CREATION DATE      : 2020/02/12
# --------------------------------------------------------------------------
#     Version                  : 1.0
#     Last Change              : 2020/02/12
## ************************************************************************** ##

#-----------------------------------------------------------
#                  MAIN PROCESS
#-----------------------------------------------------------
"""一个表示car的类"""
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
        print("This car has " + str(self.odometer_reading) + " miles on it.")

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

#-----------------------------------------------------------
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

