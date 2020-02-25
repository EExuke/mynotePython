############################################################################# ##
# Copyright (C) 2019-2020 Cameo Communications, Inc.
############################################################################# ##
#
# --------------------------------------------------------------------------
#     AUTHOR                   : EExuke
#     FILE NAME                : 5_tuples.py
#     FILE DESCRIPTION         : Python file
#     FIRST CREATION DATE      : 2020/01/17
# --------------------------------------------------------------------------
#     Version                  : 1.0
#     Last Change              : 2020/01/17
## ************************************************************************** ##
#
# 5_1 & 5_2 #
car = 'Jili'
print(car == 'Auto')
print(car == 'Jili')

print((car.lower() == 'jili') and (car != 'Auto'))
print((car.lower() == 'bmw') or (car != 'Auto'))

numbs = range(1,10)
numb = 7
if numb in numbs :
    print(str(numb) + " in numb list \n")

numb = 77
if numb not in numbs :
    print(str(numb) + " not in numbs list \n")

