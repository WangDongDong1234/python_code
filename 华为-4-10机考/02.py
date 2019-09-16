str=input()
array=[]
length=len(str)
i=0
while i<length:
    if str[i].isdigit():
        n=int(str[i])
        t=str[i+2]
        for e in range(n):
            array.append(t)
        if str[i+3]!=")":
            i+=3
        else:
            i+=4
    else:
        array.append(str[i])
        i+=1
array.reverse()
s=""
for item in array:
    s=s+item
print(s)

