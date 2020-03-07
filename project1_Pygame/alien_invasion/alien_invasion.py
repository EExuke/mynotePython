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
from pygame.sprite import Group

import game_functions as gf

from settings import Settings
from ship import Ship, Bg
from bullet import Bullet
from alien import Alien
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

#-----------------------------------------------------------
#                  启动游戏主程序
#-----------------------------------------------------------
def run_game():
    # 初始化并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建Play按钮
    play_button = Button(ai_settings, screen, "Play")

    # 创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)

    # 创建一艘飞船、背景图
    ship = Ship(screen, ai_settings)
    sky = Bg(screen)
    sky.blitme()
    # 创建一个用于存储子弹的编组
    bullets = Group()
    # 创建外星人群
    aliens = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏主循环
    while True:
        # 等待按下开始按钮
        gf.check_events(ai_settings, screen, ship, aliens, bullets, stats, play_button, sb)
        # 开始游戏，并计时
        ai_settings.timer += 1
        if stats.game_active:
            # 更新飞船控制结果
            ship.update()
            # 更新子弹状态
            gf.update_bullets(aliens, bullets, ai_settings, screen, ship, stats, sb)
            # 更新外星人位置，在子弹之后方便检测是否击中
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets, sb)
        # 更新屏幕
        gf.update_screen(ai_settings, screen, ship, sky, aliens, bullets, stats, play_button, sb)


# 启动游戏
run_game()

#-----------------------------------------------------------
#                  END
#-----------------------------------------------------------

