import json

file2 = open('gfile.json', 'r', encoding='utf-8')

dats_mas = json.load(file2)

print(dats_mas)