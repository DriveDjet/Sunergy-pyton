n=int(input())
a=[]
for i in range(n):
    c=int(input())
    if c>1 and c<1000 and c<=c*10**9:
        a.append(c)

b=a[n-1]
a.insert(0,b)
a.pop()
print(a)

