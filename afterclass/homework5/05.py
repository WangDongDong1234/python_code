#求最大遍历深度
"""
n测试案例个数
num_node结点个数
start_node开始结点
start_node_index开始结点下标
new_nodes_str新的结点格式中间没有空格
"""
import copy
n=int(input())

start=input().strip().split(' ')
#结点个数
num_node=int(start[0])
#开始结点
start_node=start[1]
#结点
nodes_str=input().strip()
nodes=[item for item in nodes_str.split(' ')]
new_nodes_str=''.join(nodes)
#开始结点的下标
start_node_index=new_nodes_str.find(start_node)+1
#图的矩阵
array=[]
for i in range(0,num_node):
    tmp_str=input().strip()[2:]
    tmp=[int(item) for item in tmp_str.split(' ')]
    array.append(tmp)
print(array)
for i in range(0,num_node+1):
    if i==0:
        tmp=[]
        for j in range(0,num_node+1):
            tmp.append(0)
        array.insert(0,tmp)
    else:
        array[i].insert(0,0)
print(array)
book=[]#标记哪些点走过
for i in range(0,num_node+1):
    book.append(0)
path=copy.deepcopy(book)#记录路径

def dfs(current,step):
    if step==num_node:
        print(path)
        return
    for j in range(1,num_node+1):
        if book[j]==0 and array[current][j]==1:
            path[j]=step
            book[j]=1
            dfs(j,step+1)
            book[j]=0
book[start_node_index]=1
dfs(start_node_index,1)












