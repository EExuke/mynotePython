############################################################################# ##
# Copyright (C) 2019-2020 Cameo Communications, Inc.
############################################################################# ##
#
# --------------------------------------------------------------------------
#     AUTHOR                   : EExuke
#     FILE NAME                : 3_error.py
#     FILE DESCRIPTION         : Python file
#     FIRST CREATION DATE      : 2020/02/12
# --------------------------------------------------------------------------
#     Version                  : 1.0
#     Last Change              : 2020/02/12
## ************************************************************************** ##

#-----------------------------------------------------------
#                  MAIN PROCESS
#-----------------------------------------------------------
# ZeroDivisionError异常处理
try :
    print(5/0)
except ZeroDivisionError :
    print("You can not divide by 0 !")

# try-except-else 结构
print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.\n")

while True :
    first_number = input("\nFirst number: ")
    if first_number == 'q' :
        break
    second_number = input("\nSecond number: ")
    try :
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError :
        print("You can not divide by 0 !")
    else :
        print(answer)

#-----------------------------------------------------------
# 分析文本
title = "Alice in Wonderland"
words = title.split()
print(words)
num_words = len(words)
print("It's has " + str(num_words) + " words.")

#-----------------------------------------------------------
# 异常时沉默跳过
try :
    print(5/0)
except ZeroDivisionError :
    pass

#-----------------------------------------------------------
# 10_6
print("Enter two numbers, I'll sum them.")
print("Enter 'q' to quit.")

while True :
    first_number = input("\nEnter first number: ")
    if first_number == 'q' :
        break
    second_number = input("\nEnter second number: ")
    if second_number == 'q' :
        break
    try :
        answer = int(first_number) + int(second_number)
    except ValueError :
        print("You can only enter numbers!")
    else :
        print("the answer is: " + str(answer) + "\n")

#-----------------------------------------------------------
# count()用法
line = "EExuke, is embaded engneer xuke, and XuKe is me."
print(line.count('xuke'))
print(line.lower().count('xuke'))

