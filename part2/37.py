import json

dic={'abc':(1,2,3),'age':18,'name':['wdd','wn']}
str_json=json.dumps(dic,sort_keys=True,indent=4,separators=('+',":"),ensure_ascii=False)
print(str_json)
"""
{
    "abc":[
        1+
        2+
        3
    ]+
    "age":18+
    "name":[
        "wdd"+
        "wn"
    ]
}
"""