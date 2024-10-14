import random

diel_1 = random.randint(1, 6)
diel_2 = random.randrange(6) + 1
total = diel_1 + diel_2
print(f'При вышем броске выпало {diel_1} и {diel_2} очков, в сумме вы набрали {total}.')
if __name__ == "__main__":
    input("\n\nНажмите Enter чтобы выйти. ")

