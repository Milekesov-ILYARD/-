#Игрок отгадывет случайное число от 1-го до 100-а
import random
print("\tДобро пожаловать в игру \"Отгадай число\"! ")
print("\nЯ загадал натуральное число, из дапазона от 1 до 100.")
print("На отгадывание даётся 9 Попыток!")
print("Посторайся отгадать его за минимальное количество попыто\n")
the_namber = random.randint(1, 100)
guess = 0
tries = 0
loose = 0

while guess != the_namber:
    try:
        tries += 1
        guess = int(input('Ваше предположение: '))
    except:
        print("Данные введены не корректно!")
        if tries > 15:
            break
    else:
        if guess > the_namber:
            print('Меньше!')
        elif tries > 9:
            loose += 1
            break
        else:
            print('Больше!')

if loose != 0:
    print('Вы проиграли истратив все попытки!')
    print(f"Загаданное число было {the_namber}!")
else:
    print("Вы победили, загаданное число было", the_namber)
    print(f"Вы потратили на отгадывание всего лишь {tries} попыток!\n")


if __name__ == "__main__":
    input("\n\nНажмите Enter чтобы выйти. ")