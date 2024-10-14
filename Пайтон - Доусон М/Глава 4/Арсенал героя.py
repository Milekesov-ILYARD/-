# Демонстирует создание кортежа

inventory = ()

if not inventory:
    print('Вы обезоруженны.')
input("\nНажмите Enter чтобы продолжить.")

inventory = ("Меч",
             "Кольчуга",
             "Щит",
             "Целебное снадобье")
print('\nВыведем содержимое кортежа:')
print(inventory)
print('\nИтак в вашем арсенале:')
for iten in inventory:
    print(iten)

if __name__ == "__main__":
    input("\n\nНажмите Enter чтобы выйти. ")