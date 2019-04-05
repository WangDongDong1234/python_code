# import hashlib
#
# md5_obj=hashlib.sha1()#得到一个MD5对象
# with open('shelve_demo.bak',mode='rb')as f:
#     #循环的读取文件内容
#     #循环的来update
#     md5_obj.update(f.read())
#     res=md5_obj.hexdigest()
#     print(res)

import configparser
config=configparser.ConfigParser()
# #写配置文件
# config["DEFAULT"]={'wdd':26,
#                    'wn':22,
#                    'ww':23,
#                    'wx':23}
#
# config['bitbucket.org']={'User':'hg'}
#
# config['topsecret.server.com']={'Host Port':'50022','ForwardX11':'no'}
# with open('example.ini','w')as f:
#     config.write(f)

#读配置文件
config.read('example.ini')
print(config.sections())#['bitbucket.org', 'topsecret.server.com'](default是全局的组，default的配置项可以通过其他组拿到)
print('bitbucket.org' in config)#True
print('topsecret.server.com' in config)#True
#通过section拿option
print(config['bitbucket.org']['user'])
#同过其他组拿default中的option
print(config['bitbucket.org']['wdd'])
print(config['bitbucket.org'])#<Section: bitbucket.org>
for key in config['bitbucket.org']:
    print(key)#取到全局组的内容
