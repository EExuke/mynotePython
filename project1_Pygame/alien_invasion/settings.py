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
        self.ship_speed_factor = 16.5
        self.ships_limit = 3

        # 子弹设置
        self.bullet_speed_factor = 26.5
        self.bullet_width = 50
        self.bullet_height = 20
        self.bullet_color = (255, 125, 0)
        self.bullets_allowed = 10
        self.bullet_interval = 3

        # 计时器设置
        self.timer = 0

        # 外星人设置
        self.alien_speed_factor = 20
        self.fleet_drop_speed = 64
        self.fleet_direction = 1

