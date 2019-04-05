"""
1
a c,b c,c d,d e,d f,e g,f g
"""
import copy
n=int(input())
boundrys_str=input().strip()
new_boundary_str=boundrys_str.replace(',',' ')
#print(new_boundary_str)
boundry_list=[item for item in new_boundary_str.split(' ')]
#print(boundry_list)
s=set(boundry_list)
nodes=list(s)
#rint("1",nodes)
dict={}
for item in nodes:
    dict[item]=[0,0]
#print(dict)
boundrys=[(item[0],item[2]) for item in boundrys_str.split(',')]
#print("2",boundrys)
for item in boundrys:
    dict[item[0]][1]+=1
    dict[item[1]][0]+=1
#print("3",dict)

result=[]
sum=0
def solve(dict,result,boundrys):
    if len(dict)==0:
        global sum
        sum+=1
        #print(result)
        return
    for key,value in dict.items():
        if value[0]==0:
            new_dict=copy.deepcopy(dict)
            new_result = copy.deepcopy(result)
            del new_dict[key]
            for item in boundrys:
                if item[0]==key:
                    new_dict[item[1]][0]-=1
            new_result.append(key)
            solve(new_dict,new_result,boundrys)
solve(dict,result,boundrys)
print(sum)


