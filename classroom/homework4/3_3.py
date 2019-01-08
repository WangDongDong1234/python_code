n = int(input())
result = []
for i in range(0, n):
    huajia_muban=input().strip()
    huajia=huajia_muban.split(" ")[0]
    muban=huajia_muban.split(" ")[1]
    # huajia = int(input())
    # muban = int(input())
    str_muban = input()
    lst_muban = []
    tmp_muban = str_muban.strip().split(" ")
    for item in tmp_muban:
        lst_muban.append(int(item))
    if huajia >= muban:
        result.append(max(lst_muban))
        continue
    else:
        lst1 = lst_muban[:1]
        lst2 = lst_muban[1:]
        sum_time1 = sum(lst1)
        sum_time2 = sum(lst2)
        time = max(sum_time1, sum_time2)
        for s in range(2,4):
            lst1=lst_muban[:s]
            lst2=lst_muban[s:]
            sum_time1=sum(lst1)
            sum_time2= sum(lst2)
            tmp_time=max(sum_time1,sum_time2)
            if tmp_time<time:
                time=tmp_time
        result.append(time)
for item in result:
    print(item)



