import re

content = 'Find the key in this sentence!'
patt = r'\w\s(key)(\s|\S)+(thi)+'

# do regular expression
objs = re.search(patt, content)

if objs : 
    print(objs.group())

# detailed pattern information see https://www.runoob.com/python/python-reg-expressions.html