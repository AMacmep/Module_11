# Домашнее задание по теме "Обзор сторонних библиотек Python"
import requests

r=requests.put('https://httpbin.org/put',data={'key':'value'})
print(r)

