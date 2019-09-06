# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os
import shutil
#функция для задачи easy
'''print('Задача 1')
def create_folders():
    currentPath = os.getcwd()
    #print ("Текущая рабочая директория %s" % currentPath)
    try:
        for i in range(1,10):
            os.mkdir(currentPath+'\dir_'+str(i))
    except:
        print('Папки уже созданы')'''
#create_folders()
def create_folders(name):
    #currentPath = os.getcwd()
    #print ("Текущая рабочая директория %s" % currentPath)
    try:
        os.mkdir(name)
        print('Папка создана')
#        print(name)
    except FileExistsError:
        print('Папка с таким именем уже существует')

#create_folders(os.path.join(,"test2"))



#Функция для задачи easy
'''def delete_folders():
    currentPath = os.getcwd()
    #print ("Текущая рабочая директория %s" % currentPath)
    try:
        for i in range(1,10):
            os.rmdir(currentPath+'\dir_'+str(i))
    except:
        print('Папки уже удалены')'''

def delete_folders(name):
    try:
        os.rmdir(name)
        print('Папка удалена')
    except FileNotFoundError:
        print('Папка не найдена')

#delete_folders('Папка_тест')

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
#print('\nЗадача 2')
#folderList = os.listdir()
#print(folderList)
#for i in folderList:
#    print(i)

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
#print('\nЗадача 3')
def copy_file():
    shutil.copy('hw05_easy.py','new_hw05_easy.py')



'''name = input('В какую папку перейти: ')
os.chdir(name)
print(name)
folderList = os.listdir()
#print(folderList)
for i in folderList:
    print(i)'''