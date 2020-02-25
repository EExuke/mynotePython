############################################################################# ##
# Copyright (C) 2019-2020 Cameo Communications, Inc.
############################################################################# ##
#
# --------------------------------------------------------------------------
#     AUTHOR                   : EExuke
#     FILE NAME                : 3_funcReturn.py
#     FILE DESCRIPTION         : Python file
#     FIRST CREATION DATE      : 2020/02/09
# --------------------------------------------------------------------------
#     Version                  : 1.0
#     Last Change              : 2020/02/09
## ************************************************************************** ##

#-----------------------------------------------------------
#                  MAIN PROCESS
#-----------------------------------------------------------
# 8_6
def city_country(city, country) :
    """返回组合字符串"""
    str = city + ', ' + country
    return str

print(city_country('Chengdu', 'China') + "\n")

#-----------------------------------------------------------
# 8_7
def make_album(singer, album) :
    """返回保存专辑的字典"""
    albums = {singer:album,}
    return albums

albums  = make_album('XuSong', '《In Dream》')
print(albums)

#-----------------------------------------------------------
# 8_8
while True :
    singer = input("\n请输入歌手姓名(0退出)：")
    if singer == '0' :
        break
    album = input("\n请输入专辑名(0退出)：")
    if singer == '0' :
        break
    albums  = make_album(singer, album)
    print(albums)

