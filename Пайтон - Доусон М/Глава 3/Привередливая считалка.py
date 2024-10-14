#Демонстрирует работу break и  continue
count = 0
while True:
    count += 1
    if count > 10:
        break
    if count == 5:
        continue
    print(count)

if __name__ == "__main__":
    input("\n\nНажмите Enter чтобы выйти. ")