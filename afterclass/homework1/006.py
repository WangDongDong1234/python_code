array=input()
sum=int(input())
array_temp=array.strip(" ").split(" ")

list=[]
for item in array_temp:
    list.append(int(item))
list.sort()
# print(list)
total=0
for i in range(0,len(list)):
    if list[i]>sum:
        break
    temp=sum-list[i]
    if temp in list:
        total+=1
print(int(total/2))