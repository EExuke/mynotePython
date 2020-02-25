############################################################################# ##
# Copyright (C) 2019-2020 Cameo Communications, Inc.
############################################################################# ##
#
# --------------------------------------------------------------------------
#     AUTHOR                   : EExuke
#     FILE NAME                : 1_person.py
#     FILE DESCRIPTION         : Python file
#     FIRST CREATION DATE      : 2020/02/07
# --------------------------------------------------------------------------
#     Version                  : 1.0
#     Last Change              : 2020/02/07
## ************************************************************************** ##

#-----------------------------------------------------------
#                  MAIN PROCESS
#-----------------------------------------------------------
# 6_1
person_0 = {
    'first_name': 'Xu',
    'last_name': 'Ke',
    'age': 23,
    'city': 'chengdu',
    }

print("the person0 name is:" +
    person_0['first_name'] + person_0['last_name'] +
    "\nhis age is : " + str(person_0['age']) +
    "\nand he is live in " + person_0['city'] +
    ".")

#-----------------------------------------------------------
# 6_2
person_0['fanum'] = 7

print("the favorite number is:" + 
    str(person_0['fanum']) + 
    ".\n")

#-----------------------------------------------------------
# 6_3
dictionary = {
    'var': '变量',
    'if': '条件判断_如果',
    'else': '条件判断_否则',
    'for': '用于循环遍历',
    'print': '用于打印输出',
    }

print("var: " + dictionary['var'] + "\n" +
    "if: " + dictionary['if'] + "\n" +
    "else: " + dictionary['else'] + "\n" +
    "for: " + dictionary['for'] + "\n" +
    "print: " + dictionary['print'] +
    ".")

