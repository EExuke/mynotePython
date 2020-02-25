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
requested_toppings = []
if requested_toppings :
    for requested_topping in requested_toppings :
        print("Adding " + requested_topping + ".")
    print("finished make ! \n")
else :
    print("Are you sure you want a plain pizza? \n")
print("example end")
# 5_8 #
users = ['admin', 'root', 'EExuke', 'xuke', 'iceke']
if users :
  for user in users :
      if (user == 'admin') :
          print("Hello " + user + ", would you like to see a status report?")
      else :
          print("Hello " + user + ", thank you for logging in agin!") 
else :
  print("we need to find some users!")
print("5_8 end \n")

# 5_10 #
current_users = ['amdin', 'root', 'EExuke', 'xuke', 'iceke']
new_usrs = ['amdin', 'root', 'guest']
for user in new_usrs :
    if user.lower() in current_users :
        print("the name '" + user + "' has exist! please change..")
    else :
        print("the name '" + user + "' is ok!")
print("5_10 end")

# 5_11 #
numbs = range(1,10)
for numb in numbs :
    if (numb == 1) :
        print(str(numb) + "st")
    elif (numb == 2) :
        print(str(numb) + "nt")
    elif (numb == 3) :
        print(str(numb) + "rt")
    else :
        print(str(numb) + "th")
print("5_11 end")