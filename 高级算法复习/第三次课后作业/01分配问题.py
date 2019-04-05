"""
分配问题
Description
对给定的n个任务与n个人之间的成本矩阵完成成本最低的任务分配策略。
Input
输入：第一行为用例个数，之后为每一个用例；用例的第一行为任务个数，即n；用例的第二行为使用逗号隔开的人员完成任务的成本；
每一个成本描述包括人员序号、任务序号和成本，使用空格隔开。人员序号和任务序号都是从1到n的整数，序号出现的次序没有固定规则。
Output
输出：每一个用例输出一行，从序号为1的人员开始，给出其分配的任务序号，使用空格隔开；使用逗号将多个解隔开。结果按照人员分配
的任务序号大小排，第一个人员的任务序号大的放在前面，如果相同则看第二个人员的任务，以此类推。

Sample Input 1

1
4
2 1 6,1 2 2,1 3 7,1 4 8,1 1 9,2 2 4,2 3 3,2 4 7,3 1 5,3 2 8,3 3 1,3 4 8,4 1 7,4 2 6,4 3 9,4 4 4
Sample Output 1

2 1 3 4
解法一：全排列
解法二：勾牙利


"""
n=int(input())
array_str=input().strip()
array_tmp=[item for item in array_str.split(',')]
print(array_tmp)
array=[]
for item in array_tmp:
    tmp=[]
    for e in item.strip("'").split(' '):
        tmp.append(int(e))
    array.append(tmp)
print(array)
cost_array=[]
m=int(len(array)/n)

for i in range(m+1):
    tmp=[]
    for j in range(n+1):
        tmp.append(0)
    cost_array.append(tmp)
for item in array:
    cost_array[item[0]][item[1]]=item[2]
book=[0 for i in range(n+1)]
box=[0 for i in range(n+1)]
min=9999999
result=[0 for i in range(n+1)]
def dfs(index):
    global min
    global result
    if index==n+1:
        cost=0
        for i in range(1,n+1):
            cost+=cost_array[i][box[i]]
        if cost<min:
            min=cost
            #result=box#指向的是同一个数组  box变了result也会变(严重注意)
            for i in range(n+1):
                result[i]=box[i]
        return
    for i in range(1,n+1):
        if book[i]==0:
            book[i]=1
            box[index]=i
            dfs(index+1)
            book[i]=0
dfs(1)
print(min,result)
