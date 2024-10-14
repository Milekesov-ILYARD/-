# Компьютер выбирает случайное слово из набора а игрок его должен угадать
import random

print("\n\tДобро пожаловать в \"Угадайку\"\n")
print("Это игра с отгадыванием слова.")
print("Вам будет дана возможность получить подсказки.")
print("Вы паяnm раз сможете узнать наличие буквы в слове и её количество")
print('Если буква будет в слове вы получите "Да"')
print('Если бувы не будет в слове вы получите то "Нет"')

WORDS = ('кот', 'вода', 'море', "сахар", "вилка", "картошка")
word = random.choice(WORDS)

counters = 0
answer = ''

print("\nЕсли хахотите выйдти из игры не вводя ни чего нажмите Enter")
while counters <= 5:
    answer = input('\nВедите ваш вариант буквы входящей в слово: ')
    if answer == '':
        break
    elif len(answer) > 1:
        print('Введите одну букву.')
    elif answer.lower() in word:
        print(f'"Да", её количество {word.count(answer)}')
        counters += 1
    else:
        print('"Нет')
        counters += 1

if counters != 0:
    print("Если хахотите выйдти из игры не вводя ни чего нажмите Enter")
while answer.lower() != word and answer != '':
    answer = input('\nВедите ваш вариант слова: ')
    if answer.lower() != word:
        print("Вы ошиблись, попробуйте ещё раз.")

if answer.lower() == word.lower():
    print("\nДа именно так! Вы отгадали!\n")

print("\nСпасибо за игру.")

if __name__ == "__main__":
    input("\n\nНажмите Enter чтобы выйти. ")





