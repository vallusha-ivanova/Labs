import json
with open('100. json.json', 'r', encoding='utf8') as f:
 data = json.load(f)
 for i in range(len(data.get('products'))):
     k = data.get('products')[i]
     print('Название: ' + str(k.get('name')))
     print('Цена: ' + str(k.get('price')))
     print('Вес: ' + str(k.get('weight')))
     if str(k.get('name')):
         print('В наличии')
     else:
         print('Нет в наличии!', '\n')

