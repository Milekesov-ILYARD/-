#Демонстрирует работу фунуции len() и оператора in

message = input("Введите текст: ")

T = 0

print('\nдлинна введёного вами текста составляет:', len(message))
print('\nСамая частая согласная, \"Т\"')

if "т" in message:
    for i in message.lower():
        if i == 'т':
            T += 1
    print(f'...встречается в вашем тексте {T} раз.')
else:
    print('...не встречаеся в вашем тексте.')

if __name__ == "__main__":
    input("\n\nНажмите Enter чтобы выйти. ")