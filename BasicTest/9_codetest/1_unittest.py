############################################################################# ##
# Copyright (C) 2019-2020 Cameo Communications, Inc.
############################################################################# ##
#
# --------------------------------------------------------------------------
#     AUTHOR                   : EExuke
#     FILE NAME                : 1_unittest.py
#     FILE DESCRIPTION         : Python file
#     FIRST CREATION DATE      : 2020/02/12
# --------------------------------------------------------------------------
#     Version                  : 1.0
#     Last Change              : 2020/02/12
## ************************************************************************** ##

#-----------------------------------------------------------
#                  MAIN PROCESS
#-----------------------------------------------------------
# 继承单元测试类unittest
import unittest
from name_function import get_formatted_name

class NameTestCase(unittest.TestCase) :
    """测试name_function.py"""
    def test_first_last_name(self) :
        """是否能正确处理Xu Ke这样的姓名？"""
        formatted_name = get_formatted_name('xu', 'ke')
        self.assertEqual(formatted_name, 'Xu Ke')

    def test_first_last_middle_name(self) :
        """是否能正确处理Ee Xu Ke这样的姓名？"""
        formatted_name = get_formatted_name('ee', 'ke', 'xu')
        self.assertEqual(formatted_name, 'Ee Xu Ke')


unittest.main()

