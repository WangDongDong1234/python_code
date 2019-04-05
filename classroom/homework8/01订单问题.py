"""
描述



输入


•第一行包含一个整数，测试用例数。


•第二行包含三个整数n、x、y。


•第三行包含n个整数。第i个整数表示ai。


•第四行包含n个整数。第i个整数表示bi。


产量


打印一个整数，表示他们将收到的最大小费。
1  21  16
15 3 3
1 2 3 4 5
5 4 3 2 1
5 3 3
5 4 3 5 4
1 1 1 1 1

5 3 3
5 4 3 5 4
1 2 1 1 1  17
"""
n=int(input())
for i in range(n):
    input1_str = input().strip()
    input1 = [int(item) for item in input1_str.split(' ')]
    x = input1[1]
    y = input1[2]
    x_money_str = input().strip()
    x_money = [int(item) for item in x_money_str.split(' ')]
    x_money.insert(0, 0)
    y_money_str = input().strip()
    y_money = [int(item) for item in y_money_str.split(' ')]
    y_money.insert(0, 0)
    # print(x, y, x_money, y_money)
    task_nums = len(x_money) - 1
    dict_x = []
    dict_y = []
    for i in range(1, task_nums + 1):
        dict_x.append([i, x_money[i]])
    for i in range(1, task_nums + 1):
        dict_y.append([i, y_money[i]])
    dict_x.sort(key=lambda item: item[1], reverse=True)
    dict_y.sort(key=lambda item: item[1], reverse=True)
    box = []
    for i in range(task_nums + 1):
        box.append(0)
    sum = 0
    sum_money = 0
    i = 0
    j = 0
    while sum < task_nums:
        if dict_x[i][1] >= dict_y[j][1] and x > 0:
            if box[dict_x[i][0]] == 0:
                box[dict_x[i][0]] = 1
                sum_money += dict_x[i][1]
                i += 1
                x -= 1
                sum += 1
            else:
                i += 1
        elif dict_x[i][1] < dict_y[j][1] and y > 0:
            if box[dict_y[j][0]] == 0:
                box[dict_y[j][0]] = 2
                sum_money += dict_y[j][1]
                j += 1
                y -= 1
                sum += 1
            else:
                j += 1
        elif x == 0:
            if box[dict_y[j][0]] == 0:
                box[dict_y[j][0]] = 2
                sum_money += dict_y[j][1]
                j += 1
                y -= 1
                sum += 1
            else:
                j += 1
        elif y == 0:
            if box[dict_x[i][0]] == 0:
                box[dict_x[i][0]] = 1
                sum_money += dict_x[i][1]
                i += 1
                x -= 1
                sum += 1
            else:
                i += 1
    print(sum_money,box[1:])



