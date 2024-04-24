import json
import datetime
from datetime import date
import random

file2 = open('gfile.json', 'r', encoding='utf-8')

dats_mas = json.load(file2)

datchik11= dats_mas[0]
dat11_lib = {}
datchik12 = dats_mas[1]
dat12_lib = {}
datchik13 = dats_mas[2]
dat13_lib = {}
datchik14 = dats_mas[3]
dat14_lib = {}

fignya = []

for i in range(10):
    data = {}
    data['cex'] = str(random.randint(1,10))
    data['datchik'] = str(random.randint(1,10))

    data['date'] = '2024-04-24'
    b = random.randint(1, 3)
    if b == 1 or b == 2:
        data['Значение'] = str(random.randint(30, 100))
    elif b == 3:
        data['Значение'] = str(random.randint(1000, 100000))
    fignya.append(data)

print(fignya)
print(date.today())






print(dat11_lib)
print(dat12_lib)
print(dat13_lib)
print(dat14_lib)



print(dats_mas)