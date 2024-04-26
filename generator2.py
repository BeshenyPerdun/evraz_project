import json
import datetime
from datetime import date
import random
import time

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

errors =0

def dats():
    data = date.today()
    # year = data[0:4]-
    # print(year)
    delta = datetime.timedelta(random.randint(0,7))
    rd = data - delta
    return rd
fignya = []

for i in range(20):
    data = {}
    data['Цех'] = str(random.randint(1,10))
    data['Датчик'] = str(random.randint(1,10))
    dats2 = dats()
    data['Дата'] = str(dats2)
    b = random.randint(1, 4)
    if b == 1 or b == 2 or b == 3:
        data['Значение'] = str(random.randint(30, 100))
    elif b == 4:
        data['Значение'] = str(random.randint(1000, 100000))
        errors += 1
    fignya.append(data)
    print(data)
    time.sleep(2)



print(fignya)
print(errors)




