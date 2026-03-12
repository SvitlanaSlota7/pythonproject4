input_string = "x"
if len(input_string) < 2:
   result = ""
else:
   # цей блок не буде виконано оскільки 'x' має довжину 1 і весь блок else  ігнорується
   first_two = text[:2]
   last_two = text[-2:]
   result = first_two + last_two
print(f"String: '{input_string}'")
print(f"Expected Result: '{result}'")