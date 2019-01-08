import copy
str1=input().strip()
str2=input().strip()
#print(str1,str2)
list_b=[]
list_c=[]
#初始化数组
for i in range(len(str1)+1):
    list_tmp=[]
    for j in range(len(str2)+1):
        list_tmp.append(0)
    list_b.append(list_tmp)
list_c=copy.deepcopy(list_b)
#print(list_b)
#print(list_c)
def LCS(str1,str2,list_b,list_c):
    for i in range(1,len(str1)+1):
        for j in range(1,len(str2)+1):
            if str1[i-1]==str2[j-1]:
                list_b[i][j]=list_b[i-1][j-1]+1
                list_c[i][j]=0
            else:
                if list_b[i][j-1]==list_b[i-1][j]:
                    #左右都可以
                    list_b[i][j]=list_b[i-1][j]
                    list_c[i][j]=3
                elif list_b[i][j-1]>list_b[i-1][j]:
                    #向左
                    list_b[i][j] = list_b[i][j - 1]
                    list_c[i][j]=1
                elif list_b[i][j-1] < list_b[i-1][j]:
                    #向上
                    list_b[i][j] = list_b[i-1][j]
                    list_c[i][j]=2
LCS(str1,str2,list_b,list_c)
print(list_b)
print(list_c)
# for item in list_b:
#     print(item)
# print("----")
# for item in list_c:
#     print(item)
# def print_LCS(x,y):
#     if x==0 or y==0:
#         return
#     if list_c[x][y]==0:
#         print_LCS(x-1,y-1)
#         print(str1[x-1],end=" ")
#     elif list_c[x][y]==3:
#         print("(",end=" ")
#         print_LCS(x-1,y)
#         print("+",end=" ")
#         print_LCS(x,y-1)
#         print(")",end=" ")
#     elif list_c[x][y]==1:
#         print_LCS(x,y-1)
#     elif list_c[x][y]==2:
#         print_LCS(x-1,y)

# def print_LCS2(x,y):
#     if x==0 or y==0:
#         return ""
#     if list_c[x][y]==0:
#         return print_LCS2(x-1,y-1)+str1[x-1]
#     elif list_c[x][y]==3:
#         if print_LCS2(x-1,y)==print_LCS2(x,y-1):
#             return print_LCS2(x,y-1)
#         return "("+print_LCS2(x-1,y)+"+"+print_LCS2(x,y-1)+")"
#
#     elif list_c[x][y]==1:
#         return print_LCS2(x,y-1)
#     elif list_c[x][y]==2:
#         return print_LCS2(x-1,y)
# result=print_LCS2(len(str1),len(str2))
# print(result)
max_length=list_b[len(str1)][len(str2)]
print(max_length)
result=[]

def print_path(x,y,s):
    while x>0 and y>0:
        if str1[x-1]==str2[y-1]:
            s+=str1[x-1]
            print_path(x-1,y-1,s)
        else:
            if list_b[x-1][y]>list_b[x][y-1]:
                x-=1
            elif list_b[x-1][y]<list_b[x][y-1]:
                y-=1
            else:
                print_path(x-1,y,s)
                print_path(x,y-1,s)
    if len(s)==max_length:
        result.append(s[::-1])

print_path(len(str1),len(str2),"")
print("111")
for item in result:
    print(item)


