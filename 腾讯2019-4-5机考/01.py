money_kind_str=input().strip()
money_kind=[int(item) for item in money_kind_str.split(' ')]
money=money_kind[0]
kind=money_kind[1]
value=[]
for i in range(kind):
    v=int(input())
    value.append(v)
value.sort(reverse=True)
count=0
money_array=[0,0,0,0]
while money>0:
    for i in range(kind):
        if money>value[i]:
            money_array[i]=money//value[i]
            count+=money//value[i]




print(count)