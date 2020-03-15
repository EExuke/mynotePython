############################################################################# ##
# Copyright (C) 2019-2020 Cameo Communications, Inc.
############################################################################# ##
#
# --------------------------------------------------------------------------
#     AUTHOR                   : EExuke
#     FILE NAME                : bar_desc.py
#     FILE DESCRIPTION         : Python file
#     FIRST CREATION DATE      : 2020/03/15
# --------------------------------------------------------------------------
#     Version                  : 1.0
#     Last Change              : 2020/03/15
## ************************************************************************** ##

#-----------------------------------------------------------
#                  MAIN PROCESS
#-----------------------------------------------------------
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
my_style = LS('#333366', base_style=LCS)
chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'Python Projects'
chart.x_labels = ['httpie', 'django', 'flask']

plot_dicts = [
        {'value': 16101, 'label': 'Description of httpie.'},
        {'value': 15028, 'label': 'Description of django.'},
        {'value': 14798, 'label': 'Description of flask.'},
        ]
chart.add('', plot_dicts)
chart.render_to_file('bar_descriptions.svg')

