#import copy
str1=input().strip()
str2=input().strip()
#print(str1,str2)
list_b=[]
#list_c=[]
#初始化数组
for i in range(len(str1)+1):
    list_tmp=[]
    for j in range(len(str2)+1):
        list_tmp.append(0)
    list_b.append(list_tmp)
#list_c=copy.deepcopy(list_b)
#print(list_b)
#print(list_c)
def LCS(str1,str2,list_b):
    for i in range(1,len(str1)+1):
        for j in range(1,len(str2)+1):
            if str1[i-1]==str2[j-1]:
                list_b[i][j]=list_b[i-1][j-1]+1
                #list_c[i][j]=0
            else:
                if list_b[i][j-1]==list_b[i-1][j]:
                    #左右都可以
                    list_b[i][j]=list_b[i-1][j]
                    #list_c[i][j]=3
                elif list_b[i][j-1]>list_b[i-1][j]:
                    #向左
                    list_b[i][j] = list_b[i][j - 1]
                    #list_c[i][j]=1
                elif list_b[i][j-1] < list_b[i-1][j]:
                    #向上
                    list_b[i][j] = list_b[i-1][j]
                    #list_c[i][j]=2
LCS(str1,str2,list_b)
#print(list_b)
#print(list_c)
max_length=list_b[len(str1)][len(str2)]
#print(max_length)
result=[]

def path(x,y,s):

    while x>0 and y>0:
        if str1[x-1]==str2[y-1]:
            s+=str1[x-1]
            x-=1
            y-=1
        else:
            if list_b[x][y-1]>list_b[x-1][y]:
                y-=1
            elif list_b[x][y-1]<list_b[x-1][y]:
                x-=1
            else:
                path(x,y-1,s)
                path(x-1,y,s)
                #终止条件为啥要加在这里  把return 改成break   这里执行完x与y没有改变会无限循环下去
                #return
                break
    if len(s)==max_length and s[::-1] not in result:
        result.append(s[::-1])

s=""
path(len(str1),len(str2),s)
for item in result:
    print(item)


