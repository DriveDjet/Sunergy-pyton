
a = list(map(int, input().split()))
newset = set()
for i in a:
    print('YES' if i in newset else 'NO')
    newset.add(i)
