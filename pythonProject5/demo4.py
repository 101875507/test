import re
#findall: 匹配字符串中所有的符合正则规则的内容
#lst= re.findall(r'\d+','我的电话号码是：10086,我女朋友的电话号码是：10010')
#print(lst)
#finditer: 匹配字符串中所有的符合正则规则的内容(返回的是迭代器),从迭代器中拿到内容需要。group()
#it = re.finditer(r'\d+','我的电话号码是：10086,我女朋友的电话号码是：10010')
#print(it)
#for i in it:
#    print(i.group())
#search 返回的对象是match对象，拿数据是需要.group
#s = re.search(r'\d+','我的电话号码是：10086,我女朋友的电话号码是：10010')
#print(s.group())
#s = re.match(r'\d+','10086,我女朋友的电话号码是：10010')
#print(s.group())
