############################################################################# ##
# Copyright (C) 2019-2020 Cameo Communications, Inc.
############################################################################# ##
#
# --------------------------------------------------------------------------
#     AUTHOR                   : EExuke
#     FILE NAME                : python_repos.py
#     FILE DESCRIPTION         : Python file
#     FIRST CREATION DATE      : 2020/03/15
# --------------------------------------------------------------------------
#     Version                  : 1.0
#     Last Change              : 2020/03/15
## ************************************************************************** ##

import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

#-----------------------------------------------------------
#                  找出github上星级最高的python项目
#-----------------------------------------------------------

# 执行 API 调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
# 显示响应结果
print("Status code:", r.status_code)

# 将 API 响应存储在一个变量中
response_dict = r.json()
print("Total repositories:", response_dict['total_count'])

# 探索有关仓库的信息
repo_dicts = response_dict['items']
print("Repositories returned:", len(repo_dicts))

# 研究有关仓库的指定信息
#repo_dict = repo_dicts[0]
# print("\nKeys:", len(repo_dict))
# for key in sorted(repo_dict.keys()):
#     print(key)

# 打印查看每个项目仓库的信息：
#index = 0
#print("\nSelected information about each repository:")
#for repo_dict in repo_dicts:
    #index += 1
    #print("\nSelected information about " + str(index) + " repository:")
    #print('Name:', repo_dict['name'])
    #print('Owner:', repo_dict['owner']['login'])
    #print('Stars:', repo_dict['stargazers_count'])
    #print('Repository:', repo_dict['html_url'])
    #print('Created:', repo_dict['created_at'])
    #print('Updated:', repo_dict['updated_at'])
    #print('Description:', repo_dict['description'])

names, stars = [], []
for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    # 自定义工具提示标签
    plot_dict = {
            'value': repo_dict['stargazers_count'],
            'label': repo_dict['description'],
            'xlink': repo_dict['html_url'],
            }
    plot_dicts.append(plot_dict)

# 可视化
my_style = LS('#333366', base_style=LCS)

my_config = pygal.Config()        # 创建配置类型的实例
my_config.x_label_rotation = 45   # x轴旋转45度
my_config.show_legend = False     # 隐藏图例
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15     # 将较长的标签缩短为15个字符
my_config.show_y_guides = False   # 隐藏水平线
my_config.width = 1000

# 绘制图表
chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Most-Starred Python Projects on GitHub'
chart.x_labels = names
chart.add('', stars)
chart.render_to_file('./python_repos.svg')


