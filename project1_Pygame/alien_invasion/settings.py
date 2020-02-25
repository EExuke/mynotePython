############################################################################# ##
# Copyright (C) 2019-2020 Cameo Communications, Inc.
############################################################################# ##
#
# --------------------------------------------------------------------------
#     AUTHOR                   : EExuke
#     FILE NAME                : settings.py
#     FILE DESCRIPTION         : Python file
#     FIRST CREATION DATE      : 2020/02/24
# --------------------------------------------------------------------------
#     Version                  : 1.0
#     Last Change              : 2020/02/24
## ************************************************************************** ##

#-----------------------------------------------------------
#                  设置类
#-----------------------------------------------------------
class Settings():
    """存储《外星人入侵》的所有设置的类"""

    def __init__(self):
        """初始化游戏的设置"""
        # 屏幕设置
        self.screen_width = 2600
        self.screen_height = 1700
        self.bg_color = (0, 0, 0)

        # 飞船的设置
        self.ship_speed_factor = 6.5

