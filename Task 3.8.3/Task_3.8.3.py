m=int(input())
if (m>=1) and (m<=m*10**6):
    n=int(input())
    if (n>=1) and (n<=100):
        weights=[]
    else:
        print("Недопустимое число рыбаков")
else:
    print("Недопустимая максимальная масса")

for i in range(n):
    weight=int(input())
    if weight>=1 and weight<=m:
        weights.append(weight)
    else:
        print("Недопустимы вес рыбака")
weights.sort()
i,j=0, len(weights)-1
boats=0

while i<=j:
    if weights[i]+weights[j]<=m:
        i+=1
    else:
        j-=1
        boats+=1
else:
     boats+=1
print(boats)