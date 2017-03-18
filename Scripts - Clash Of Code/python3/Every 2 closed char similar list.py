print(sum(any([a==b for a,b in zip(w,w[1:])])for w in input().lower().split()))

'''or'''

import re
s=re.findall('(\w*(\w)\\2\w*)',input().lower())
print(len(s))


'''
abbcdeefgg
return sum(b,e,g)==3
'''
