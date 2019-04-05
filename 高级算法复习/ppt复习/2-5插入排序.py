def insert(array):
    length=len(array)
    for i in range(1,length):
        #i前面的坐标
        j=i-1
        tmp=array[i]
        while tmp<array[j] and j>-1:#注意这里是j>-1
            array[j+1]=array[j]
            j-=1
        array[j+1]=tmp    #注意这里是j+1,j指的是下一个要比较的元素，j+1位置才是空着的位置
array=[5,4,3,6,8,9,7,2,1]
insert(array)
print(array)