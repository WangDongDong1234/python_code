while 1:
    try:
        str=input().strip()
        if len(str)==0:
            break
        list_tmp=str.split(" ")
        list=[int(item) for item in list_tmp]
        n=list[0]
        array=list[1:]
        for i in range(0,n-1):
            for j in range(1,n-i):
                if array[j-1]>array[j]:
                    array[j-1],array[j]=array[j],array[j-1]
        for i in range(n):
            if i!=n-1:
                print(array[i],end=" ")
            else:
                print(array[i], end="")
    except EOFError:
        break

