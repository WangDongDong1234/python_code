dict={}
with open("stock2.txt",mode="r",encoding="utf-8") as f:
    while 1:
        context=f.readline().strip("\n")
        #print(context)
        if not context:
            break
        array=context.split(",")
        key=array[0]+","+array[1]
        value=[int(array[2]),float(array[3])]
        if key in dict:
            tmp=dict[key]
            tmp[0]+=value[0]
            tmp[1]+=value[1]
        else:
            dict[key]=value
for key,value in dict.items():
    print(key,",",value[0],value[1])
