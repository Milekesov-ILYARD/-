class NumbersError(Exception):
    pass
class EvenError(NumbersError):
    pass
class NegativeError(NumbersError):
    pass

def no_even(numbers):
    if all(x % 2 != 0 for x in numbers):
        return True
    raise EvenError("В списке не должно быть чётных чисел")

def no_negative(numbers):
    if all(x >= 0 for x in numbers):
        return True
    raise NegativeError("В списке не должно быть отрицательных чисел")


def main():
    print("Введите числа в одну строку через пробел:")
    try:
        numbers = [int(x) for x in input().split()]
        if no_negative(numbers) and no_even(numbers):
            print(f"Сумма чисел равна: {sum(numbers)}.")
    except NumbersError as e:  # обращение к исключению как к объекту
        print(f"Произошла ошибка: {e}.")
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}.")


if __name__ == "__main__":
    main()