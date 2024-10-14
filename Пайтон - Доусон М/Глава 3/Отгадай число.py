#Игрок отгадывет случайное число от 1-го до 100-а
import random
print("\tДобро пожаловать в игру \"Отгадай число\"! ")
print("\nЯ загадал натуральное число, из дапазона от 1 до 100.")
print("Посторайся отгадать его за минимальное количество попыто\n")
the_namber = random.randint(1, 100)
guess = 0
tries = 0

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
        elif tries > 25:
            break
        else:
            print('Больше!')

print("Вы победили, загаданное число было", the_namber)
print(f"Вы потратили на отгадывание всего лишь {tries} попыток!\n")

if __name__ == "__main__":
    input("\n\nНажмите Enter чтобы выйти. ")