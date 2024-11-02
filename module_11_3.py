# Домашнее задание по теме "Интроспекция"
# Цель задания:

# Закрепить знания об интроспекции в Python.
# Создать персональную функции для подробной интроспекции объекта.
import sys
import time
from pprint import pprint
import inspect

introspect_dict = {}

def introspection_info(obj):
    type_obj = type(obj)
    all_attributes = dir(obj)
    attributes = [attribute for attribute in all_attributes if
                  not callable(getattr(obj, attribute)) and not attribute.startswith('__')]
    methods = [method for method in all_attributes if callable(getattr(obj, method)) and not method.startswith('__')]
    module_obj = inspect.getmodule(obj)
    byte_size = sys.getsizeof(obj)

    instrospect_dict = {'Тип объекта': type_obj}
    instrospect_dict['Атрибуты объекта'] = attributes
    instrospect_dict['Методы объекта'] = methods
    instrospect_dict['Модуль, к которому объект принадлежит'] = module_obj
    instrospect_dict['Размер объекта в байтах'] = byte_size
    return instrospect_dict

'''
pprint(introspection_info(1),sort_dicts=False)
print('-----------------------------------')
pprint(introspection_info("Тестовая строка"),sort_dicts=False)
print('-----------------------------------')
pprint(introspection_info(introspection_info),sort_dicts=False)
print('-----------------------------------')
pprint(introspection_info(introspect_dict),sort_dicts=False)
print(dir(introspect_dict))
'''

number_info = introspection_info(42)
print(number_info)
