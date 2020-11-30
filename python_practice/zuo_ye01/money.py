saved_money = 1000


# 发工资模块，用来增加收入计算
def send_money():
    print("发工资")
    global send_money
    send_money = 2000


# 工资查询模块，用来展示工资数额
def select_money():
    if send_money == 2000:
        print(f"存款金额为:{send_money}")
    else:
        print("存款金额为：1000")


# 启动文件展示最终存款金额
if __name__ == '__main__':
    send_money()
    select_money()
