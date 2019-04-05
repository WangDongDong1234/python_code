n=int(input())
array=[]
for i in range(n):
    tmp_str=input().strip()
    tmp=[int(item) for item in tmp_str.split(' ')]
    array.append(tmp)
#print(array)
array.sort(key=lambda item:item[1])
#print(array)
array_a=[]
array_b=[]
count_a=0
count_b=0
state=True
i=0
total=0
while state:
    array_b.append(array[i])
    for item in array_b:
        total+=item[0]
    count_a=n-1-i
    if count_a<total:
        state=False
    else:
        i+=1
sum_b=0
for item in array_b:
    sum_b+=item[1]
print(sum_b)
