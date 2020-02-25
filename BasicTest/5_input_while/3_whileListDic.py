############################################################################# ##
# Copyright (C) 2019-2020 Cameo Communications, Inc.
############################################################################# ##
#
# --------------------------------------------------------------------------
#     AUTHOR                   : EExuke
#     FILE NAME                : 3_whileListDic.py
#     FILE DESCRIPTION         : Python file
#     FIRST CREATION DATE      : 2020/02/08
# --------------------------------------------------------------------------
#     Version                  : 1.0
#     Last Change              : 2020/02/08
## ************************************************************************** ##

#-----------------------------------------------------------
#                  MAIN PROCESS
#-----------------------------------------------------------
# 例
responses = {}

# 设置一个标志，指出调查是否结束
polling_active = True

while polling_active :
    # 提示输入
    name = input("\nWhat is your name? ")
    response = input("\nWhich nountain would you like? ")
    # 将答卷存储在字典中
    responses[name] = response
    # 判断是否继续调查
    repeat = input("\nWould you like to question next one?")
    if repeat == 'no' :
        polling_active = False
# 调查结束，显示结果
print("\n---Poll Result---")
for name, response in responses.items() :
    print(name + " Would like to climb " + response + ".")

#-----------------------------------------------------------
# 7_8
sandwich_orders = ['chiken', 'peigen', 'meal', 'pastrami', 'pastrami', 'pastrami']
finished_sanwich = []
while sandwich_orders :
    made = sandwich_orders.pop()
    print("I made your " + made + "sandwich.\n")
    finished_sanwich.append(made)

#-----------------------------------------------------------
# 7_9
print(finished_sanwich)
saleout = 'pastrami'
while saleout in finished_sanwich :
    finished_sanwich.remove(saleout)
print(finished_sanwich)



