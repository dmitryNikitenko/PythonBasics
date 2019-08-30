# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.
print('Задание 1\n')

def my_round(number, ndigits):
    number = number*pow(10,ndigits)
    number_ost = number - int(number)
    if number-int(number) >0.5:
        number=(number+1)//1
    else:
        number=number//1

    return number/pow(10,ndigits)
#    pass
print(my_round(2.4264567, 2))
print(my_round(2.0994267, 4))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить
print('\nЗадание 2\n')
#ticket_number='123006'
def lucky_ticket(ticket_number):
    ticket_number = list(str(ticket_number))
    numbers = [int(i) for i in ticket_number]
#    print(numbers)
    if (sum(numbers[:3]) == sum(numbers[3:])):
        ticket_number="LUCKY :)"
    else:
        ticket_number="UNLUCKY :("
    return ticket_number
 #   pass

print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))