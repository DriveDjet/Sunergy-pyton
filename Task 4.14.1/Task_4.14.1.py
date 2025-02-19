
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]
n=(len(my_list)-1)
list.reverse(my_list)

def recurs_print(my_list, n):
    if  n<0:
        return print('Конец списка!')
    else:
        print(my_list[n])
        n-=1
        recurs_print(my_list, n)

recurs_print(my_list, n)

