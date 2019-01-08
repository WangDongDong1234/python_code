a=input()
b=input()
list_1=a.strip(" ").split(" ")
list_2=b.strip(" ").split(" ")
list_a=[]
list_b=[]
for item in list_1:
    list_a.append(int(item))
for item in list_2:
    list_b.append(int(item))
cha=abs(sum(list_a)-sum(list_b))
for i in range(0,len(list_a)):
    for j in range(0,len(list_b)):
        tmp=abs((sum(list_a)-list_a[i]+list_b[j])-(sum(list_b)-list_b[j]+list_a[i]))
        if tmp<cha:
            cha=tmp
            t=list_a[i]
            list_a[i]=list_b[j]
            list_b[j]=t
print(cha)