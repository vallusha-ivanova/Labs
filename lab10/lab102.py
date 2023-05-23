import json
new_data={'name':input("Новый продукт"), 'price': input("цена"), 'available':input('наличие'),'weight':input('вес')}
with open("100. json.json", encoding='utf8') as f:
    data = json.load(f)
    data['products'].append(new_data)
    with open('100. json.json', 'w', encoding='utf8') as outfile:
        json.dump(data, outfile, ensure_ascii=False, indent=4)