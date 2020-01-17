############################################################################# ##
# Copyright (C) 2019-2020 Cameo Communications, Inc.
############################################################################# ##
#
# --------------------------------------------------------------------------
#     AUTHOR                   : EExuke
#     FILE NAME                : 2_guestes.py
#     FILE DESCRIPTION         : Python file
#     FIRST CREATION DATE      : 2020/01/06
# --------------------------------------------------------------------------
#     Version                  : 1.0
#     Last Change              : 2020/01/06
## ************************************************************************** ##
#
guestes = ['EExuke', 'jariy Gu', 'Jack Cheng',]
invite = "hi " + guestes[0] + ", please come to dinner with me!"
print (invite)
invite = "hi " + guestes[1] + ", please come to dinner with me!"
print (invite)
invite = "hi " + guestes[2] + ", please come to dinner with me!"
print (invite)
#####################################################################
print ("Sorry,", guestes[2], "is in guangzhou now!")
guestes[2] = 'Cai Cai'
invite = "hi " + guestes[2] + ", please come to dinner with me!"
print (invite)
#####################################################################
print ("There has a bigger table, so I can invite more friends!")
guestes.insert(0, 'Zhang Xu')
guestes.insert(2, 'Han Han')
guestes.append('Jie Guang')
for guest in guestes :
    print ("hi", guest, "welcome to my party!")
#####################################################################
print ("now can only invite two friends!")
guest = guestes.pop()
print ("Sorry,", guest)
guest = guestes.pop()
print ("Sorry,", guest)
guest = guestes.pop()
print ("Sorry,", guest)
guest = guestes.pop()
print ("Sorry,", guest)
for guest in guestes :
    print ("hi", guest, "welcome to my party!")
#####################################################################
del guestes[1]
guestes.remove('Zhang Xu')
print (str(len(guestes)))
