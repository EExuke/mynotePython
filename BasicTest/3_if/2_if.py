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
# 5_3 & 5_4 & 5_5 #
color = ['green', 'yellow', 'red']
alien_color = 'red'

if alien_color == color[0] :
    print("alien_color is " + color[0])
elif alien_color == color[1] :
    print("alien_color is " + color[1])
elif alien_color == color[2] :
    print("alien_color is " + color[2])
else :
    print("do not have this aliem_color")

# 5_6 #
stages = ['baby', 'groping', 'child', 'teen', 'man', 'oldman']
age = 18
print("there is a man age of " + str(age) + "\n")
if (age < 2 ) :
    print("he is a " + stages[0])
elif ((age >= 2) and (age < 4)) :
    print("he is a " + stages[1])
elif ((age >= 4) and (age < 13)) :
    print("he is a " + stages[2])
elif ((age >= 13) and (age < 20)) :
    print("he is a " + stages[3])
elif ((age >= 20) and (age < 65)) :
    print("he is a " + stages[4])
else :
    print("he is a " + stages[5])