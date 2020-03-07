############################################################################# ##
# Copyright (C) 2019-2020 Cameo Communications, Inc.
############################################################################# ##
#
# --------------------------------------------------------------------------
#     AUTHOR                   : EExuke
#     FILE NAME                : alien.py
#     FILE DESCRIPTION         : Python file
#     FIRST CREATION DATE      : 2020/02/27
# --------------------------------------------------------------------------
#     Version                  : 1.0
#     Last Change              : 2020/02/27
## ************************************************************************** ##

import pygame
from pygame.sprite import Sprite

#-----------------------------------------------------------
#                  外星人类
#-----------------------------------------------------------
class Alien(Sprite):
    """表示单个外星人的类"""
    def __init__(self, ai_settings, screen):
        """初始化外星人并设置其起始位置"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载外星人图像并设置其rect属性
        self.image = pygame.image.load('images/alien_1.png')
        self.rect = self.image.get_rect()

        # 每个外星人最初都在左上角附近
        self.rect.x = (self.rect.width / 2)
        self.rect.y = (self.rect.height / 10)

        # 存储外星人的准确位置
        self.x = float(self.rect.centerx)
        self.y = float(self.rect.centery)

        # 外星人移动方向
        self.direction = 1

    def blitme(self):
        """在指定位置绘制外星人"""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """检测是否到达屏幕边界，是则返回True"""
        screen_rect = self.screen.get_rect()
        if self.rect.top >= screen_rect.bottom:
            self.rect.y = 0
        elif self.rect.right >= screen_rect.right:
            self.rect.x = screen_rect.right
            return True
        elif self.rect.left <= 0:
            self.rect.x = 0
            return True
        else:
            return False

    def update(self):
        """移动外星人的位置"""
        self.x += (self.ai_settings.alien_speed_factor * self.direction)
        self.rect.x = self.x

