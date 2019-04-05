""""""
import os
# os.path.abspath(path)#返回path规范化的绝对路径
# # os.path.split(path)#将path分割成目录和文件名二元组返回
# # os.path.dirname(path)#返回path的目录，其实就是os.path.split(path)的第一个元素
# # os.path.basename(path)#返回path最后的文件名，如果path以\或/结尾，那么就会返回空值即os.path.split(path)的第二个元素
# # os.path.exists(path) #如果path存在，返回True;如果path不存在，返回false
# # os.path.isabs(path)#如果path是绝对路径，返回True
# # os.path.isfile(path)#如果path是一个存在的文件，返回True,否则返回false
# # os.path.isdir(path)#如果path是一个存在的目录，则返回True,否在返回false
# # os.path.join(path1,path2)#组合路径（根据平台的分割符进行拼接）
# # os.path.getatime(path)#返回path所指向的文件或者目录的最后访问时间
# # os.path.getmtime(path)#返回path所指向的文件或者目录的最后修改时间
# # os.path.getsize(path)#返回path文件或文件夹（只返回文件夹的大小，文件夹里有什么都不会计算）的大小
print(__file__)
print(os.path.dirname(os.path.dirname(__file__)))