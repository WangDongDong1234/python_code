import re
#内置的包
from urllib.request import urlopen

res=urlopen("https://movie.douban.com/explore#!type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=20&page_start=20")
with open("data.html",mode="w",encoding="utf-8") as f:
    f.write(res.read().decode("utf-8"))
