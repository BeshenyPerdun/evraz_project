import json

file2 = open('gfile.json', 'r', encoding='utf-8')

dats_mas = json.load(file2)

datchik1 = dats_mas[0]
dat1_lib = {}
datchik2 = dats_mas[1]
datchik3 = dats_mas[2]
datchik4 = dats_mas[3]

print(datchik1)
print(datchik2)
print(datchik3)
print(datchik4)

for i in range(0,len(datchik1)):
    dat1_lib



print(dats_mas)