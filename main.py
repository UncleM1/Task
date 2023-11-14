
#Обновим данный список словарей данными о начале и завершении рабочего дня в соответсвии с представленными данными
busy = [
    {'start':'00:00',
     'stop':'9:00'
     },
    {'start':'10:30',
     'stop':'10:50',
     },
    {'start':'18:40',
         'stop':'18:50',
         },
    {'start':'14:40',
         'stop':'14:50',
         },
    {'start':'16:40',
         'stop':'17:20',
         },
    {'start':'20:05',
         'stop':'20:20',
         },
    {'start':'21:00',
     'stop':'00:00',
     }
]

#Преобразуем список слварей в список списков
lst = []
for i in busy:
    a = list(i.values())
    lst.append(a)

#Представим время в виде десятичной дроби и отсортируем список по возрастанию
for i in range(len(lst)):
    for j in range(len(lst[i])):
        a = lst[i][j].split(':')
        a[0] = int(a[0])
        a[1] = int(a[1])/60
        lst[i][j] = a[0]+a[1]

lst = sorted(lst)


#Функция how_much проверяет колличество вхождений получаса в заданные промежуток времени
#и составляетсписок windows со свободным временем (время предствляется в формате h:m)
windows = [

]
def how_much(a,b):
    counter = int((b-a)//0.5)
    for i in range(counter):
        w = a+ 0.5
        if a - int(a)==0:
            window = str(int(a)) + ':' +str(int((a - int(a))*60))+'0'
        else:
            window = str(int(a)) + ':' +str(round((a - int(a))*60))
        if w - int(w) == 0:
            window += '-' + str(int(w)) + ':' + str(int((w - int(w)) * 60)) + '0'
        else:
            window += '-' + str(int(w)) + ':' + str(round((w - int(w)) * 60))
        windows.append(window)
        a = w


for i in range(len(lst)-1):
    how_much(lst[i][1],lst[i+1][0])
