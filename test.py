"""
# function with return value
def cube(num):
    return num * num * num


num = float(input("enter the value of: "))
print(f" {num} cube is: ", cube(num))


# calculator with function
def calculator():
    print("Welcome to the calculator")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operator = input("Enter the operation (+, -, *, /,%): ")

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        result = num1 / num2
    else:
        print("Invalid operator entered")
        return

    print(f"{num1} {operator} {num2} = {result}")
    calculator()


calculator()

# calculate no using f string
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
result = num1 + num2
print(f"{num1} {num2} = {result}")


# find the maximum number
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

max_num = max_num(num1, num2, num3)
print("Maximum number is: ", max_num)

# dictonary
Month_Conversions = {
    "jan": "january",
    "feb": "february",
    "mar": "march",
    "apr": "april",
    "may": "may",
    "jun": "june",
    "jul": "july",
    "aug": "august",
    "sep": "september",
    "oct": "october",
    "nov": "november",
    "dec": "december",
}

month = input("Enter the month: ")
print(Month_Conversions.get(month, "Not a valid key"))

# while loop

i = 1
while i <= 10:
    print(i)
    i += 1

print("loop is over")

# Guessing Game using While loop
secret = input("Enter the secret: ")
guess_limit = int(input("Enter the guess limit: "))
guess = input("Enter the guess: ")
guess_count = 1
out_of_guesses = False

while guess != secret and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input("Enter the guess again: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("You lose!")
else:
    print("Correct guess")

# for loop

for i in range(1, 6):
    print(i)

friends = ["suresh", "ramesh", "sita"]
for friend in friends:
    print(friend)

for index in range(len(friends)):
    print(friends[index])


# Raise to power using function and for loop
def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result


base_num = float(input("Enter the base number: "))
pow_num = int(input("Enter the power number: "))

print(f"{base_num} to the power of {pow_num} is: ", raise_to_power(base_num, pow_num))

# 2D List

num_list = [[1, 2, 3, 4], [5, 6, 7, 8], [10, 11, 12, 13]]

for row in num_list:
    for col in row:
        print(col)
    print(row)


# build a translater


def translater(text):
    result = ""
    for letter in text:
        if letter.lower() in "aeiou":
            if letter.isupper():
                result += "G"
            else:
                result += "g"
        else:
            result += letter
    return result


print(translater(input("Enter the text: ")))
"""