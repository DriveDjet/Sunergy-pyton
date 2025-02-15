import collections
pets={1:{'Мухтар':{
'Вид питомца':'Собака',
'Возвраст питомца':9,
'Имя владельца':'Павел'}},
      2:{'Каа':{
'Вид питомца':'желторый питон',
'Возвраст питомца':19,
'Имя владельца':'Саша'}}}

pet2={}

def create(): #добавление новой записи
    print('### Функция добавления новой записи!')
    last=collections.deque(pets, maxlen=1)[0]
    last+=1
    inp()
    pets[last]=pet2
    print('Новая запись добавлена!')
    return

def inp(): #ввод данных о питомце
    nickname=input('Кличка питомца:')
    view=input('Вид питомца:')
    year=int(input('Возвраст питомца:'))
    name=input('Имя владельца:')
    pet={'Вид питомца':view,'Возвраст питомца':year,'Имя владельца':name}
    pet2[nickname]=pet
    return pet2 

def get_suffix(years): #суффикс возвраста
    if years!=11 and years%10==1:
        suf='год'
    elif 1<years%10<5 and years!=12 and years!=13 and years!=14:
        suf='года'  
    else:
        suf='лет'
    return suf

def get_pet(ID):
    return pets[ID] if ID in pets.keys() else False
    

def read(): #отброжение информации о запрашиваемом питомце
    print('### Функция отборажения информации о пиомце!')
    ID=int(input('Введите ID:'))
    pet=get_pet(ID)

    if not pet:
        print(f'Нет питомца с таким ID:{ID}')
        return

    key=[x for x in pet.keys()][0]
    suf=get_suffix(pet[key]['Возвраст питомца'])

    string=f'Это {pet[key]['Вид питомца']} по кличке "{key}".'\
    f' Возвраст питомца: {pet[key]['Возвраст питомца']} {suf}.'\
    f' Имя владельца: {pet[key]['Имя владельца']}.'
    print(string)

def update(): #обновление информации о питомце
    print('### Функция обновления информации о питомце')
    ID=int(input('Введите ID питомца, парметр которого вы хотите обновить:'))
    pet=get_pet(ID)
    if not pet:
        print(f'Нет питомца с таким ID:{ID}')
        return
    par=input('Параметр питомца, который вы хотите обновить. Введите "info", для отображения доступных параметров. ')
    if par=='info':
        print('"Вид питомца", "Возвраст пиомца", "Имя владельца"')
        par=input('Параметр питомца, который вы хотите обновить:')
    new=input('Новое значение для этого параметра:')
    key=[x for x in pet.keys()][0]
  
    if par=='Вид питомца':
        pets[ID][key]['Вид питомца']=new
        print('Информация обновлена!')
    elif par=='Возвраст питомца':
        pets[ID][key]['Возвраст питомца']=int(new)
        print('Информация обновлена!')
    elif par=='Имя владельца':
        pets[ID][key]['Имя владельца']=new
        print('Информация обновлена!')
    else:
        par=('Неверно введенна команда!')
        print(par)
        
def delete(): #удаление записи о пиомце
    print('### Функция удаления записи о существующем питомце')
    ID=int(input('Введите ID питомца:'))
    pet=get_pet(ID)
    if not pet:
        print(f'Нет питомца с таким ID:{ID}')
        return
    del pets[ID]
    print(f'Запись о питомце с ID:{ID} удалена!')

def pets_list(): #вывод всего словаря 'pets'
    n=len(pets)
    for i in range (1,n+1):
        print(f'{i}-{pets[i]}')

command=input('Введите команду! Для отбражения списка команд введите "info". ')
while command!='stop':
    if command=='info':
        print('Команда "create" - создает новую запись о питомце!\nКоманда "read" - отображает информацию о запрашиваемом питомце!')
        print('Команда "update" - обновляет информацию об указанном питомце!\nКоманда "delete" - удаляет запись о питомце!\nКоманда "list" - выводит весь список питомцев и данные о них!\nКоманда "stop - прекращает работу программы!"')
    elif command=='create':
        create()
    elif command=='read':
        read()
    elif command=='update':
        update()
    elif command=='delete':
        delete()
    elif command=='list':
        pets_list()
    else:
        print('Команда введене неверно!!!')
    command=input('Введите команду! Для отбражения списка команд введите "info". ')    
else:                                       
    print('END')

    
