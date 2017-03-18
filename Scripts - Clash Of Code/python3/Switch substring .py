def swap(text, ch1, ch2):
    return text.replace(ch2, '!',).replace(ch1, ch2).replace('!', ch1)

print(swap(swap(input(),'A','T'), 'C', 'G'))

'''
https://www.codingame.com/clashofcode/clash/report/3015647c334e54c47729782b14d04cc3763d67
'''
