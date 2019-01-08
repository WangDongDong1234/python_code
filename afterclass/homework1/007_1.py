#list记录以i为分段点的最长增长子序列的个数
#返回最大分段点的坐标
def Max(list,n):
    max=0
    index=0;
    for i in range(0,n):
        if list[i]>max:
            max=list[i]
            index=i
    return index;

def LIS(array,len,list,list_increase):
    # list记录以i为分段点的最长增长子序列的个数
    for i in range(0,len):
        list.append(1)
        list_increase[i].append(array[i])
        for j in range(0,i):
            if (array[i]>array[j])and(list[j]+1>list[i]):
                list[i]=list[j]+1
                for item in list_increase[j]:
                    if item not in list_increase[i]:
                        list_increase[i].append(item)
    location=Max(list,len)
    return  location

arr=input()
arr_tmp=arr.strip(" ").split(" ")
#起初输入的数组
array_0=[]
array=[]
for item in arr_tmp:
    array.append(int(item))
    array_0.append(int(item))
list1=[]
list_increase=[]
for i in range(0,len(array_0)):
    tmp_list=[]
    list_increase.append(tmp_list)
index=LIS(array,len(array),list1,list_increase)
#print(list1)
#print(list_increase)

array.reverse()
list_reduce=[]
list2=[]
for i in range(0,len(array_0)):
    tmp_list = []
    list_reduce.append(tmp_list)
index2=LIS(array,len(array),list2,list_reduce)
list2.reverse()
list_reduce.reverse()
#print(list2)
#print(list_reduce)
sum=0
index=0
for i in range(0, len(list1)):
    if sum<(list1[i]+list2[i]):
        sum=list1[i]+list2[i]
        index=i
list_increase[index].sort()
list_reduce[index].sort(reverse=True)
#print(list_increase[index])
#print(list_reduce[index])
print_list=[]
for item in list_increase[index]:
    print_list.append(item)
for i in range(1,len(list_reduce[index])):
    print_list.append(list_reduce[index][i])

for item in print_list:
    print(item,end=" ")