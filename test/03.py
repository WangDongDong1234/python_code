n_d_str=input().strip()
n_d=[int(item) for item in n_d_str.split(' ')]
n=n_d[0]
d=n_d[1]
array=[]
for i in range(n):
    tmp_str=input().strip()
    tmp=[int(item) for item in tmp_str.split(' ')]
    tmp.insert(0,i+1)
    array.append(tmp)
#print(n,d)
#print(array)
#抢的店铺
box=[]
for i in range(3):
    box.append(0)
#标记店铺
book=[]
for i in range(n+1):
    book.append(0)

sum=0
def dfs(step):
    if step==3:
        global sum
        if abs(array[box[1]-1][1]-array[box[2]-1][1])>=d:
            total=array[box[1]-1][2]+array[box[2]-1][2]
            if total>sum:
                sum=total
        return
    for i in range(1,n+1):
        if book[i]==0:
            book[i]=1
            box[step]=i
            dfs(step+1)
            book[i]=0
dfs(1)
print(sum)



