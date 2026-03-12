num1 = 5
num2 = 9
correct_answer = num1 * num2
user_answer = int(input(f"Скільки буде {num1} * {num2}?"))
if user_answer == correct_answer:
    print(f"Вірна відповідь!")
else:
    print(f"Не вірно - {correct_answer}.")


    