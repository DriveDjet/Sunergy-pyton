
s1=list(map(int,input().split()))
s2=list(map(int,input().split()))
sl1=set(s1)
sl2=set(s2)
sum=sl1.intersection(sl2)
print(len(sum))

   