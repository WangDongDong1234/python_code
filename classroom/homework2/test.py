dict={'qq':21,'ww':2,'ee':7}
print(dict.items())
dict=sorted(dict.items(),key=lambda item:item[1])
print(dict)