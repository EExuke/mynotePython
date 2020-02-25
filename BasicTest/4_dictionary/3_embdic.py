############################################################################# ##
# Copyright (C) 2019-2020 Cameo Communications, Inc.
############################################################################# ##
#
# --------------------------------------------------------------------------
#     AUTHOR                   : EExuke
#     FILE NAME                : 3_embdic.py
#     FILE DESCRIPTION         : Python file
#     FIRST CREATION DATE      : 2020/02/07
# --------------------------------------------------------------------------
#     Version                  : 1.0
#     Last Change              : 2020/02/07
## ************************************************************************** ##

#-----------------------------------------------------------
#                  MAIN PROCESS
#-----------------------------------------------------------
# 例
aliens = []

for alien_number in range(30) :
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)

for alien in aliens[0:3] :
    if alien['color'] == 'green' :
        alien['color'] = 'yellow'
        alien['points'] = 10
        alien['speed'] = 'medium'

for alien in aliens[0:5] :
    print(alien)
print("...\n")

#-----------------------------------------------------------
# 6_7
persons = {
    'xuke' : {
        'first_name': 'xu',
        'last_name': 'ke',
        'age': '23',
        'city': 'chengdu',
        },
    'jaerygu' : {
        'first_name': 'jaery',
        'last_name': 'gu',
        'age': '23',
        'city': 'jiangyin',
        },
    'jackcheng' : {
        'first_name': 'jack',
        'last_name': 'cheng',
        'age': '23',
        'city': 'guangzhou',
        },
}


for name, info in persons.items() :
    print("\nname: " + name.title() )
    for k, v in info.items() :
        print(k + ": " + v)

