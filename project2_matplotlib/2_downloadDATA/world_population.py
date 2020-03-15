############################################################################# ##
# Copyright (C) 2019-2020 Cameo Communications, Inc.
############################################################################# ##
#
# --------------------------------------------------------------------------
#     AUTHOR                   : EExuke
#     FILE NAME                : world_population.py
#     FILE DESCRIPTION         : Python file
#     FIRST CREATION DATE      : 2020/03/14
# --------------------------------------------------------------------------
#     Version                  : 1.0
#     Last Change              : 2020/03/14
## ************************************************************************** ##

import json
import pygal_maps_world.maps

from country_code import get_country_code
from pygal.style import RotateStyle
from pygal.style import LightColorizedStyle as LCS

#-----------------------------------------------------------
#                  绘制世界人口地图
#-----------------------------------------------------------
# 将数据加载到一个列表中（列表中每个成员为一个字典）
filename = 'population_data.json'
with open(filename) as f:
    pop_data = json.load(f)

# 创建包含人口信息的字典
cc_populations = {}
for pop_dict in pop_data:
    if pop_dict['Year'] == '2010':
        country_name = pop_dict['Country Name']
        # 字符串格式转换为数字格式
        population = int(float(pop_dict['Value']))
        code = get_country_code(country_name)
        if code:
            cc_populations[code] = population
        else:
            code = pop_dict['Country Code']
            print("no code of " + code + " of " + country_name + " in COUNTRIES")

# 根据人口数量将字典分组
cc_pops_1, cc_pops_2, cc_pops_3 = {}, {}, {}
for cc, pop in cc_populations.items():
    if pop < 10000000:
        cc_pops_1[cc] = pop
    elif pop < 1000000000:
        cc_pops_2[cc] = pop
    else:
        cc_pops_3[cc] = pop
# 看看每组分别包含多少个国家
print(len(cc_pops_1), len(cc_pops_2), len(cc_pops_3))

# 根据指定基色(#336699)绘制地图, 并加亮颜色
wm_style = RotateStyle('#993322', base_style=LCS)
wm = pygal_maps_world.maps.World(style = wm_style)
wm.title = 'World Population in 2010, by Country'
# 将各组键值分别加入图表中
wm.add('>1bn', cc_pops_3)
wm.add('10m-1bn', cc_pops_2)
wm.add('0-10m', cc_pops_1)
#wm.add('2010', cc_populations)

# 渲染成文件
wm.render_to_file('./world_population.svg')

