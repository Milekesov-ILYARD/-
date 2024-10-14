print("Эта программа высчитывает посную цену автомобиля")
print("Она учитывает: налог, регистационный сбор, агентский сбор, цену доставки машины по месту назначения\n")
tax = 0
registration_fee = 20000
agency_fee = 15000
shipping_cost = 10000
total_amount = 0
try:
    initial_cost = int(input("Введите изначальную стоимость машины: "))
except:
    print("Произошла ошибка попробуйте заново")
else:
    tax = initial_cost * 0.15
    total_amount = initial_cost + tax + registration_fee + agency_fee + shipping_cost
    print("\nСтоимость машины с учётом наценок:", total_amount)
if __name__ == "__main__":
    input("\n\nНажмите Enter чтобы выйти. ")

