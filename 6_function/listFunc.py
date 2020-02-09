############################################################################# ##
# Copyright (C) 2019-2020 Cameo Communications, Inc.
############################################################################# ##
#
# --------------------------------------------------------------------------
#     AUTHOR                   : EExuke
#     FILE NAME                : 4_listFunc.py
#     FILE DESCRIPTION         : Python file
#     FIRST CREATION DATE      : 2020/02/09
# --------------------------------------------------------------------------
#     Version                  : 1.0
#     Last Change              : 2020/02/09
## ************************************************************************** ##

#-----------------------------------------------------------
#                  MAIN PROCESS
#-----------------------------------------------------------
# 8_9
def show_magicians(names) :
    """打印出魔术师们的名字"""
    named = []
    while names :
        name = names.pop()
        print("\nLet us welcome magician: " + name)
        named.append(name)
    return named

names = ['EExuke', 'Daiv', 'Trasla',]
named = show_magicians(names)
print("\n")

#-----------------------------------------------------------
# 8_10
names = ['EExuke', 'Daiv', 'Trasla',]
def make_great(names) :
    """加称号,改变列表"""
    maked = []
    for name in names :
        name = 'The great ' + name
        maked.append(name)
    names = show_magicians(maked)
    return(names)

names = make_great(names)
show_magicians(names)
print("\n")

#-----------------------------------------------------------
# 8_11
names = ['EExuke', 'Daiv', 'Trasla',]
make_great(names[:])
show_magicians(names)
print("\n")

