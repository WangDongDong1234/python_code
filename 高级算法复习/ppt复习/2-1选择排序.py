"""
选择排序
"""
def selectedSort(array):
    length=len(array)
    #n个数进行n-1次选择
    for i in range(0,length-1):
        small=i
        for j in range(i+1,length):
            if array[small]>array[j]:
                array[small],array[j]=array[j],array[small]
array=[2,5,8,4,4,7,9,1,3]
selectedSort(array)
print(array)