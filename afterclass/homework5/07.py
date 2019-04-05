n=int(input())

for i in range(n):
    numNode_startNode_str = input().strip()
    numNode_startNode = [item for item in numNode_startNode_str.split(' ')]
    numNode = int(numNode_startNode[0])
    startNode = numNode_startNode[1]
    nodes_str = input().strip()
    nodes = [item for item in nodes_str.split(' ')]
    nodes.insert(0, ' ')
    array = []
    for i in range(numNode + 1):
        if i == 0:
            tmp = []
            for j in range(numNode + 1):
                tmp.append(0)
            array.append(tmp)
        else:
            tmp_str = input().strip()
            tmp = [int(item) for item in tmp_str.split(' ')[1:]]
            tmp.insert(0, nodes[i])
            array.append(tmp)
    # print(array)
    book = []  # 标记是否访问
    for i in range(numNode + 1):
        book.append(0)
    # print(book)
    result = []  # 深度访问结果
    global start
    for i in range(len(nodes)):
        if nodes[i] == startNode:
            start = i
            break
    # print(start)
    result = []
    # 队列存放深度遍历的点
    team = []
    team.append(start)
    book[start] = 1
    # print(team)
    while len(team) != 0:
        current = team.pop(0)
        result.append(current)
        for j in range(1, numNode + 1):
            if array[current][j] == 1 and book[j] == 0:
                book[j] = 1
                team.append(j)
    for i in range(numNode):
        if i == 0:
            print(nodes[result[i]], end='')
        else:
            print('', nodes[result[i]], end='')
    print()
