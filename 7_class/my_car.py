############################################################################# ##
# Copyright (C) 2019-2020 Cameo Communications, Inc.
############################################################################# ##
#
# --------------------------------------------------------------------------
#     AUTHOR                   : EExuke
#     FILE NAME                : my_car.py
#     FILE DESCRIPTION         : Python file
#     FIRST CREATION DATE      : 2020/02/12
# --------------------------------------------------------------------------
#     Version                  : 1.0
#     Last Change              : 2020/02/12
## ************************************************************************** ##

#-----------------------------------------------------------
#                  MAIN PROCESS
#-----------------------------------------------------------
# 导入car.py中的Car类
from classes import Car, ElecCar

my_new_car = Car('audi', 'a6', 2020)
my_new_car.get_descriptive_name()

my_new_car.odometer_reading = 23
my_new_car.read_odometer()


my_tesla = ElecCar('tesla', 'model 3', 2020)
my_tesla.get_descriptive_name()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()


#-----------------------------------------------------------
# 导入整个模块，与函数相同
# import classes
# 用时：classes.Car()

#-----------------------------------------------------------
# 导入模块中所有类，与函数相同
# from classes import *

#-----------------------------------------------------------
# 也可以在模块中导入模块，用于分散模块内容

