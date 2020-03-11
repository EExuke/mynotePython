############################################################################# ##
# Copyright (C) 2019-2011 Cameo Communications, Inc.
############################################################################# ##
#
# --------------------------------------------------------------------------
#     AUTHOR                   : EExuke
#     FILE NAME                : scatter_squares.py
#     FILE DESCRIPTION         : Python file
#     FIRST CREATION DATE      : 2020/03/11
# --------------------------------------------------------------------------
#     Version                  : 1.0
#     Last Change              : 2020/03/11
## ************************************************************************** ##
#

import matplotlib.pyplot as plt

# --------------------------------------------------------------------------
#     散点图
# --------------------------------------------------------------------------
# 点的坐标与尺寸
# plt.scatter(2, 4, s=10)
# --------------------------------------------------------------------------
# 简单散点列表
# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]
# plt.scatter(x_values, y_values, s=100)
# --------------------------------------------------------------------------
# 计算散点值
x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]
# edgecolor指定轮廓颜色，c指定点的颜色;可使用RGB配色：c=(0, 0, 8)
# plt.scatter(x_values, y_values, c='red', edgecolor='none', s=2)
# 使用颜色映射：
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor='none', s=2)
# --------------------------------------------------------------------------


# 设置图表标题并给坐标轴加上标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
# 设置刻度标记的大小
plt.tick_params(axis='both', which='major', labelsize=14)
# 设置每个坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])

# 保存; 路径/文件名; 第二个参数为“裁剪多余空白”,可省略
plt.savefig('../squares_plot.png', bbox_inches='tight')
# 显示
plt.show()

