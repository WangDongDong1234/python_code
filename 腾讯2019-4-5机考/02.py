length=int(input())
str=input().strip()
book=[1 for i in range(length)]
array=[]
for e in str:
    array.append(e)
start=True
while sum(book)>0 and start:
    for i in range(length):
        while book[i]==0 and i<length-1:
            i+=1
        if i==length-1:
            start=False
            break
        j=i+1
        while book[j]==0 and j<length:
                j+=1
        if j>length-1:
            start=False
            break

        if (array[i]=='0' and array[j]=='1') or (array[i]=='1' and array[j]=='0'):
            book[i]=0
            book[j]=0
            break

print(sum(book))