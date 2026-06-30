
'''

import re


pattern='[abc]'
text = 'codegnan'


res = re.match(pattern,text)

print(res.group() if res else "No match Found")


c


#match:checks the first character

import re
pattern='[abc]'
text = 'Pyhton'


res = re.match(pattern,text)

print(res.group() if res else "No match Found")


No match Found





# search:checks the entire string
import re
pattern='[a-z]'
text = 'Pyhton version 3.11'


res = re.search(pattern,text)

print(res.group() if res else "No match Found")




#find all
import re
pattern='[a-z]'#[0-9]
text = 'Pyhton version 3.11'


res = re.findall(pattern,text)
print(res)

#print(res.group() if res else "No match Found")

['y', 'h', 't', 'o', 'n', 'v', 'e', 'r', 's', 'i', 'o', 'n']

#['3', '1', '1']




#find it

import re
pattern='[0-9]'
text = 'Python version 3.11'


res = re.finditer(pattern,text)
for i in res:
    print(i.group(),i.start())


3 15
1 17
1 18





#fullmatc:

import re

pattern='[a-z]{9}'
text = 'abcdefghi'


res = re.fullmatch(pattern,text)
#for i in res:
#    print(i.group(),i.start())
    

print(res.group() if res else "No match Found")


abcdefghi



#split

import re

pattern=r'[,a+yn]'
text = 'java,python,c++'


res = re.split(pattern,text)

    
print(res)


['j', 'v', '', 'p', 'tho', '', 'c', '', '']



'''

import re

pattern = r'[0-9][2]'
text = 'python: 34 mysql : 78 java : 56 html : 45'

res = re.sub(pattern, '***', text)

print(res)

python: 34 mysql : 78 java : 56 html : 45


























































