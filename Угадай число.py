import random
a = 20
s = random.randint(1,10)
t = 0

if t == 0:
    print('Было загадано число, Попытайтесь его угадать.\n Введите 777 если решите просто закончить!')

while s != a:
    t += 1
    try:
        a = int(input("Введите число: "))
    except ValueError:
        print('Вы ввели не число!')
    except:
        print('У нас что - то пошло не так!')
        break

    else:
        if a <= 0:
            print('Введите положительное число.')
        elif a == 777:
            print('Вы решили закончить игру!')
            break
        elif a > 100:
            print('Вы ввели слишком большое число.')
        elif 100 > a > 10:
            print('Введите число поменьше.')
        elif a < 11 and a < s:
            print('Вы близко, но нужно чуть больше')
        elif a < 11 and a > s:
            print('Вы близко, но нужно чуть меньше')
        elif t > 7 and t < 9:
            print('Загадано число от 1 до 10')
        elif t > 12:
            print('Введите 777 если решите просто закончить!')
        elif t > 21:
            break

if s == a:
    print("Поздровляю вы справились и угадалм число, ведь оно было равно", s, '!!')
print("Игра завершена!")




