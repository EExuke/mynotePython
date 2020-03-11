############################################################################# ##
# Copyright (C) 2019-2011 Cameo Communications, Inc.
############################################################################# ##
#
# --------------------------------------------------------------------------
#     AUTHOR                   : EExuke
#     FILE NAME                : random_walk.py
#     FILE DESCRIPTION         : Python file
#     FIRST CREATION DATE      : 2020/03/11
# --------------------------------------------------------------------------
#     Version                  : 1.0
#     Last Change              : 2020/03/11
## ************************************************************************** ##
#

from random import choice
import matplotlib.pyplot as plt

# --------------------------------------------------------------------------
#         随机漫步
# --------------------------------------------------------------------------
class RandomWalk():
    """一个生成随机漫步数据的类"""
    def __init__(self, num_points=5000):
        """ 初始化随机漫步的属性 """
        self.num_points = num_points
        # 所有随机漫步都始于 (0, 0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """ 计算随机漫步包含的所有点 """
        # 不断漫步,直到列表达到指定的长度
        while len(self.x_values) < self.num_points:
            # 决定前进方向以及沿这个方向前进的距离
            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance
            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance
            # 拒绝原地踏步
            if x_step == 0 and y_step == 0:
                continue
            # 计算下一个点的 x 和 y 值
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step
            self.x_values.append(next_x)
            self.y_values.append(next_y)

# 不断生成漫步结果：
while True:
    # 创建一个 RandomWalk 实例
    rw = RandomWalk(5000)
    # 生成漫步点
    rw.fill_walk()

    # 设置绘图窗口的尺寸
    plt.figure(figsize=(10, 6))
    # 用于颜色映射的点序列表：
    point_numbers = list(range(rw.num_points))
    # 将其包含的点都绘制出来
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=1)
    #plt.plot(rw.x_values, rw.y_values, linewidth=2)
    # 追加绘制，突出起点和终点
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    #plt.plot(0, 0, linewidth=2)
    #plt.plot(rw.x_values[-1], rw.y_values[-1], linewidth=2)
    # 隐藏坐标轴
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)

    # plt.savefig('../random_walk.png', bbox_inches='tight')  # 保存生成图
    plt.show()

    keep_running = input("是否继续生成下一幅？(y/n): ")
    if keep_running == 'n':
        break

