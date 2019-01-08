num=int(input())
for i in range(0,num):
    n=int(input())
    array=input()
    list=[]
    tmp_array=array.strip(" ").split(" ")
    for item in tmp_array:
        list.append(int(item))
    #print(list)
    sum=0
    for q in range(0,len(list)):
        for w in range(q+1,len(list)):
            if list[q]>list[w]:
                sum+=1
    print(sum)