def calculate(text_input):
    if '+' in text_input:
        return int(text_input[0]) + int(text_input[2])
    elif '-' in text_input:
        return int(text_input[0]) - int(text_input[2])
    elif '*' in text_input:
        return int(text_input[0]) * int(text_input[2])
    elif '/' in text_input:
        return int(text_input[0]) / int(text_input[2])
    elif '~' in text_input:
        return [int(text_input[0]) // int(text_input[2]), int(text_input[0]) % int(text_input[2])]


print("Welcome to the Python calculator!")


calculations_freqs = int(input('How many calculations do you want to do? '))


for calc in range(calculations_freqs):
    user_input = input("What do you want to calculate? ")
    result = calculate(user_input)
    if type(result) == list:
        print(f"The answer is {result[0]}\nThe remainder is {result[1]}")
    else:  print(f"The answer is {result}")
