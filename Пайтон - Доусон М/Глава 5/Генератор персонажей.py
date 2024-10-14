
def display_dict(dictsionary):
    if type(dictsionary) == type({}):
        for i in dictsionary:
            try:
                print(f'{i.capitalize()} : {dictsionary[i]}')
            except:
                print(f'{i} : {dictsionary[i]}')
    else:
        print("Введённые данные не имеют тип - словарь.")

def examination_value_character(value):
    if value == '1':
        value = "сила"
    elif value == '2':
        value = 'здоровье'
    elif value == '3':
        value = 'интелект'
    elif value == '4':
        value = 'мудрость'
    elif value == '5':
        value = 'ловкость'
    return value


points = 35
characteistics = {
    "сила" : 1,
    "здоровье" : 1,
    "интелект" : 1,
    "мудрость" : 1,
    "ловкость" : 1
}

chose_1 = ''
chose_2 = None
counters = 0
print("\nДобро пожаловать в РПГ гнгератор персонажа.\n")

name = input("Введите имя вашего персонажа: ")

choise = None
while choise != '0':
    print(f'\nХарактеристики героя {name}: ')
    print(f'Свободных очков характеристик: {points}\n')
    print(display_dict(characteistics))
    print(
        '''
        Доступные действия?
        0 - Выйти
        1 - Изменить имя персонажа
        2 - Добавить очки к стату
        3 - Вернуть очки характиистик в свободные
        4 - Узнать класс персонажа
        5 - Сохранить песонажа (Ещё не реализовано)
        6 - Загрузить персонажа (Ещё не реализовано)
        '''
    )
    choise = input("Ваш выбор: ")
    print()
    if choise == "0":
        print("До свидания.")

    elif choise == "1":
        print('Вы решили изменить имя персонажа, вы уверенны в своём решении?')
        print("Если уверенны введите: да")
        print("Если вы передумали или ошиблись пунктом меню, введите любой другой ваиант.")
        chose_1 = input("\nВведите ваш выбор: ")
        if chose_1.lower() == 'да':
            name = input('Введите новок имя персонажа: ')
            print(f'\nТеперь его зовут {name}!')
        else:
            print("\nВы решили не переименовывать героя.")
            print(f'Его всё ещё зовут {name}!')

    elif choise == "2":
        if points > 0:
            print("\nВы хотите усилить своего героя добавив ему очков в характеристики.")
            print("Вы можете взять их из свободных очков характеристик.")
            print(f'Свободных характеисик у вас сейчас {points}')
            while chose_2 != 0:
                try:
                    counters += 1
                    if counters > 10:
                        counters = 0
                        break
                    print("\nЕсли хотите выйдти нажмите: 0")
                    chose_2 = int(input('Введите сколько очков вы хотите добавить:'))
                    if chose_2 > points:
                        print('У вас нет стольо свободных баллов')
                        raise ValueError
                except:
                    print('\nОшибка в ведённых данных')

                else:
                    while chose_1 not in characteistics:
                        print("Введите название характеристики или соответствующий ей номер")
                        print("сила - 1\nздоровье - 2\nинтелект - 3\nмудрость - 4\nловкость - 5")
                        print("Если хотите вййдти введите: 0")
                        chose_1 = input("\nВведите ваш выбор: ")

                        if chose_1 == '0':
                            break
                        else:
                            examination_value_character(chose_1)
                            chose_1 = chose_1.lower()

                        if chose_1 in characteistics:
                            characteistics[chose_1] += chose_2

                        else:
                            print("Такой характеристики у вашего персонажа нет.")
                            counters += 1
                            if counters > 10:
                                counters = 0
                                break


                if chose_1 == '0':
                    chose_1 = ''
                    chose_2 = None
                    counters = 0
                    break


        else:
            print('\nУ вас нет свободных очков характеистик.')
            print("Что бы получить свободные баллы попробуйте обратиться в пункт меню:")
            print("3 - Вернуть очки характиистик в свободные")

    else:
        print("Извините такой пункт ещё не реализован", choise)



if __name__ == "__main__":
    input("\n\nНажмите Enter чтобы выйти. ")