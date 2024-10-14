#

print('\tПриветствую!')
print("Видимо вы решили попробовать, угадает ли компьютор задуманное вами число?")
print("Давайте попробуем, но загаданное число должно быть в диапазоне от 1 до 100.")
print("Иначе ни чего не получится!\n")

max_number = 100
min_number = 1
middle_number = 50
tries = 1
counter = 0

guess_number = 0
error = 0

while guess_number == 0:
    try:
        guess_number = int(input('Введите число из допазона от 1 до 100: '))
        counter +=1
    except:
        print("Вы ввели не корректные данные!")
        error += 1
        if error > 7:
            break

while middle_number != guess_number:
    if guess_number < 1:
        if counter > 0:
            print('\nЧисло Меньше одного!')
        break
    elif guess_number > 100:
        print('\nЧисло больше Ста!')
        break
    elif middle_number > guess_number:
        max_number = middle_number
        middle_number = middle_number // 2
        tries += 1
    elif middle_number < guess_number:
        middle_number = (middle_number + max_number) // 2
        tries += 1
    else:
        print('')
        break

if guess_number == middle_number:
    print('\nКомпьтер смог угадать загаданное число!!!')
    print(f'Это число {middle_number}!\nИ угадал он с {tries}-го раза!')
else:
    print("\nМы (Разработчик и компьютер) не смогли отгадать число, ведь что-то пошло не так!")

if __name__ == "__main__":
    input("\n\nНажмите Enter чтобы выйти. ")
