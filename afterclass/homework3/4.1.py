def insert(array,n):
    result=[]
    result.append(array[0])
    length=1
    for i in range(1,n):
        if array[i]>=result[length-1]:
            result.append(array[i])
            length+=1
        else:
            index=length-1
            pre=index-1
            while pre>=0 and array[i]<result[pre]:  #中止条件  array[i]>=resutl[pre]或者pre=-1,index=0
                index-=1
                pre-=1
            result.insert(index,array[i])
            length+=1
    return result
while 1:
    try:
        str=input().strip()
        list=[int(item) for item in str.split(" ")]
        n=list[0]
        array=list[1::]
        arr=insert(array,n)
        print(arr[0], end='')
        for i in range(1, n):
            print('', arr[i], end='')
        print()
    except EOFError:
        break
#3 3 9 12 24 29 34 49 51 56 78 84 100
#3 3 9 12 24 29 34 49 51 56 78 84 100