str=input().strip()
k=int(input())
length=len(str)
i=0
j=0
array=[]
while i<=length-1:
    for j in range(length+1):
        array.append(str[i:j])
    i+=1
#print(array)
s=set(array)
array=list(s)
#print(array)
last=[]
for item in array:
    if len(item)>0:
        if len(item)>=3:
            if int(item[1:]) in last:
                continue
            else:
                last.append((int(item[1:])))
        else:
            last.append(int(item))
print(last)
last.sort()
print(last[k-1])


