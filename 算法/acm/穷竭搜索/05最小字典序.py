str_str=input().strip()
list=[]
for item in str_str:
    list.append(item)
left=0
right=len(list)-1
result=[]
def select(arr,i,j):
    if i==j:
        return True
    if arr[i]<arr[j]:
        return True
    elif arr[i]>arr[j]:
        return False
    else:
        return select(arr,i+1,j+1)
while left<=right:
    if left==right:
        result.append(list[left])
        break
    if select(list,left,right):
        result.append(list[left])
        left+=1
    else:
        result.append(list[right])
        right-=1
result_str=""
for item in result:
    result_str+=item
print(result_str)



