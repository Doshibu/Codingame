def spl(seq, length):
    return [seq[i:i+length] for i in range(0, len(seq), length)]

u=input().replace(' ','')
if '(0)' in u : u='0'+u.split('(0)', 1)[-1]
if '(+879 )' in u : u='0'+u.split('(+879 )', 1)[-1]
print(' '.join(spl(u, 3)))
