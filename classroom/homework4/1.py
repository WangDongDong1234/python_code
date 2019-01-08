n=int(input())
result=[]
for i in range(0,n):
    array=input()
    tmp=array.strip().split(" ")
    lst=[]
    for item in tmp:
        lst.append(int(item))
    sum=1
    for i in range(0,lst[1]):
        sum*=lst[0]
    #print(sum)
    result.append(sum%lst[2])
for item in result:
    print(item)