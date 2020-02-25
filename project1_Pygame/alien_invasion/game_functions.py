############################################################################# ##
# Copyright (C) 2019-2020 Cameo Communications, Inc.
############################################################################# ##
#
# --------------------------------------------------------------------------
#     AUTHOR                   : EExuke
#     FILE NAME                : game_function.py
#     FILE DESCRIPTION         : Python file
#     FIRST CREATION DATE      : 2020/02/25
# --------------------------------------------------------------------------
#     Version                  : 1.0
#     Last Change              : 2020/02/25
## ************************************************************************** ##

import sys
import pygame

#-----------------------------------------------------------
#                  事件响应函数
#-----------------------------------------------------------
def check_keydown_events(event, ship):
    """响应按键按下"""
    if event.key == pygame.K_RIGHT:
        # 向右移动飞船
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # 向左移动飞船
        ship.moving_left = True

def check_keyup_events(event, ship):
    """响应按键松开"""
    if event.key == pygame.K_RIGHT:
        # 停止向右移动飞船
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        # 停止向左移动飞船
        ship.moving_left = False

def check_events(ship):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        # 退出事件
        if event.type == pygame.QUIT:
            sys.exit()
        # 按键事件
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

#-----------------------------------------------------------
#                  更新屏幕函数
#-----------------------------------------------------------
def update_screen(ai_settings, screen, ship, sky):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环都重绘屏幕
    screen.fill(ai_settings.bg_color)
    sky.blitme()
    ship.blitme()
    #让最近绘制的屏幕可见
    pygame.display.flip()

#-----------------------------------------------------------
#                  控制飞船
#-----------------------------------------------------------


