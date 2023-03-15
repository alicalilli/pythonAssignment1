### task3

# Define the divide() and chars() functions
def divide(x, y):
    return [x[a:a+y] for a in range(0, len(x), y)]

def chars(substring):
    unique_chars_str = ""
    for char in substring:
        if char not in unique_chars_str:
            unique_chars_str += char
    return unique_chars_str

while True:
    x = input("Please input a sequence of characters: ")
    y = input("Please input a digit: ")
    # Here we check if the y is digit and greater than 0
    if y.isdigit() and int(y) > 0 and len(x) % int(y) == 0:
        # Here we convert input y into an integer
        y = int(y)
        break
    else:
        print("Please enter a valid input for y.")

# Call the divide() function to split the string into substrings
substrings = divide(x, y)

# Call the chars() function on each substring to get the unique characters
for substring in substrings:
    unique_chars = chars(substring)
    print(unique_chars)
