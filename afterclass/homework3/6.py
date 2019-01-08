
str=input()
array=[int(i) for i in str.strip().split(" ")]
list=array[1::]
result=[]
for i in range(array[0]):
    result.append(0)
for i in range(array[0]):
    for j in range(array[0]):
        if list[i]>list[j]:
            result[i]+=1
print_result=[]
for i in range(0,array[0]):
    for j in range(0,len(result)):
        if i==result[j]:
            print_result.append(list[j])
for i in range(0,len(print_result)):
    if i==0:
        print(print_result[0],end="")
    else:
        print("",print_result[i],end="")
