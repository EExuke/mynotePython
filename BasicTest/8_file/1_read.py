############################################################################# ##
# Copyright (C) 2019-2020 Cameo Communications, Inc.
############################################################################# ##
#
# --------------------------------------------------------------------------
#     AUTHOR                   : EExuke
#     FILE NAME                : 1_read.py
#     FILE DESCRIPTION         : Python file
#     FIRST CREATION DATE      : 2020/02/12
# --------------------------------------------------------------------------
#     Version                  : 1.0
#     Last Change              : 2020/02/12
## ************************************************************************** ##

#-----------------------------------------------------------
#                  MAIN PROCESS
#-----------------------------------------------------------
# rstrip() 去除行尾的换行符号，使用strip()去除行首尾空格
filename = 'pi_digits.txt'

with open(filename) as file_object :
    for line in file_object :
        print(line.rstrip())

print("\n")
# readlines()读取每行; with内部创建列表，给外部使用
with open(filename) as file_object :
    lines = file_object.readlines()

for line in lines :
    print(line.rstrip())

# use
pi_string = ''
for line in lines :
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

print(pi_string.replace('3', '7'))

