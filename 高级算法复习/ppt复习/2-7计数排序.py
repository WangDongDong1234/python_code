def  countSort(array):
    length=len(array)
    count=[0 for i in range(length)]
    for i in range(length):
        for j in range(length):
            if array[j]<=array[i]:
                count[i]+=1
    reslut=[0 for i in range(length)]
    for i in range(len(count)):
        reslut[count[i]-1]=array[i]
    return reslut

def countSort2(array):
    length = len(array)
    result = [0 for i in range(length)]
    for i in range(length):
        count=0
        for j in range(length):
            if array[j] <= array[i]:
                count += 1
        result[count-1]=array[i]

    return result
array=[2,2,2,1,5,7,4,9,8,6,3]
print(countSort(array))
print(countSort2(array))
