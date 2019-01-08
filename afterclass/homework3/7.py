#快排的递归实现
def quicksort(arr,i,j):
    if j<=i:
        return
    left=i
    right=j
    tmp=arr[i]

    while left!=right:
        while arr[right]>=tmp and right>left:
            right-=1
        while arr[left]<=tmp and right>left:
            left+=1
        arr[left],arr[right]=arr[right],arr[left]

    arr[left],arr[i]=arr[i],arr[left]
    quicksort(arr,i,left-1)
    quicksort(arr,left+1,j)

arrary=[9,8,0,6,6,5,5,7,4,2,2,3,1]
quicksort(arrary,0,12)
print(arrary)