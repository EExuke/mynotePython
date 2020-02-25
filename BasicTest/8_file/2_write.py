############################################################################# ##
# Copyright (C) 2019-2020 Cameo Communications, Inc.
############################################################################# ##
#
# --------------------------------------------------------------------------
#     AUTHOR                   : EExuke
#     FILE NAME                : 2_write.py
#     FILE DESCRIPTION         : Python file
#     FIRST CREATION DATE      : 2020/02/12
# --------------------------------------------------------------------------
#     Version                  : 1.0
#     Last Change              : 2020/02/12
## ************************************************************************** ##

#-----------------------------------------------------------
#                  MAIN PROCESS
#-----------------------------------------------------------
# 写入空文件
filename = 'pro.txt'

with open(filename, 'w') as file_object :
    file_object.write("I love programing!\nwhat ever use C/C++ or Python.\n")
    file_object.write("I love creating new games.\n")

#-----------------------------------------------------------
# 附加模式写文件
with open(filename, 'a') as file_object :
    file_object.write("I also love Linux_shell programing!\n")

#-----------------------------------------------------------
# 10_3
filename = 'guest.txt'
while True :
    name = input("tell me your name ('quit' for end): ")
    if name == 'quit' :
        break
    with open(filename, 'a') as file_object :
        file_object.write(name + "\n")
        print("Hi, " + name.title() + " welcome to my party!\n")

