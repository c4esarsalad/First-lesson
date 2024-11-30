meme_dictionary = {"КРИНЖ": "Стыдно",
"ЛОЛ": "Очень смешно",
"РОФЛ": "Шутка",
"КРИПОВЫЙ":"Страшный"}

word = input("Введите непонятное слово (большими буквами!): ")

if word in meme_dictionary.keys():
    print("Это значит " + meme_dictionary[word])
else:
    print("Даже я незнаю что это значит")
