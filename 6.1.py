# Ввод предложения
sentence = input("Введите предложение: ")

# Вывод букв, стоящих на четных местах
print("Буквы на четных местах:")
for i in range(1, len(sentence), 2):  # Индексы четных мест: 1, 3, 5, ...
    if sentence[i].isalpha():  # Проверка, что символ — это буква
        print(sentence[i])