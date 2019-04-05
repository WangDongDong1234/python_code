#求最大遍历深度
"""

"""
import copy
#测试用例个数
n=int(input())
#结点个数和起始节点
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
print(array)
book = []  # 标记是否访问
for i in range(numNode + 1):
    book.append(0)
print(book)
global start
for i in range(len(nodes)):
    if nodes[i] == startNode:
        start = i
        break
max=0
def dfs(begin):
    book[begin]=1
    max_tmp=1
    for j in range(1,len(book)):
        if array[begin][j]==1 and book[j]==0:
            max_tmp=dfs(j)+1
    global max
    if max_tmp>max:
        max=max_tmp
    return max_tmp
print(dfs(start))

