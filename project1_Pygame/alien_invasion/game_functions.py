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
import random
from time import sleep

from bullet import Bullet
from alien import Alien

#-----------------------------------------------------------
#                  事件响应函数
#-----------------------------------------------------------
def check_keydown_events(event, ai_settings, screen, ship, bullets):
    """响应按键按下"""
    if event.key == pygame.K_RIGHT:
        # 向右移动飞船
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        # 向左移动飞船
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        # 开火
        ship.fire = True
    elif event.key == pygame.K_q:
        # 按q退出游戏
        sys.exit()


def check_keyup_events(event, ship):
    """响应按键松开"""
    if event.key == pygame.K_RIGHT:
        # 停止向右移动飞船
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        # 停止向左移动飞船
        ship.moving_left = False
    elif event.key == pygame.K_SPACE:
        # 停止开火
        ship.fire = False


def check_play_button(ai_settings, screen, ship, aliens, bullets, stats, play_button, mouse_x, mouse_y, sb):
    """ 在玩家单击 Play 按钮时开始新游戏 """
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # 重置动态设置的参数
        ai_settings.initialize_dynamic_settings()
        # 隐藏光标
        pygame.mouse.set_visible(False)
        # 重置游戏统计信息
        stats.reset_stats()
        stats.game_active = True
        # 重置记分牌图像
        sb.prep_score
        sb.prep_level
        sb.prep_high_score()
        sb.prep_ships()
        # 清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()
        # 创建一群新外星人， 并让飞船居中
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()


def check_events(ai_settings, screen, ship, aliens, bullets, stats, play_button, sb):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        # 退出事件
        if event.type == pygame.QUIT:
            sys.exit()
        # 按键事件
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(ai_settings, screen, ship, aliens, bullets, stats, play_button, mouse_x, mouse_y, sb)

#-----------------------------------------------------------
#                  更新屏幕显示函数
#-----------------------------------------------------------
def update_screen(ai_settings, screen, ship, sky, aliens, bullets, stats, play_button, sb):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环都重绘背景、飞船、外星人
    # screen.fill(ai_settings.bg_color)
    sky.blitme()
    ship.blitme()
    # 绘制外星人群
    aliens.draw(screen)
    # 在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # 显示得分
    sb.show_score()
    # 如果游戏处于非活动状态，就绘制Play按钮
    if not stats.game_active:
        play_button.draw_button()
    # 让最近绘制的屏幕可见
    pygame.display.flip()


def update_bullets(aliens, bullets, ai_settings, screen, ship, stats, sb):
    """更新子弹状态"""
    # 更新子弹运动后的位置
    bullets.update()
    # 删除已经消失的子弹(遍历副本,控制原本)
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets, stats, sb)
    # 发射子弹:创建一个新子弹，并加入编组bullets中
    if (ship.fire == True) and (len(bullets) < ai_settings.bullets_allowed):
        if ((ai_settings.timer % ai_settings.bullet_interval) == 0):
            new_bullet = Bullet(ai_settings, screen, ship)
            bullets.add(new_bullet)

def check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets, stats, sb):
    """响应子弹击中外星人"""
    # 检查是否有子弹击中了外星人，并删除被击中的，Ture表示删除对应的满足条件的元素单位，不删除则为False
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats, sb)
    if len(aliens) == 0:
        # 一波击杀完成，删除现有的子弹，加快节奏，并新建外星人群
        bullets.empty()
        ai_settings.increase_speed()
        # 提高等级
        stats.level += 1
        sb.prep_level()
        # 新外星人群
        create_fleet(ai_settings, screen, ship, aliens)

#-----------------------------------------------------------
#                   创建外星人群的函数
#-----------------------------------------------------------
def create_fleet(ai_settings, screen, ship, aliens):
    """创建外星人群"""
    # 创建一个外星人，并计算一行可容纳数量
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    # 创建外星人群, 随机行、随机列
    for row_number in random.sample(range(0, number_rows + 1), random.randint(1, number_rows)):
        for alien_number in random.sample(range(0, number_aliens_x + 1), random.randint(1, number_aliens_x)):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)

def get_number_aliens_x(ai_settings, alien_width):
    """计算一行可容纳多少个外星人，外星人间距为外星人宽度的一半"""
    available_space_x = ai_settings.screen_width - alien_width
    number_aliens_x = int(available_space_x / (1.5 * alien_width))
    return number_aliens_x

def get_number_rows(ai_settings, ship_height, alien_height):
    """计算屏幕可容纳多少行外星人"""
    available_space_y = (ai_settings.screen_height - (2 * alien_height) - ship_height)
    number_rows = int(available_space_y / (1.5 * alien_height))
    return number_rows

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """创建一个外星人并将其加入到当前位置"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = (alien_width / 2) + (1.5 * alien_width * alien_number)
    alien.rect.centerx = alien.x
    alien.rect.centery = 0.5 * alien.rect.height + 1.5 * alien.rect.height * row_number
    # 加入到编组aliens中
    aliens.add(alien)

#-----------------------------------------------------------
#                   控制外星人移动的函数
#-----------------------------------------------------------
def check_fleet_edges(ai_settings, aliens):
    """检测每个外星人是否到达边界"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, alien)

def change_fleet_direction(ai_settings, alien):
    """外星人下移动，改变方向"""
    # for alien in aliens.sprites():
    alien.rect.y += ai_settings.fleet_drop_speed
    alien.direction *= -1

def update_aliens(ai_settings, stats, screen, ship, aliens, bullets, sb):
    """利用编组使用alien对象的方法，更新所有外星人的位置"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    # 检查外星人是否与飞船相撞
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets, sb)

def ship_hit(ai_settings, stats, screen, ship, aliens, bullets, sb):
    """响应被外星人撞到的飞船"""
    if stats.ships_left > 0:
        # 将ships_left减1
        stats.ships_left -= 1
        # 更新计分牌
        sb.prep_ships()
        # 清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()
        # 创建一群新外星人，并将飞船置于初始位置
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
        # 暂停一下
        sleep(0.5)
    else:
        stats.game_active = False
        # 光标重新可见
        pygame.mouse.set_visible(True)

#-----------------------------------------------------------
#                   检查是否诞生了最高分
#-----------------------------------------------------------
def check_high_score(stats, sb):
    """ 检查是否诞生了新的最高得分 """
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()

