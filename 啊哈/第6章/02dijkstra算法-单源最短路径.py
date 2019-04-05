"""
6 9
1 2 1
1 3 12
2 3 9
2 4 3
3 5 5
4 3 4
4 5 13
4 6 15
5 6 4


"""
dians_bians_str=input().strip()
dians_bians=[int(item) for item in dians_bians_str.split(" ")]
dians=dians_bians[0]
bians=dians_bians[1]
array=[]
for i in range(dians):
    tmp=[]
    for j in range(dians):
        if i==j:
            tmp.append(0)
        else:
            tmp.append(99999)
    array.append(tmp)
for i in range(bians):
    tmp_str=input().strip()
    tmp=[int(item) for item in tmp_str.split(" ")]
    array[tmp[0]-1][tmp[1]-1]=tmp[2]
print(array)
start=int(input("请输入起点从1开始"))
dis=[99999 for i in range(dians)]
print(dis)
for i in range(dians):
    dis[i]=array[start-1][i]
#标记是否所有的点都最短了
book=[0 for i in range(dians)]
book[start-1]=1
#起点到其他n-1个点的最短距离
for i in range(dians-1):
    min=99999
    #记录最短点的下标
    book_dian=0
    for i in range(dians):
        print("那个是str",book[i],dis[i])
        if book[i]==0 and dis[i]<min:
            min=dis[i]
            book_dian=i
    book[book_dian]=1
    #通过找到的最小的点，能否将其他的点的距离更新一下
    for i in range(dians):
        if array[book_dian][i]!="inf":
            if dis[i]>dis[book_dian]+array[book_dian][i]:
                dis[i]=dis[book_dian]+array[book_dian][i]
print(dis)