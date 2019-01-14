"""
注意下一个取哪个点
在一个x轴上，距离A为R的只要满足一侧有点就行了
"""
n=int(input())
r=int(input())
array_str=input().strip()
array=[int(item) for item in array_str.split(" ")]
result=[]
total=0
current=array[0]
for i in range(len(array)):
    if array[i]==current+r:
        result.append(array[i])
        current=array[i+1]
        total+=1
    elif array[i]>current+r:
        result.append(array[i-1])
        current=array[i]
        total+=1
    else:
        continue
print(result)
print(total)