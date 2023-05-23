ru_en = {}
with open('en-ru.txt', "r", encoding='utf-8') as file:
    for a in file:
        en_word, ru_words = a.split('-')
        for ru_word in ru_words.split(', '):
            if ru_word not in ru_en:
                ru_en[ru_word] = [en_word]
            else:
                ru_en[ru_word].append(en_word)
with open('ru-en.txt', 'w', encoding='utf-8') as file:
    for ru_word in sorted(ru_en):
        en_words = ', '.join(sorted(ru_en[ru_word]))
        file.write(f'{ru_word}-{en_words}\n')
