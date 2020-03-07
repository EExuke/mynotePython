############################################################################# ##
# Copyright (C) 2019-2020 Cameo Communications, Inc.
############################################################################# ##
#
# --------------------------------------------------------------------------
#     AUTHOR                   : EExuke
#     FILE NAME                : ship.py
#     FILE DESCRIPTION         : Python file
#     FIRST CREATION DATE      : 2020/02/24
# --------------------------------------------------------------------------
#     Version                  : 1.0
#     Last Change              : 2020/02/24
## ************************************************************************** ##

import pygame
from pygame.sprite import Sprite

#-----------------------------------------------------------
#                  管理飞船行为的类
#-----------------------------------------------------------
class Ship(Sprite):

    def __init__(self, screen, ai_settings):
        """初始化飞船并设置其初始位置"""
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship_1.png')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘新飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 在属性center中存储小数
        self.center = float(self.rect.centerx)

        # 移动标志
        self.moving_right = False
        self.moving_left = False
        self.fire = False

    def update(self):
        """根据移动标志调整飞船的位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.center -= self.ai_settings.ship_speed_factor
        # 再根据center更新rect对象
        self.rect.centerx = self.center

    def center_ship(self):
        """让飞船居中到初始位置"""
        self.center = self.screen_rect.centerx

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

#-----------------------------------------------------------
#                  背景图片
#-----------------------------------------------------------
class Bg():

    def __init__(self, screen):
        """初始化并设置初始位置"""
        self.screen = screen

        # 加载图像并获取其外接矩形
        self.image = pygame.image.load('images/bg_alien.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def blitme(self):
        """在指定位置绘制"""
        self.screen.blit(self.image, self.rect)

