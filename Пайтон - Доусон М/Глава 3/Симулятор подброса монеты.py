import random

# Симулятор подбрасываня монеты 100 раз!
avers = 0
revers = 0


for i in range(100):
    a = random.randint(1, 2)
    if a == 1:
        avers += 1
    else:
        revers += 1

print(f'Решка выпала {avers} раз, а орёл выпал {revers} раз.')
print("Мы играем в идеальном мире в идеальныз условиях и ребра не выподало!")


if __name__ == "__main__":
    input("\n\nНажмите Enter чтобы выйти. ")