"""
归并排序
"""
def  merge(a,b):
    c=[]
    i=0
    j=0
    while i<len(a) and j<len(b):
        if a[i]<b[j]:
            c.append(a[i])
            i+=1
        elif a[i]>b[j]:
            c.append(b[j])
            j+=1
        else:
            c.append(a[i])
            c.append(b[j])
            i+=1
            j+=1
    if i==len(a):
        while j<len(b):
            c.append(b[j])
            j+=1
    if j==len(b):
        while i<len(a):
            c.append(a[i])
            i+=1
    return c

def mergeSort(array):
    if len(array)<=1:
        return array  #这里不能丢
    mid=int(len(array)/2)
    left=mergeSort(array[0:mid])
    right=mergeSort(array[mid:])
    return merge(left,right)

array=[2,4,5,6,8,7,3,1,9,2,5]
print(mergeSort(array))