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
result = []  # 深度访问结果
global start
for i in range(len(nodes)):
    if nodes[i] == startNode:
        start = i
        break
print("start-index",start)
# def dfs(current,result,book):
#     if len(result)==numNode:
#         print(result)
#         return
#     result.append(nodes[current])
#     book[current]=1
#     for j in range(1,numNode+1):
#         if array[current][j]==1 and book[j]==0:
#             new_result=copy.deepcopy(result)
#             new_book=copy.deepcopy(book)
#             dfs(j,new_result,new_book)
#
# dfs(start,result,book)

result.append(nodes[start])
book[start]=1
def dfs(current,result,book):
    if len(result)==numNode:
        print(result)
        return
    for j in range(1,numNode+1):
        if array[current][j]==1 and book[j]==0:
            new_result = copy.deepcopy(result)
            new_book=copy.deepcopy(book)
            new_result.append(nodes[j])
            new_book[j]=1
            dfs(j,new_result,new_book)
dfs(start,result,book)