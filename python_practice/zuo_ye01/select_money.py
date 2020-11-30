# 工资查询模块，用来展示工资数额

import money


def select_money():
    send_money = money.send_money
    if send_money == 2000:
        print(f"存款金额为:{send_money}")
    else:
        print("存款金额为：1000")
