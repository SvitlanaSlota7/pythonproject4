input_string = "my"
if len(input_string) < 2:
    result = ""
else:
    first_two = input_string[0:2]
    last_two = input_string[-2:]
    result = first_two + last_two
print(f"String: '{input_string}'")
print(f"Expected Result: '{result}'")