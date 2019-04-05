"""
https://www.cnblogs.com/fzl194/p/8677350.html
"""
array_str=input().strip()
array=[int(item) for item in array_str.split(' ')]
array.insert(0,0)

def fun(main):
    length=len(array)-1
    while(length):
        thissum=0
        maxsum=-9999
        start=1
        finish=1
        thisstart=1
        for i in range(1,len(array)):
            thissum+=array[i]
            if(thissum>maxsum):
                maxsum=thissum
                start=thisstart
                finish=i
            if thissum<0:
                thissum=0
                thisstart=i+1
        print(maxsum,start,finish)
        length-=1
fun(array)
