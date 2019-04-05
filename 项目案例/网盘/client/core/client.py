def mian():
    start_1=[('登陆',),('注册',),('退出',)]
    for index,item in enumerate(start_1,1):
        print(index,item[0])
    while True:
        try:
            num=int(input('>>'))
            func_str=start_1[num-1][1]
        except:
            print("你输入的信息有误")
            #字符串数据类型的方法login  register quit