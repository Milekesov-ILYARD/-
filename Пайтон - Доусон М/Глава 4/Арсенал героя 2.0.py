# Демонстирует создание кортежа

inventory = ("меч",
             "кольчуга",
             "щит",
             "целебное снадобье")
print('\nИтак в вашем арсенале:')
for iten in inventory:
    print(iten)
input("\nНажмите Enter чтобы продолжить.")

# Найдём длинну кортежа
print("\nСейчас в вашем распоряжении", len(inventory), "предмета/-ов.")
input("\nНажмите Enter чтобы продолжить.")

print("\nЕсть ли целебное снадобье с собой на случай ранения?")
if "целебное снадобье" in inventory:
    print("Всё отлично, вы ещё поживёте и повоюете!")
else:
    print("Кажись тяжко придётся.")

index = 100
while index > len(inventory) - 1 or index < -len(inventory):
    try:
        index =  int(input('\nВведите индекс одного из предметов арсенала: '))
    except:
        print("Данные введены не корректно.")
    else:
        if index > len(inventory) - 1 or index < -len(inventory):
            print("Под данным индексом ничего не обнаружено, попробуйте другой индекс.")
        else:
            print(f"\nПод индексом {index} в инвентаре находиться {inventory[index]}")


print('\nДавайте посмотрим на выборку, от одного предмета до другого (это называется срез)')

start = -100
finish = 100

while True:
    try:
        print('Введите индекс одного из предметов арсенала: ')
        start =  int(input("\nНачальная позиция (меньшее значение идекса для среза): "))
        finish = int(input("\nКонечная позиция (большее значение идекса для среза): "))
    except:
        print("Данные введены не корректно.")
    else:
        print(f'Срез инвентрая [{start} : {finish}] выглядит как: ', end=' ')
        print(inventory[start:finish])
        break
input("\nНажмите Enter чтобы продолжить.")

chest = ('золото','драгоценные камни')
print("\nВы нашли ларец, вот что в еём есть:")
print(chest)

print("\nВы пиобщили содежимое ларца к своему арсеналу:")
inventory += chest
print("Теперь в вшем распоряжении:")
print(inventory)

if __name__ == "__main__":
    input("\n\nНажмите Enter чтобы выйти. ")
