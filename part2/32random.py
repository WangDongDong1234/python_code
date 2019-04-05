import random
# #0-1之内的随机小数
# print(random.random())
# #1-5之内的随机小数(给定任意范围)
# print(random.uniform(1,5))
#
# print(random.randint(1,2))#[1,2]
# print(random.randrange(1,2))#[1,2)
# print(random.randrange(1,10,2))#[1,10)之内随机取奇数
#
#随机抽取一个值
l=["11","22","33","aa"]
ret=random.choice(l)
print(ret)


#随机抽取多个值
ret=random.sample(l,2)
print(ret)
print("".join(ret))

#在原来列表的基础上做乱序
random.shuffle(l)
print(l)

def choose_num():
    num=None
    if(random.randint(1,2)%2==0):
        num=random.randrange(0,10)
        return num
    else:
        num=random.randrange(65,123)
        return chr(num)

for i in range(6):
    print(choose_num())


