############################################################################# ##
# Copyright (C) 2019-2020 Cameo Communications, Inc.
############################################################################# ##
#
# --------------------------------------------------------------------------
#     AUTHOR                   : EExuke
#     FILE NAME                : 6_importFunc.py
#     FILE DESCRIPTION         : Python file
#     FIRST CREATION DATE      : 2020/02/09
# --------------------------------------------------------------------------
#     Version                  : 1.0
#     Last Change              : 2020/02/09
## ************************************************************************** ##

#-----------------------------------------------------------
#                  MAIN PROCESS
#-----------------------------------------------------------
# test
# 需要句点表示
import moreInput
user_profile = moreInput.build_profile('EE', 'xuke', location='Chengdu', field='C/C++')
print(user_profile)

# 导入特定函数
from listFunc import show_magicians
names = ['EExuke', 'Daiv', 'Trasla',]
named = show_magicians(names)

# as别名
from listFunc import show_magicians as sm
names = ['EExuke', 'Daiv', 'Trasla',]
named = sm(names)

# *无需句点表示
from moreInput import *
user_profile = build_profile('EE', 'xuke', location='Chengdu', field='C/C++')
print(user_profile)

