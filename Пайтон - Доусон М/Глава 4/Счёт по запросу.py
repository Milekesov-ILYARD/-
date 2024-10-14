# Программа счёта чисел

print("\nЭта программа считает числа по введённым вами параметрам.")
print("Давайте попробуем.")

try:
    first = int(input('\nВведите начальное число: '))
    finish = int(input('Введите ограничивающее число(конечное): '))
    step = int(input('Введите шаг счёта чисел: '))
except:
    print('\nДаннын введены не корректно')
else:
    print("Посчитаем: ")
    for i in range(first, finish + 1, step):
        print(i, end=" ")




if __name__ == "__main__":
    input("\n\nНажмите Enter чтобы выйти. ")
