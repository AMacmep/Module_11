# Домашнее задание по теме "Обзор сторонних библиотек Python"
import requests
import numpy as np
import pandas as pd
import pillow


url_name='https://github.com/AMacmep/Module_11'
head_url=requests.head(url_name)
print(head_url)




# xlsx = pd.ExcelFile("Excel file 1.xlsx")
# df = pd.read_excel(xlsx, "Sheet1")
# print(df)
# df.sort_index(axis=1, ascending=False)
# print(df)


