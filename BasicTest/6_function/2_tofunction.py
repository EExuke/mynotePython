############################################################################# ##
# Copyright (C) 2019-2020 Cameo Communications, Inc.
############################################################################# ##
#
# --------------------------------------------------------------------------
#     AUTHOR                   : EExuke
#     FILE NAME                : 2_tofunction.py
#     FILE DESCRIPTION         : Python file
#     FIRST CREATION DATE      : 2020/02/09
# --------------------------------------------------------------------------
#     Version                  : 1.0
#     Last Change              : 2020/02/09
## ************************************************************************** ##

#-----------------------------------------------------------
#                  MAIN PROCESS
#-----------------------------------------------------------
# 8_3
def make_shirt(size, outlook) :
    """T恤"""
    print("make the T-shirt in size of : " + size + "\n")
    print("make the T-shirt with outlook of : " + outlook + "\n")

make_shirt('XL', 'startSky')
make_shirt(outlook = 'blank', size = 'M')

#-----------------------------------------------------------
# 8_4
def make_shirt_L(size = 'L', outlook = 'I Love Python') :
    """T恤"""
    print("make the T-shirt in size of : " + size + "\n")
    print("make the T-shirt with outlook of : " + outlook + "\n")

make_shirt_L()
make_shirt_L(size = 'M')
make_shirt_L(outlook = 'I love C/C++')

#-----------------------------------------------------------
# 8_4
citys = {'Chengdu':'China', 'Suzhou':'China', 'Xinde':'American',}
def describe_city(city, country = 'China') :
    """描述城市所属国家"""
    print("\nthe city " + city +" is in " + country + ".\n")

for city, country in citys.items() :
    if country == 'China' :
        describe_city(city)
    else :
        describe_city(city, country)

