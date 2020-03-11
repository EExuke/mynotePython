############################################################################# ##
# Copyright (C) 2019-2020 Cameo Communications, Inc.
############################################################################# ##
#
# --------------------------------------------------------------------------
#     AUTHOR                   : EExuke
#     FILE NAME                : die.py
#     FILE DESCRIPTION         : Python file
#     FIRST CREATION DATE      : 2020/03/11
# --------------------------------------------------------------------------
#     Version                  : 1.0
#     Last Change              : 2020/03/11
## ************************************************************************** ##

import pygal
from random import randint

#-----------------------------------------------------------
#                  模拟骰子
#-----------------------------------------------------------
class Die():
    """ 表示一个骰子的类 """
    def __init__(self, num_sides=6):
        """ 骰子默认为 6 面 """
        self.num_sides = num_sides
    def roll(self):
        """" 返回一个位于 1 和骰子面数之间的随机值 """
        return randint(1, self.num_sides)

#-----------------------------------------------------------
#                  掷骰子
#-----------------------------------------------------------
# 创建2个die实例,可传递骰子面数
die_1 = Die()
die_2 = Die(6)

# 掷几次骰子,并将结果存储在一个列表中
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll()
    results.append(result)

#print(results)

# 分析结果
frequencies = []
for value in range(2, die_1.num_sides+die_2.num_sides+1):
    # 使用list的count方法统计
    frequency = results.count(value)
    frequencies.append(frequency)

#print(frequencies)

#-----------------------------------------------------------
#                   pygal.Bar()绘制直方图
#-----------------------------------------------------------
# 对结果进行可视化
hist = pygal.Bar()
# 设置图表的各属性
hist.title = "Results of rolling one D6 1000 times."
hist.x_labels = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
# 添加一系列值和值的标签
hist.add('D6 + D6', frequencies)
# 渲染为SVG文件
hist.render_to_file('/home/xuke/Pictures/die_visual.svg')


