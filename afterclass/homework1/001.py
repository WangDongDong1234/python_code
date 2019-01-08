array=input()
num=int(input())
list=[]
array_temp=array.strip(" ").split(" ")
for item in array_temp:
    list.append(int(item))
# print(list)
total=0
for i in range(0,len(list)):
    for j in range(i+1,len(list)):
        if j>i:
            max=list[i]
            min=list[i]
            for item in(i+1,j):
                if list[item]>max:
                    max=list[item]
                if list[item]<min:
                    min=list[item]
        if max-min>num:
            total+=1

print(total)