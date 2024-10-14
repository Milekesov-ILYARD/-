import random

WORDS = ("Вальгалла", "Жуть", "Умник", "Страх", "Страж", "Ужас", "Улучшение", "Безумие", "Благородство", "Мироздание")

start_words = list(WORDS[:])
finish_words = []
a = ''
b = 0

while start_words:
    b = len(start_words) - 1
    a = start_words.pop(random.randint(0, b))
    finish_words.append(a)

for i in finish_words:
    print(i)


if __name__ == "__main__":
    input("\n\nНажмите Enter чтобы выйти. ")
