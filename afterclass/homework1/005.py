array=input()
section=input()
num=int(input())
array_temp=array.strip(" ").split(" ")
section_temp=section.strip(" ").split(" ")
list=[]
for item in array_temp:
    list.append(int(item))
list_temp=list[int(section_temp[0])-1:int(section_temp[1]):1]
#print(list_temp)
list_temp.sort()
#print(list_temp)
print(list_temp[num-1])
