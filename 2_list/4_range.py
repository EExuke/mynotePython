############################################################################# ##
# Copyright (C) 2019-2011 Cameo Communications, Inc.
############################################################################# ##
#
# --------------------------------------------------------------------------
#     AUTHOR                   : EExuke
#     FILE NAME                : 4_range.py
#     FILE DESCRIPTION         : Python file
#     FIRST CREATION DATE      : 2020/01/07
# --------------------------------------------------------------------------
#     Version                  : 1.0
#     Last Change              : 2020/01/07
## ************************************************************************** ##
#
for i in range(1,21) :
    print (i)

numbers = range(1,1000001)
# for number in numbers :
#     print (number)
print (min(numbers))
print (max(numbers))
print (sum(numbers))

nums = list(range (1, 20, 2))
for num in nums :
    print (num)

nums = list(range (3, 30, 3))
for num in nums :
    print (num)

######### 乘方 ** #######
nums = list(range (1, 10))
for num in nums :
    result = num**3
    print (result)

squear = [ val**3 for val in range(1, 10)]
print (squear)
###############切片################
print(nums)
print("there are first three nums:",nums[:3])
print("there are last three nums:",nums[-3:])

