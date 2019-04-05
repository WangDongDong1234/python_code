import copy
n=int(input())

num=int(input())
array=[]
for i in range(num):
    tmp_str=input().strip()
    tmp=[int(item) for item in tmp_str.split(' ')]
    array.append(tmp)


book=[]#标记
for i in range(num+1):
    book.append(0)
#表示第一个菜买第几家的
box=copy.deepcopy(book)

mix_money=999999
def dfs(index):
    global mix_money
    if index>num:
        sum=0
        for i in range(1,num+1):
            sum+=array[box[i]-1][i-1]
        if sum<mix_money:
            mix_money=sum
        return
    for i in range(1,num+1):
        if book[i]==0:
            book[i]=1
            box[index]=i
            dfs(index+1)
            book[i]=0
dfs(1)
print(mix_money)