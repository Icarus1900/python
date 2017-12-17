import re
"""
findall() return list
finditer() return iterator
search() only return the first match,return object,use group() to show content
match() only search at the beginning,return object,use group() to show content
split() return list
. represent anything except /n
* repeat times from zero to infinity
+ repeat times from one to infinity
? repeat times from zero to one
{a,b} repeat times from a to b
[] choose one from inside
^ match from the start
$ match from the end
() match by group
| or
\ escape string
\d match any delimiter
\D match any non-delimiter
\s match any blank space
\S match any non-blank space
\w match any delimiter or alphabet
\W match any non-delimiter and non-alphabet
r raw string, do not use escape string in python interpreter
"""

s1 = 'alexsb'

print(s1.find('r/sb$/'))

print(s1.replace('sb','SB'))

s2 = 'abcdefg123hijk456lmn789'

print(re.findall('\d',s2))

print(re.findall('\d+',s2))

print(re.findall('\d?',s2))

print(re.findall('\d*',s2))

print(re.findall('\d{1,2}',s2))

print(re.findall('[^1-9]{1,}',s2))

print(re.findall('a[b,d]c',s2))

print(re.findall('(ab)+cd',s2))  # show content in group in priority

print(re.findall('(?:ab)+cd',s2))  # cancel priority for content in group

print(re.findall('ab|dc',s2))

print(re.findall('www\.(?:baidu|google)\.com','www.baidu.com'))

print(re.findall('([\d\.]+\*[\d\.]+)','1*2+1.4*6.8'))

print(re.findall('\s?(I)\s','I AM LISA'))

print(re.findall(r'\b(I)','I AM LISA'))

print(re.findall(r'c\\l','accc\l'))

print(re.finditer('\d+','123abc'))

res = re.search('\d+','abc123def456')
print(res.group())

res = re.match('\d+','123abc456')
print(res.group())

print(re.split('l','hello mzh'))

print(re.sub('\d+','A','123abc456def'))