str=input().strip()
list=[int(item) for item in str.split(" ")]
n=list[0]
array=list[1:]
result=[]
result.append(array[0])
length=1
for i in range(1,n):
    if array[i]>=result[length-1]:
        result.append(array[i])
        length+=1
    else:
        #array[i]小于result中最后一个
        index=length-1
        j=index-1
        while j>=0 and array[i]<result[j]:
            index-=1
            j-=1
        result.insert(index,array[i])
        length+=1
for i in range(n):
    if i ==0:
        print(result[i], end="")
    else:
        print(" "+result[i])