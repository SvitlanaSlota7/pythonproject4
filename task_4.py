phone_number = input("Введіть ваш номер телефону")
if len(phone_number) == 10 and phone_number.isdigit():
     print(f"Номер '{phone_number}' має правильний формат")
else:
    print(f"Номер '{phone_number}' має невірний формат. Перевірте довжину та символи")