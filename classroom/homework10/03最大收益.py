"""
第一排列顺序是收益  第二排列顺序是截至
思想是截至日期越靠后的尽量最后做，先做收益最大且截至日期靠前的
"""
n=int(input())

for i in range(n):
    num = int(input())
    id_deadline_profit_str = input().strip()
    id_deadline_profit1 = [int(item) for item in id_deadline_profit_str.split(' ')]
    id_deadline_profit = []
    for i in range(num):
        tmp = []
        tmp.append(id_deadline_profit1[3 * i])
        tmp.append(id_deadline_profit1[3 * i + 1])
        tmp.append(id_deadline_profit1[3 * i + 2])
        id_deadline_profit.append(tmp)
    # print(id_deadline_profit)

    id_deadline_profit.sort(key=lambda item: item[1])
    max_deadline = id_deadline_profit[len(id_deadline_profit) - 1][1]
    # print(max_deadline)
    id_deadline_profit.sort(key=lambda item: item[2], reverse=True)
    #print(id_deadline_profit)
    i = 1
    sum = 0
    total = 0

    # while i<=max_deadline:
    #     for item in id_deadline_profit:
    #         if i<=item[1]:
    #             total+=1
    #             sum+=item[2]
    #             break
    #     i+=1
    for item in id_deadline_profit:
        if i <= max_deadline:
            if i <= item[1]:
                total += 1
                sum += item[2]
                i += 1
    print(total, sum)



