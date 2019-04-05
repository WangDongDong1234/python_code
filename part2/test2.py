import configparser
config=configparser.ConfigParser()
# config["DEFAULT"]={
#     'wdd':26,
#     'wn':22,
#     'ww':23,
#     'wx':23
# }
#
# config['bitbucket.org']={'User':'hg'}
#
# config['topsecret.server.com']={'Host Port':'50022','ForwardX11':'no'}
#
# with open('11.ini','w') as f:
#     config.write(f)
config.read('11.ini')
print(config.sections())