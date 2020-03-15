############################################################################# ##
# Copyright (C) 2019-2020 Cameo Communications, Inc.
############################################################################# ##
#
# --------------------------------------------------------------------------
#     AUTHOR                   : EExuke
#     FILE NAME                : countries.py
#     FILE DESCRIPTION         : Python file
#     FIRST CREATION DATE      : 2020/03/14
# --------------------------------------------------------------------------
#     Version                  : 1.0
#     Last Change              : 2020/03/14
## ************************************************************************** ##

from pygal_maps_world.i18n import COUNTRIES

#-----------------------------------------------------------
#                  根据国家名获得国别码
#-----------------------------------------------------------
# 将导入的国别码字典，按字母排序后输出
# for country_code in sorted(COUNTRIES.keys()):
#     print(country_code, COUNTRIES[country_code])

def get_country_code(country_name):
    """ 根据指定的国家,返回 Pygal 使用的两个字母的国别码 """
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
        # 如果没有找到指定的国家,就返回 None
    return None

