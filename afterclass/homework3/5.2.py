def bubble(array,n):
    for i in range(0,n-1):
        for j in range(1,n-i):
            if array[j-1]>array[j]:
                array[j-1],array[j]=array[j],array[j-1]

while 1:
    try:
        str=input().strip()
        list=[int(item) for item in str.split(" ")]
        n=list[0]
        array=list[1::]
        bubble(array,n)
        print(array[0], end='')
        for i in range(1, n):
            print('', array[i], end='')
        print()
    except EOFError:
        break
