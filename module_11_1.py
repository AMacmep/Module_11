# Домашнее задание по теме "Обзор сторонних библиотек Python"
import requests as rq
import pandas as pd
import numpy as np
from PIL import Image


'''
# Requests - это простая HTTP-библиотека для Python, созданная для людей.
url_name = 'https://esia.gosuslugi.ru/'
r = rq.get(url_name)
encoding_url = r.encoding
print(f'Кодировка страницы {url_name} - {encoding_url}')  # Вывод на печать используюмую кодировку
print()

# Pandas -  это библиотека, предоставляющая высокопроизводительные и простые в использовании структуры данных
# и инструменты для анализа данных для языка программирования Python.

data = pd.read_csv("myfile.csv", sep=";", header=(0))  # Читаем данные из файла .csv
df = pd.DataFrame(data)  # Изменение представления данных с целью дальнейшей обработки или обобщения данных

sorted_data = df.sort_values('Age')  # Отсортировано по значению в столбце 'Age'
print(sorted_data)
print()

filtered_age = df.filter(regex='g')
print(filtered_age)  # фильтруем по значению заголовка содержащего символ 'g'
print()
'''

# NumPy -  базовый пакет для научных вычислений,
# билиотека которая предоставляет объект многомерного массива
# и набор процедур для быстрых операций с массивами

array_1 = np.array([[3, 7, 9],
                    [6, 4, 2]])
array_2 = np.array([[17, 15, 22],
                    [6, 3, 9]])  # Создали тестовый двухмерный массив
print(array_1.ndim)  # Количество измерений массива
print(array_1.shape)  # Вывели размер массива

sort_array = np.sort(array_1, 0)  # Сортировка по столбцам
print(sort_array)
print()

array_0 = np.concatenate((array_1, array_2), axis=0)
print(array_0)  # Объединение массивов
print(array_0.shape)
print()

array_mult = array_1 * array_2  # поэлементное умножение массивов
print(array_mult)

# Pillow - иблиотека обработки изображений

size_2=1000,1000
with Image.open("picture1.jpg") as im:
    (left, upper, right, lower) = (500,0,1000,500)
    im_crop = im.crop((left, upper, right, lower)) #Обрезка изображения
    im.thumbnail(size_2)    # изменение размера
    im.rotate(-20).save('picture2.gif', 'gif') # поворот и сохранение
    im_crop.rotate(60).show()  # поворот изображения на 60 градусов и вывод на экран



