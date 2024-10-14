# Демонстрирует списочные методы

scores = []
choise = None

while choise != 0:
    print(
        '''
        Рекорды:
        0 - Выйти
        1 - Показать рекроды
        2 - Добавить рекорд
        3 - Удалить рекорд
        4 - Сортировать список
        '''
    )
    choise = input("Ваш выбор: ")
    print()
    if choise == 0:
        print("До свидания.")
    elif choise == 1:
        print("Рекорды:")
        for score in scores:
            print(score)
    elif choise == 2:
        try:
            score = int(input("Введите свой рекорд"))
        except:
            print("Данные введены не корректно попробуйте ещё раз.")
        else:
            scores.append(score)
    elif choise == 3:
        try:
            score = int(input("Какой из рекордов удалить?: "))
        except:
            print("Данные введены не корректно.")
        else:
            if score in scores:
                scores.remove(score)
            else:
                print(f"Результат {score} не содержится в списке рекордов.")
    elif choise == 4:
        scores.sort(reverse=True)
    else:
        print(f"Извините, такого пункта,{choise}, нет в меню.")

if __name__ == "__main__":
    input("\n\nНажмите Enter чтобы выйти. ")


