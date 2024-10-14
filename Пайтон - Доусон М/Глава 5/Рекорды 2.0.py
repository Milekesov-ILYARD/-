# Демонстрирует вложенные последовательнысти

scores = []
choise = None

while choise != 0:
    print(
        '''
        Рекорды 2.0
        0 -  Выйти
        1 - Показать рекорды
        2 - Добавить рекорд
        
        '''

    )
    choise = input("Ваш выбор: ")
    print()
    # Выход
    if choise == '0':
        print("До свидания")
    # Вывод таблицы рекордов
    elif choise == '1':
        print("Рекорды:\n")
        print('ИМЯ\tРЕЗУЛЬТАТ')
        for entry in scores:
            score, name = entry
            print(f'{name}\t{score}')

    elif choise == '2':
        name = input('Впишитк имя игрока: ')
        try:
            score = int(input('Введите его езультат: '))
        except:
            print("Данные введены не корректно.")
        else:
            entry = (score, name)
            scores.append(entry)
            scores.sort(reverse=True)
            scores = scores[:5] # В списке осаётся только пять рекордов
    else:
        print("Извините в меню нет пункта", choise)

if __name__ == "__main__":
    input("\n\nНажмите Enter чтобы выйти. ")
