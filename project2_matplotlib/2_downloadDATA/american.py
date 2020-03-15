############################################################################# ##
# Copyright (C) 2019-2020 Cameo Communications, Inc.
############################################################################# ##
#
# --------------------------------------------------------------------------
#     AUTHOR                   : EExuke
#     FILE NAME                : american.py
#     FILE DESCRIPTION         : Python file
#     FIRST CREATION DATE      : 2020/03/14
# --------------------------------------------------------------------------
#     Version                  : 1.0
#     Last Change              : 2020/03/14
## ************************************************************************** ##

import pygal_maps_world.maps

#-----------------------------------------------------------
#                  Worldmap()演示
#-----------------------------------------------------------
# 创建Worldmap类型的实例
wm = pygal_maps_world.maps.World()
# wm图表标题
wm.title = 'North, Central, and South America'
# add()方法接收一个标签和一个列表或字典，为要突出的国家
wm.add('North America', {'ca': 34126000, 'us': 309349000, 'mx': 113423000})
# 每一次调用add() 方法都使用不同的颜色
wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('South America', ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf', 'gy', 'pe', 'py', 'sr', 'uy', 've'])

# 渲染为图像文件
wm.render_to_file('./americas.svg')

