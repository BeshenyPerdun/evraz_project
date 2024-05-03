import json
import datetime
from datetime import date
import random
import time

file2 = open('gfile.json', 'r', encoding='utf-8')

dats_mas = json.load(file2)


errors = 0

def dats():
    data = date.today()
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
    file = open('file.json', 'w', encoding='utf-8')
    json.dump(fignya, file, ensure_ascii=False)
    file.close()
    time.sleep(3)


print(fignya)
print(errors)




