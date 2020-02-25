############################################################################# ##
# Copyright (C) 2019-2020 Cameo Communications, Inc.
############################################################################# ##
#
# --------------------------------------------------------------------------
#     AUTHOR                   : EExuke
#     FILE NAME                : 5_moreInput.py
#     FILE DESCRIPTION         : Python file
#     FIRST CREATION DATE      : 2020/02/09
# --------------------------------------------------------------------------
#     Version                  : 1.0
#     Last Change              : 2020/02/09
## ************************************************************************** ##

#-----------------------------------------------------------
#                  MAIN PROCESS
#-----------------------------------------------------------
# 8_12
def sandwich(*toppings) :
    """打印任意多参数"""
    print("toppings:")
    for topping in toppings :
        print("-" + topping)

sandwich('peppertion')
sandwich('peppertion', 'morstosh', 'moshroom')

#-----------------------------------------------------------
# 8_13
def build_profile(first, last, **user_info) :
    """任意数量的形参和其值"""
    profile = {}
    profile['first'] = first
    profile['last'] = last
    for k, v in user_info.items() :
        profile[k] = v
    return profile

user_profile = build_profile('EE', 'xuke', location='Chengdu', field='C/C++')
print(user_profile)

