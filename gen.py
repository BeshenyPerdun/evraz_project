import time
import random
import json

nd = 4

dats = {}
dats2 = {}

datchik1 = []
datchik2 = []
datchik3 = []
datchik4 = []





while True:
    #Температура воды например
    for i in range(0, nd):
        b = random.randint(1,3)
        if b == 1 or b == 2:
            dats['d'+ str(i+1)] = str(random.randint(30,100))
        elif b == 3:
            dats['d'+ str(i+1)] = str(random.randint(500, 1000))
    for k in range(0, nd):
        b = random.randint(1,3)
        if b == 1 or b == 2:
            dats2['d'+ str(k+1)] = str(random.randint(30,100))
        elif b == 3:
            dats2['d'+ str(k+1)] = str(random.randint(500, 1000))
    datchik1.append(dats['d1'])
    datchik2.append(dats['d2'])
    datchik3.append(dats['d3'])
    datchik4.append(dats['d4'])




    # him_ulav_ceh = {
    #     'datchik1' : {
    #         'data1': str(datchik1[1]),
    #         'data2': str(datchik1[2])
    # }}



    
    dats_massive = [dats, dats2]
    datchiks_massive = [datchik1, datchik2, datchik3, datchik4]
    print(dats)
    file2 = open('gfile.json', 'w', encoding='utf-8')
    file = open('file.json', 'w', encoding='utf-8')
    json.dump(dats_massive, file, ensure_ascii=False)
    json.dump(datchiks_massive, file2, ensure_ascii=False)
    file.close()
    time.sleep(3)
   






