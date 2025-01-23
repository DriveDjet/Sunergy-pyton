n=int(input())
c=[]

for i in range(n):
    a=int(input())
    if a>1 and a<1000 and a<=a*10**5:
        c.append(a)
c.reverse()
print(c)