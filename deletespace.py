import re

text = '''請 求 您 幫 我 oxxo.studio 去 除 空 白 ok ？
但是要保留換行 可以 嗎 ，(        哈哈哈 )( 啊哈)
統一便利超商 (711) 的括號之間也要有空白喔！
寫作規    範就是這 麼 100% 的龜毛～
'''


a=re.compile('[\u4E00-\u9FFF\uFF00-\uFFFF\u0021-\u002F\n]|[a-zA-Z0-9]+')
b=re.findall(a,text)
text =' '.join(b)
print(text)

a=re.compile('(?<=[^a-zA-Z0-9\u0021-\u002F])(\x20)(?=[^a-zA-Z0-9\u0021-\u002F])')
text = re.sub(a,'', text)
print(text)

a=re.compile('(\x20)(?=[\(\%\uFF00-\uFFFF])')
text = re.sub(a,'', text)
print(text)

text = text.replace(' . ','.')
print(text)