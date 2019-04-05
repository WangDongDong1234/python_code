"""
思想是每添加一个中转点，使得任意两点的路径变短
4 8
1 2 2
1 3 6
1 4 4
2 3 3
3 1 7
3 4 1
4 1 5
4 3 12
"""
citys_rotes_str=input().strip()
citys_rotes=[int(item) for item in citys_rotes_str.split(' ')]
citys=citys_rotes[0]
rotes=citys_rotes[1]
array=[]
for i in range(citys):
    tmp=[]
    for j in range(citys):
        if i==j:
            tmp.append(0)
        else:
            tmp.append(99999)
    array.append(tmp)
for i in range(rotes):
    tmp_str=input().strip()
    tmp=[int(item) for item in tmp_str.split(' ')]
    array[tmp[0]-1][tmp[1]-1]=tmp[2]
print(array)
for k in range(citys):
    for i in range(citys):
        for j in range(citys):
            if array[i][j]>array[i][k]+array[k][j]:
                array[i][j]=array[i][k]+array[k][j]

print(array)
