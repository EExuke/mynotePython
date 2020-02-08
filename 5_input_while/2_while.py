############################################################################# ##
# Copyright (C) 2019-2020 Cameo Communications, Inc.
############################################################################# ##
#
# --------------------------------------------------------------------------
#     AUTHOR                   : EExuke
#     FILE NAME                : 2_while.py
#     FILE DESCRIPTION         : Python file
#     FIRST CREATION DATE      : 2020/02/08
# --------------------------------------------------------------------------
#     Version                  : 1.0
#     Last Change              : 2020/02/08
## ************************************************************************** ##

#-----------------------------------------------------------
#                  MAIN PROCESS
#-----------------------------------------------------------
# 7_4
peiliao = " "
while peiliao != 'quit' :
    peiliao = input("\nwhat peiliao do you need? : ")
    if peiliao != 'quit' :
        print("\nOk, we will add the " + peiliao + " in your pizza.\n")

#-----------------------------------------------------------
# 7_5
age = " "
while age != 'quit' :
    age  = input("\nHow old are you? : ")
    if age.isdigit() :      #数字判断: a.isdigit() 字母判断：a.isalpha 字母或数字：a.isalnum()
        age = int(age)
        if (age < 3) :
            print("this age is free!\n")
        elif ((age >= 3) & (age < 12)) :
            print("this age need $10. \n")
        else :
            print("this age need $15. \n")

#-----------------------------------------------------------
# 7_6
peiliao = " "
while True :
    peiliao = input("\nwhat peiliao do you need? : ")
    if peiliao != 'quit' :
        print("\nOk, we will add the " + peiliao + "in your pizza.\n")
    else :
        break

