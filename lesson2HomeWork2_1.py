# Задача-1:
# Дан список фруктов.
# Напишите программу, выводящую фрукты в виде нумерованного списка,
# выровненного по правой стороне.
# Подсказка: воспользоваться методом .format()

# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз
print('\nЗадача №1 \n')
fruits = ["яблоко", "банан", "киви", "арбуз"]
#print(enumerate(fruits, start=0))
for key, fruits in enumerate(fruits, start=1):
    key=str(key)
  #  print(index)
    print((key + '.'), '{:>10}'.format(fruits))




# Задача-2:
# Даны два произвольные списка.
# Удалите из первого списка элементы, присутствующие во втором списке.
print('\nЗадача №2 \n')
first_list = ['значения', 'произвольного', 'списка', 1]
second_list = ['значения','произвольного','списка', 2]
print("Значения первого списка до удаления: ",first_list)
for value in second_list:
#    print(value)
    if value in first_list:
        first_list.remove(value)
print("значения первого списка после удаления: ", first_list)
print(second_list)

print('\nЗадача №3 \n')

# Задача-3:
# Дан произвольный список из целых чисел.
# Получите НОВЫЙ список из элементов исходного, выполнив следующие условия:
# если элемент кратен двум, то разделить его на 4, если не кратен, то умножить на два.

number_list=[1,2,3,4,5,6,76,7]
print(number_list)
new_number_list=[]
for value in number_list:
    if value%2==0:
        value=value/4
        print(value)
        new_number_list.append(value)
    else:
       value=value*2
       print(value)
       new_number_list.append(value)
print('Исходный список :',number_list)
print('Новый обработанный список: ',new_number_list)