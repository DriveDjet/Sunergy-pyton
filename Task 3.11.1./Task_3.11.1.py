def fac(n):
    if n == 0:
        return 1
    return fac(n-1) * n

y=int(input())
spisok=[]
a=fac(y)

for i in range(a,0,-1):
    spisok.append(fac(i))
print(spisok)