name = input("Введите имя: ")
group = input("Введите группу: ")
age = int(input("Введите возраст: "))
interests = input("Ваши интересы: ")

print("\n________ МОЯ ВИЗИТКА ________")
print(f"Имя: {name}")
print(f"Группа: {group}")
print(f"Возраст: {age}")
print(f"Интересы: {interests}")
print("____________________________")

def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

temperature = 25
print(
    f"{temperature} °C = "
    f"{celsius_to_fahrenheit(temperature)} °F"
)

def calculate_discount(price, discount):
    return price - (price * discount / 100)

price = 1500
discount = 20
final_price = calculate_discount(price, discount)

print(f"Цена: {price} руб.")
print(f"Скидка: {discount}%")
print(f"Итоговая стоимость: {final_price} руб.")

def normalize_name(name):
    return name.strip().title()

raw_name = "   иВАН иВАНОВ   "
print(f"Нормализованное имя: {normalize_name(raw_name)}")