input_str=input()
array=[item for item in input_str.split(" ")]
n=array[0]
arr=array[1:]
result=[]
for e in arr:
    if len(e)>8:
        n=len(e)//8
        yushu=len(e)%8
        for i in range(1,n+1):
            result.append(e[(i-1)*8:(i*8)])
        tmp=8-yushu
        tmp_e=e[(n)*8:]
        for i in range(tmp):
            tmp_e+="0"
        result.append(tmp_e)
    elif len(e)==8:
        result.append(e)
    else:
        tmp=8-len(e)
        for i in range(tmp):
            e+="0"
        result.append(e)

result.sort()
for item in result:
    print(item,end=" ")