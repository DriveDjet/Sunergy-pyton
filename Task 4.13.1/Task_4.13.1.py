import random
l=int(input())
n=int(input())

mat1=[[random.randint(1, 1001) for j in range(n)] for i in range(l)]
print('Matrix 1:')
for i in range (l):
    print(mat1[i])

mat2=[[random.randint(1, 1001) for j in range(n)] for i in range(l)]
print('Matrix 2:')
for i in range (l):
    print(mat2[i])

mat3=[[mat1[i][j]+mat2[i][j] for j in range (len(mat1[0]))] for i in range(len(mat1))]
print('Matrix 3:')
for i in range (l):
    print(mat3[i])