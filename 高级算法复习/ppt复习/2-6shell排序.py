"""
思想：取步增长为length/2  直到步增长为1
"""
def shellsort(array):
    length=len(array)
    gap=length
    while gap>1:
        gap=int(gap/2)#gap是增量
        for i in range(gap,length):
            for j in range(i,0,-gap):#为啥要多这一步，带排序数要插到以排序数组的某一个位置，不能只和最后一个比较
                if array[i]<array[i-gap]:#i至少要是第二个  有个i-gap
                    array[i],array[i-gap]=array[i-gap],array[i]
array=[5,4,6,8,9,7,2,1,3]
shellsort(array)
print(array)