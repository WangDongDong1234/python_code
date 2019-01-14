dic={"a":8,"b":2,"c":3}
it=sorted(dic.items(),key=lambda item:item[1])
di={}
for item in it:
    di[item[0]]=item[1]
print(di)