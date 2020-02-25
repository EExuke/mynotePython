############################################################################# ##
# Copyright (C) 2019-2020 Cameo Communications, Inc.
############################################################################# ##
#
# --------------------------------------------------------------------------
#     AUTHOR                   : EExuke
#     FILE NAME                : 1_input.py
#     FILE DESCRIPTION         : Python file
#     FIRST CREATION DATE      : 2020/02/08
# --------------------------------------------------------------------------
#     Version                  : 1.0
#     Last Change              : 2020/02/08
## ************************************************************************** ##

#-----------------------------------------------------------
#                  MAIN PROCESS
#-----------------------------------------------------------
# 7_1
car = input("\nTell me what car you need: ")
print("Let me see if I can find you a " + car + "\n")

#-----------------------------------------------------------
# 7_2
member = input("\nTell me how many peopel will coming: ")
member = int(member)
if (member > 8) :
    print("sorry, we have not enough sets!\n")
else :
    print("Ok, we will wait for your coming\n")

#-----------------------------------------------------------
# 7_3
num = input("\ninput a number: ")
num = int(num)
if ((num % 10) == 0) :
    print("the num is 10's multiple!\n")
else :
    print("the nun is not 10's multiple\n")

