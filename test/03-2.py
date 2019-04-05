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

array.sort(key=lambda item:item[2],reverse=True)

#标志循环是否结束
book=True
for i in range(n):
    if book:
        for j in range(i+1,n):
            if abs(array[i][1]-array[j][1])>=d:
                print(array[i][2]+array[j][2])
                book=False
                break
    else:
        break

