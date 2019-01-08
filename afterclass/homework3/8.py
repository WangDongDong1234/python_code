##归并排序的递归实现
def merge(a,b):
    i=0
    j=0
    arr=[]
    while i<len(a) and j<len(b):
        if a[i]<=b[j]:
            arr.append(a[i])
            i+=1
        else:
            arr.append(b[j])
            j+=1

    if i==len(a):#注意此处是i==len(a)-1还是i==len(a)
        arr.extend(b[j:])
    if j==len(b):
        arr.extend(a[i:])
    return arr

def merge_sort(nums):
    if len(nums)<=1:
        return nums
    mid=int(len(nums)/2)
    left=merge_sort(nums[:mid])
    right=merge_sort(nums[mid:])
    return merge(left,right)

while 1:
    try:
        str=input().strip()
        list=[int(item) for item in str.split(" ")]
        n=list[0]
        array=list[1::]
        arr=merge_sort(array)
        #print(arr)
        print(arr[0], end='')
        for i in range(1, n):
            print('', arr[i], end='')
        print()
    except EOFError:
        break
