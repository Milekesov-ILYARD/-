# Демонстрирует как создавать новые строки из исходных с помощью цикла for

massage = input('Введите текст: ')
new_message = ''
VOWELS =  "аеiоuаеёиоуыэюя"

print()
for letter in massage:
    if letter.lower() not in VOWELS:
        new_message += letter
        print('Созданна новая строка:', new_message)
print("Вот ваш текст с изятыми гласными буквами: .", new_message)

# Почему цикл выводит с пробелами вместо гласнвх, происходит конкатенация строк откуда пробелы?

if __name__ == "__main__":
    input("\n\nНажмите Enter чтобы выйти. ")