# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]
print("Задание 1:")
var_list=[1,3,4,5,2]
new_var_list=[i**2 for i in var_list]
print(new_var_list)

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.
print("Задание 2:")
fruits1=['apple', 'banana','orange','kiwi','pear','avocado','melon']
fruits2=['apple', 'apricot' ,'banana','orange','kiwi','lemon','pear']
fruits_new= [i for i in fruits1 if i in fruits2]
print(fruits_new)

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4
print("Задание 3:")
number_list=[1,3,4,5,-2,345,9,36]
new_number_list= [i for i in number_list if i>0 and i%3==0 and i%4!=0]
print(new_number_list)

