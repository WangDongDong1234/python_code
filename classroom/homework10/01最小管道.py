
n=int(input())

for i in range(n):
    house_line_str = input().strip()
    house_line = [int(item) for item in house_line_str.split(' ')]
    house = house_line[0]
    line = house_line[1]
    # 表示房子的进出情况
    state = []
    for i in range(house):
        # 出 进  装什么(2表示水箱，3表示水龙头)
        tmp = [0, 0, 0]
        state.append(tmp)
    # 保存各个房间和管道信息
    array = []
    for i in range(line):
        start_end_length_str = input().strip()
        start_end_length = [int(item) for item in start_end_length_str.split(' ')]
        array.append(start_end_length)
        # 出
        start = start_end_length[0]
        # 进
        end = start_end_length[1]
        state[start - 1][0] = 1
        state[end - 1][1] = 1

    # 水龙头
    a = 0
    # 水箱
    b = 0
    resutlt1 = []
    restult2 = []
    restult3 = []
    for i in range(len(state)):
        if state[i][0] == 0 and state[i][1] == 1:
            state[i][2] = 3
            a += 1
            # 装水龙头的房间
            resutlt1.append(i + 1)
        elif state[i][0] == 1 and state[i][1] == 0:
            state[i][2] = 2
            b += 1
            # 装水箱的房间
            restult2.append(i + 1)
        else:
            # 什么也不装的房间
            restult3.append(i + 1)
    # print(resutlt1,restult2,restult3)#[1, 6, 8] [2, 3, 5] [4, 7, 9]
    # print(array)#[[7, 4, 98], [5, 9, 72], [4, 6, 10], [2, 8, 22], [9, 7, 17], [3, 1, 66]]
    r1 = []
    r2 = []
    for item in array:
        if item[0] in restult2 and item[1] in resutlt1:
            r1.append(item)
        else:
            r2.append(item)
    r2.sort(key=lambda item: item[2])
    # print(r1)[[2, 8, 22], [3, 1, 66]]
    # print(r2)[[4, 6, 10], [9, 7, 17], [5, 9, 72], [7, 4, 98]]
    for item in r1:
        print(item[0], item[1], item[2])
    short = r2[0][2]
    out_o = []
    in_i = []
    for item in r2:
        out_o.append(item[0])
        in_i.append(item[1])
    same = []
    for item in out_o:
        if item in in_i:
            same.append(item)
    for item in same:
        out_o.remove(item)
        in_i.remove(item)
    print(out_o[0], in_i[0], short)


