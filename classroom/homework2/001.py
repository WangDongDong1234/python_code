n1=int(input())
num=int(input())
array_string=input()
array_tmp=array_string.strip(" ").split(" ")
list=[]
for item in array_tmp:
    list.append(int(item))
list.sort()
dict={}
for item in list:
    if item in dict.keys():
        dict[item]+=1
    else:
        dict[item]=1
print(dict.items())
dict=sorted(dict.items(),key=lambda  item:item[1],reverse=True)

# print(dict.items())
result=[]
# for item in dict:
#     for i in range(0,item[1]):
#         result.append(item[0])
# print(result)
for i in range(0,len(dict)):
    for j in range(0,dict[i][1]):
        result.append(dict[i][0])
print(result)