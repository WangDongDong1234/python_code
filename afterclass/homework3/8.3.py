#自己手写一遍
#非递归的思想：
def merge(array,low,mid,height):
    left=array[low:mid]
    right=array[mid:height]
    i=0
    j=0
    result=[]
    while i<len(left) and j<len(right):

        if left[i]<=right[j]:
            result.append(left[i])
            i+=1
        else:
            result.append(right[j])
            j+=1
        if i==len(left):
            result.extend(right[j:])
        if j==len(right):
            result.extend(left[i:])

        array[low:height]=result

array=[5,4,3,2,1]
i=1#先一个一个的一组  然后两个两个的一组
while i<len(array):
    low=0
    while low<len(array):
        mid=low+i
        height=min(low+2*i,len(array))
        if mid<height:
            merge(array,low,mid,height)
        low=low+i*2
    i=i*2

print("sfa ")
print(array)