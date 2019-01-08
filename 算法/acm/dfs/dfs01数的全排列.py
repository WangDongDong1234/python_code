"""
深度优先搜索的思想：
关键在于解决当下改如何做，至于下一步如何做则与当下改如何做是一样的
基本模板
void dfs(int step)
    #1.判断边界（满足边界条件的话记得最后返回最后一次调用dfs的地方）
    #2.尝试每一种可能
    for i in range(1,n+1):
        3.继续下一步
        dfs(step+1）
        4.取消当前操作

    #5返回
"""

#计算数的全排列
n=int(input())
#盒子
box=[0 for i in range(0,n+1)]
#标记
book=[0 for i in range(0,n+1)]
sum=0
#step表示当前在那个盒子面前，准备向编号为step的盒子里放
def dfs(step):
    if step==n+1:
        global sum
        sum+=1
        for i in range(1,n+1):
            print(box[i],end=" ")
        print()
        return   #返回到之前的一步（即最后一次调用dfs函数的地方）注意 参考书这里不加return的话会无休止的执行下去为啥
    for i in range(1,n+1):
        if book[i]==0:
            box[step]=i
            book[i]=1
            dfs(step+1)
            book[i]=0



dfs(1)
print(sum)
