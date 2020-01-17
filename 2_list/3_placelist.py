############################################################################# ##
# Copyright (C) 2019-2020 Cameo Communications, Inc.
############################################################################# ##
#
# --------------------------------------------------------------------------
#     AUTHOR                   : EExuke
#     FILE NAME                : 3_placelist.py
#     FILE DESCRIPTION         : Python file
#     FIRST CREATION DATE      : 2020/01/07
# --------------------------------------------------------------------------
#     Version                  : 1.0
#     Last Change              : 2020/01/07
## ************************************************************************** ##
#
place = ['Chengdu', 'Shanghai', 'Beijing', 'Guangzhou', 'HongKong']
print (place)
print (sorted(place))
print (place)

place.sort()
print (place)
place.sort(reverse=True)
print (place)

place.reverse()
print (place)

print (str(len(place)))
