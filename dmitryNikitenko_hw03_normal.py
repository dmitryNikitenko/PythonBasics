# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1
print('Задание 1\n')
[‎30.‎08.‎2019 11:45] Zakonov Ilya (DI):
def fibonacci(n,m):
    fib1 = 1
    fib2 = 1
    i = 1
    list=[]
    while i <= m:
        if i>=n:
            print(fib1)
            list.append(fib1)
        fib2 = fib2 + fib1
        fib1 = fib2 - fib1
        i += 1
    return print(list)
fibonacci(4,7)
 #  pass


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()

print('\nЗадание 2\n')
def sort_to_max(origin_list):
#    print(origin_list)
    n = 1
#    print(range(len(origin_list)-1))
    while n < len(origin_list):
        for i in range(len(origin_list) - 1):
#            print(origin_list[i])
            print(origin_list[i + 1])
            if origin_list[i] > origin_list[i + 1]:
 #               print(origin_list[i+1])
                origin_list[i],origin_list[i + 1] = origin_list[i + 1],origin_list[i]
        print(origin_list, '; n = ',n)
        n+=1

    return origin_list
    pass

print(sort_to_max([2, 10, -12, 2.5]))



# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.
print('\nЗадание 3\n')

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.
print('\nЗадание 4\n')