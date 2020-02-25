############################################################################# ##
# Copyright (C) 2019-2020 Cameo Communications, Inc.
############################################################################# ##
#
# --------------------------------------------------------------------------
#     AUTHOR                   : EExuke
#     FILE NAME                : 2_fordic.py
#     FILE DESCRIPTION         : Python file
#     FIRST CREATION DATE      : 2020/02/07
# --------------------------------------------------------------------------
#     Version                  : 1.0
#     Last Change              : 2020/02/07
## ************************************************************************** ##

#-----------------------------------------------------------
#                  MAIN PROCESS
#-----------------------------------------------------------
# 6_4
dictionary = {
    'var': '变量',
    'if': '条件判断_如果',
    'else': '条件判断_否则',
    'for': '用于循环遍历',
    'print': '用于打印输出',
    }

for k, v in dictionary.items():
    print("\nKey: " + k)
    print("Value: " + v)

for k in dictionary.keys():
    print(k)

for v in dictionary.values():
    print(v)

#-----------------------------------------------------------
# 6_6
persons = ['xuke', 'jareygu', 'jackcheng']
favorite_language = {'xuke':'C', 'jackcheng':'java',}

for name in persons:
    if name in favorite_language.keys() :
        print("Hi," + name.title() + "Thank your anuswer!")
    else :
        print("Hi," + name.title() + "Please tell me your favorite language!")

