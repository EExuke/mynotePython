############################################################################# ##
# Copyright (C) 2019-2011 Cameo Communications, Inc.
############################################################################# ##
#
# --------------------------------------------------------------------------
#     AUTHOR                   : EExuke
#     FILE NAME                : highs_lows.py
#     FILE DESCRIPTION         : Python file
#     FIRST CREATION DATE      : 2020/03/12
# --------------------------------------------------------------------------
#     Version                  : 1.0
#     Last Change              : 2020/03/12
## ************************************************************************** ##
#

import csv
from matplotlib import pyplot as plt
from datetime import datetime

# --------------------------------------------------------------------------
# 从文件中获取最高气温
# --------------------------------------------------------------------------
filename = 'sitka_weather_07-2014.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # 打印文件抬头信息
    #for index, column_header in enumerate(header_row):
        #print(index, column_header)

    # 列表存储读取的数据
    dates, highs, lows = [], [], []

    # 遍历余下各行
    for row in reader:
        try:
            # 读取第0列，并转换为数字成日期格式
            current_date = datetime.strptime(row[0], "%Y/%m/%d")
            # 读取第1列，并转换为数字
            high = int(row[1])
            # 读取第3列，并转换为数字
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing data')
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)


# --------------------------------------------------------------------------
# 根据数据绘制图形
# --------------------------------------------------------------------------
fig = plt.figure(dpi=128, figsize=(10, 5.2))
plt.plot(dates, highs, c='red')
plt.plot(dates, lows, c='blue')
# 给图标区域着色，实参alpha为透明度,0.5为不透明
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# 设置图形的格式
plt.title("Daily high and low temperatures, July 2014", fontsize=20)
plt.xlabel('Time', fontsize=16)
# 自动避免标签重叠
fig.autofmt_xdate()
plt.ylabel("Temperature (F)", fontsize=16)
plt.tick_params(axis='both', which='major', labelsize=16)

# 显示
plt.show()

