############################################################################# ##
# Copyright (C) 2019-2020 Cameo Communications, Inc.
############################################################################# ##
#
# --------------------------------------------------------------------------
#     AUTHOR                   : EExuke
#     FILE NAME                : game_stats.py
#     FILE DESCRIPTION         : Python file
#     FIRST CREATION DATE      : 2020/03/01
# --------------------------------------------------------------------------
#     Version                  : 1.0
#     Last Change              : 2020/03/01
## ************************************************************************** ##

#-----------------------------------------------------------
#                  统计游戏数据
#-----------------------------------------------------------
class GameStats():
    """跟踪游戏的统计信息"""
    def __init__(self, ai_settings):
        """初始化统计信息"""
        self.ai_settings = ai_settings
        self.reset_stats()
        # 最高分
        self.high_score = 0
        # 游戏刚开始时处于非活跃状态
        self.game_active = False

    def reset_stats(self):
        """初始化游戏运行期间变化的统计信息"""
        self.ships_left = self.ai_settings.ships_limit
        self.score = 0
        self.level = 1

