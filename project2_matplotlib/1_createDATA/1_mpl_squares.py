############################################################################# ##
# Copyright (C) 2019-2011 Cameo Communications, Inc.
############################################################################# ##
#
# --------------------------------------------------------------------------
#     AUTHOR                   : EExuke
#     FILE NAME                : mpl_squares.py
#     FILE DESCRIPTION         : Python file
#     FIRST CREATION DATE      : 2020/03/11
# --------------------------------------------------------------------------
#     Version                  : 1.0
#     Last Change              : 2020/03/11
## ************************************************************************** ##
#

import matplotlib.pyplot as plt

# --------------------------------------------------------------------------
#            绘制简单折线图
# --------------------------------------------------------------------------
inport_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]
plt.plot(inport_values, squares, linewidth = 5)

# 设置图表标题
plt.title("Square Numbers", fontsize = 24)
# 给坐标轴加标签
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Square of Value", fontsize=14)
# 设置刻度标记大小,both for x&y;刻度字号14;
plt.tick_params(axis='both', labelsize=14)

plt.show()
