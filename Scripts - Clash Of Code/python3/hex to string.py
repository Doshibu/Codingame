vi = int(input())
print(''.join([(bytes.fromhex(v).decode('utf-8')) for v in input().split()]))
