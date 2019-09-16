length=int(input())
str=input().strip()
array=[]
for e in str:
    array.append(e)
start=True
while len(array)>1 and start:
    l=len(array)
    d=[]
    for i in range(l-1):
        j=i+1
        if (array[i]=="0" and array[j]=="1") or (array[i]=="1" and array[j]=="0"):
            d.append(i)
            d.append(j)
            break
        if i==l-1:
            if (array[i]=="0" and array[j]=="1") or (array[i]=="1" and array[j]=="0"):
                start=True
            else:
                start=False
    array.pop(d[0])
    array.pop(d[0])
print(len(array))