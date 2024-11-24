number=int(input())

if number%2==0 and number<0: 
    print("Отрицательное четное число")
elif not number%2==0 and number<0:
    print("число не является четным")
elif number==0:
    print("нулевое число")
elif number%2>0 and number>0:
    print("положительное нечетное число")

