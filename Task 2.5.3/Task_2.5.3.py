print("Минимальная сумма инвестиции")
x=float(input())
print("Инвестиции Майкла")
a=float(input())
print("Инвестиции Ивана")
b=float(input())
if a>=x and b>=x:
    print(2)
elif a>=x and b<x:
    print("Mike")
elif a<x and b>=x:
    print("Ivan")
elif b+a>=x:
    print(1)
else:
    print(0)
        