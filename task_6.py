stored_name = "svitlana"
user_input = input("Enter your name:")
result = user_input.casefold() == stored_name.casefold()
print(f"Результат перевірки: {result}")