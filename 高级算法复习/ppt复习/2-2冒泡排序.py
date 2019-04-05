"""
冒泡排序
"""
def bubbleSort(array):
    for i in range(len(array)-1):
        for j in range(0,len(array)-1-i):
            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
array=[2,1,5,6,3,4,9,8,7]
bubbleSort(array)
print(array)