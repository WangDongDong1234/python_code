array=input("请输入数组:")
list=[]
list_temp=array.strip().split(" ")
for item in list_temp:
    list.append(int(item))
width=int(input("请输入窗口宽度"))
sum=0
for i in range(0,len(list)-width+1):
    max=list[i]
    for j in range(1,width):
        if list[j+i]>max:
            max=list[i+j]
    sum+=max
print(sum)