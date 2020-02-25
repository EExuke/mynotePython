############################################################################# ##
# Copyright (C) 2019-2020 Cameo Communications, Inc.
############################################################################# ##
#
# --------------------------------------------------------------------------
#     AUTHOR                   : EExuke
#     FILE NAME                : alien_invasion.py
#     FILE DESCRIPTION         : Python file
#     FIRST CREATION DATE      : 2020/02/24
# --------------------------------------------------------------------------
#     Version                  : 1.0
#     Last Change              : 2020/02/24
## ************************************************************************** ##

import pygame

from settings import Settings
from ship import Ship, Bg
import game_functions as gf

#-----------------------------------------------------------
#                  启动游戏主程序
#-----------------------------------------------------------
def run_game():
    # 初始化并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建一艘飞船、背景图
    ship = Ship(screen, ai_settings)
    sky = Bg(screen)

    # 开始游戏主循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ship)
        # 更新飞船控制结果
        ship.update()
        # 更新屏幕
        gf.update_screen(ai_settings, screen, ship, sky)


# 启动游戏
run_game()

#-----------------------------------------------------------
#                  MAIN PROCESS
#-----------------------------------------------------------

