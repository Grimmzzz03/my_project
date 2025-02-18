
import random
import sys


def main():
    """Main entry point of the program"""
    #rectangle()
    #calculator()
    #print(sys.argv)
    #dice()
    #no_guess_game()
    #fruit_salad()
    #list_deque()
    #build_stack()
    #reverse_polish_calc()
    #color_selector()
    #count_digits()
    #sort_dict_value()
    #c_char()
    #c_word()
    #word_in_file()
    #object_set()
    #num_sets()
    #fibonacci()
    #palindrome()
    #statistics()
    #factorial()
    #bubble_sort()
    #merge_sort()
    

# area and circumference of rectangle
def rectangle():
    """
    Calculate the area and circumference of a rectangle given the length and
    width.
    """
    length = int(input("Enter the length of rectangle: "))
    breath = int(input("Enter the breath of rectangle: "))
    # Check if the user has entered negative values
    if length < 0 or breath < 0:
        print(f"The values you enter are negative values: {length},{breath}")
    else:
        # Calculate the area and circumference of the rectangle
        area = length * breath
        circumference = 2 * (length + breath)
        print(f"area of rectangle is: {area}")
        print(f"circumference of rectangle is: {circumference}")


# calculator
def calculator():
    """
    A simple command line calculator.
    """
    while True:
        # Get two numbers from the user
        num_1 = int(input("Enter the 1st value: "))
        num_2 = int(input("Enter the 2nd value: "))

        # Get the operand from the user
        operand = input("Enter the operand (+, -, *, /, %) or q to quit: ")

        # Check if the values are negative
        if num_1 < 0 or num_2 < 0:
            print(f"The values you enter are negative values: {num_1},{num_2}")

        # Check if the values are valid
        else:
            pass

        # Perform the operation
        match operand:
            case "+":
                # Addition
                total = num_1 + num_2
                print(f"The sum of two numbers is: {total}")
            case "-":
                # Subtraction
                difference = num_1 + num_2
                print(f"The difference between two numbers is: {difference}")
            case "*":
                # Multiplication
                multiply = num_1 * num_2
                print(f"The multiplication of two numbers is: {multiply}")
            case "/":
                # Division
                if num_2 == 0:
                    print("You can't divide by zero")
                else:
                    divide = num_1/num_2
                    print(f"The division between two numbers is: {divide}")
            case "%":
                # Modulus
                if num_2 == 0:
                    print("You can't divide by zero")
                else:
                    modulus = num_1 % num_2
                    print(f"The modulus between two numbers is: {modulus}")
            case "q":
                # Quit
                break
            case _:
                # Invalid operand
                print("You entered a wrong operand")
                break

    print("Thanks for using calculator")


def dice():
    """
    Simulate rolling three dice with different number of sides and ask the user if they want to play again.
    """
    while True:
        # Roll a six-sided die
        dice_1 = random.randint(1, 6)
        # Roll a ten-sided die
        dice_2 = random.randint(1, 10)
        # Roll a twenty-sided die
        dice_3 = random.randint(1, 20)

        # Display the results of the dice rolls
        print(f"Dice 1: {dice_1}")
        print(f"Dice 2: {dice_2}")
        print(f"Dice 3: {dice_3}")

        # Ask the user if they want to play again
        play_again = input("Do you want to play again? (y/n): ")
        if play_again.lower() == "y":
            continue
        else:
            break

    print("Thanks for playing")


def no_guess_game():
    """
    This function will play a no guessing game
    A user will enter a number and the program will check
    if the number is in the given range or not.
    Then the program will generate a random number and will
    check if the user's guess is correct or not.
    """
    while True:
        guess_no = int(input("Enter a number between 1 to 20: "))
        # check if the number is in the given range
        if guess_no < 1:
            print("Please Enter the positive no and num should not be greater than 20")
            continue
        elif guess_no > 20:
            print("Please enter no between 1 to 20")
            continue
        else:
            print(f"The guess no enter by user is: {guess_no}")
            break

    # generate a random number
    hidden_no = random.randrange(1, 21)
    print(f"hidden no is: {hidden_no}")

    # check if the user's guess is correct or not
    if hidden_no == guess_no:
        print("You Won!")
    else:
        print("You Lose!")

    print("Thanks for playing")


def fruit_salad():
    """
    This function takes a list of fruits and returns a list of 3 fruits randomly selected.
    :return: a list of 3 fruits
    """
    fruits = ['mango','banana','papaya','apple','pineapple','guava','peach','strawberry','blueberry']
    # select 3 fruits from the list of fruits
    salad = random.sample(fruits, 3)
    print("the fruits selected to salad are:")
    # print each fruit in the list
    for fs in salad:
        print(f"\t{fs}")


def list_deque():
    """
    This function uses the deque data structure to add and remove elements
    from the left and right sides. It also shows how to rotate and extend the deque.
    """
    from collections import deque
    # create a deque with some elements
    d = deque(['a', 'b', 'c', 'd', 'e'])
    print(d)
    # add an element to the right side
    d.append('f')
    print(d)
    # add an element to the left side
    d.appendleft('g')
    print(d)
    # remove an element from the right side
    d.pop()
    print(d)
    # remove an element from the left side
    d.popleft()
    print(d)
    # rotate the deque 2 positions to the right
    d.rotate(2)
    print(d)
    # rotate the deque 1 position to the left
    d.rotate(-1)
    print(d)
    # add multiple elements to the right side
    d.extend(['g', 'h', 'i'])
    print(d)
    # add multiple elements to the left side
    d.extendleft(['j', 'k', 'l'])
    print(d)


def build_stack():
    """
    This function creates an empty stack and then
    repeatedly prompts the user to choose an action
    to perform on the stack until the user chooses
    to quit.
    """
    stack = []
    while True:
        if stack:
            print("Stack:", stack)
        else:
            print("Stack is empty")
        print("1. Push")
        print("2. Pop")
        print("3. Peek")
        print("4. Is Empty")
        print("5. Quit")
        choice = input("Enter your choice: ")
        if choice == "1":
            item = input("Enter item to push: ")
            # add the item to the top of the stack
            stack.append(item)
        elif choice == "2":
            if stack:
                # remove the top item from the stack
                item = stack.pop()
                print("Popped item:", item)
            else:
                print("Stack is empty")
        elif choice == "3":
            if stack:
                # show the top item from the stack without removing it
                print("Peeked item:", stack[-1])
            else:
                print("Stack is empty")
        elif choice == "4":
            # check if the stack is empty
            print("Is empty:", not stack)
        elif choice == "5":
            # break out of the loop and exit the function
            break
        else:
            print("Invalid choice")


def reverse_polish_calc():
    """
    This function implements a Reverse Polish Notation (RPN) calculator.
    It uses a stack to store the numbers and operators.
    The user can enter numbers and operators (+, -, *, /) to perform calculations.
    The result is calculated and printed on the screen.
    """
    stack = []
    print("1. X for Exit\n2. + for addition\n3. - for subtraction\n4. * for multiplication\n5. / for division")
    while True:
        print(stack)
        choice = input("Enter your choice: ")
        if choice == "1":
            break
        elif choice == "2":
            # addition
            a = int(input("Enter the first number: "))
            b = int(input("Enter the second number: "))
            stack.append(a + b)
        elif choice == "3":
            # subtraction
            a = int(input("Enter the first number: "))
            b = int(input("Enter the second number: "))
            stack.append(a - b)
        elif choice == "4":
            # multiplication
            a = int(input("Enter the first number: "))
            b = int(input("Enter the second number: "))
            stack.append(a * b)
        elif choice == "5":
            # division
            a = int(input("Enter the first number: "))
            b = int(input("Enter the second number: "))
            stack.append(a / b)
        else:
            print("Invalid choice")

    if stack:
        # print the result
        print("Result:", stack.pop())
    else:
        print("Stack is empty")


def color_selector():
    """
    Display a list of colors and allow the user to select one by entering a number.
    Prints the selected color.
    """
    # List of available colors
    colors = ["red", "green", "blue", "yellow", "white", "black"]

    # Display the list of colors
    for i in range(len(colors)):
        print(f"{i+1}. {colors[i]}")

    # Prompt the user to enter a choice
    choice = input("Enter your choice: ")

    # Validate the input
    if not choice.isdecimal():
        exit(f"We need a number between 1 and {len(colors)}")
    elif int(choice) < 1 or int(choice) > len(colors):
        exit(f"We need a number between 1 and {len(colors)}")
    else:
        # Print the selected color
        print(f"You have selected {colors[int(choice)-1]}")

# count the occurrence of numbers in the list
def count_digits():
    """
    Count the occurrence of each digit (0-9) in a list of numbers.
    """
    numbers = [1234,23,455,678,123,865,7654,4322,789,23345,8765,1000,2230]
    count = [0]*10  # count is a list of 10 zeros
    for num in numbers:
        for char in str(num):
            # int(char) will convert the character to an integer
            # which will be the index for the count list
            count[int(char)] += 1

    for d in range(0,10):
        print(f"{d} occurs {count[d]} times")


def sort_dict_value():
    """
    Sorts a dictionary by its values and prints the sorted results.
    """
    # Dictionary containing names as keys and scores as values
    scores = {
        'rishav': 98,
        'parul': 88,
        'saurbh': 92,
        'prakriti': 96,
    }

    # Print each name and score
    for k, v in scores.items():
        print(f"{k} => {v}")

    # Print sorted scores
    print(f"sorted_score => {sorted(scores.values())}")

    # Sort names by scores and print them
    sorted_names = sorted(scores, key=lambda x: scores[x])
    for s in sorted_names:
        print(f"{s} : {scores[s]}")

    print("-" * 20)

    # Another method to sort names by scores and print them
    for name in sorted(scores.keys(), key=lambda x: scores[x]):
        print(f"{name} : {scores[name]}")


def c_char():
    """
    Count the occurrence of each character in a given text.
    The output will be a dictionary where the keys are characters
    and the values are the number of times the character appears in the text.
    """
    text = """
        this is the very long text.
        okay, it may not be longer than that.
        """
    # create a dictionary to count the occurrence of each character
    count = {}
    # loop through each character in the text
    for character in text:
        # skip the newline character
        if character == '\n':
            continue
        # if the character is already in the dictionary
        elif character in count:
            # increment the count
            count[character] += 1
        else:
            # add the character to the dictionary
            count[character] = 1

    # print the count of each character
    for character in count:
        print(f"{character} => {count[character]}")

    print("-"*20)

    # print the count of each character
    for character in text:
        # if the character is in the dictionary
        if character in count:
            # print the count
            print(f"{character} => {count[character]}")
        else:
            # print 0 if the character is not in the dictionary
            print(f"{character} => 0")

    print("-"*20)
    # print the count of each character in sorted order
    for character in sorted(count):
        print(f"{character} => {count[character]}")


def c_word():
    """
    Count the occurrence of each word in a given list of words.
    The output will be a dictionary where the keys are words
    and the values are the number of times the word appears in the list.
    """
    word = ["tiger", "lion", "elephant", "zebra", "monkey","tiger", "lion", "elephant", "zebra", "monkey","tiger",]
    # create a dictionary to count the occurrence of each word
    count = {}
    # loop through each word in the list
    for w in word:
        # if the word is already in the dictionary
        if w in count:
            # increment the count
            count[w] += 1
        else:
            # add the word to the dictionary
            count[w] = 1

    # print the count of each word
    for w in count:
        print(f"{w} => {count[w]}")

    print("-"*20)

    # print the count of each word
    for w in word:
        # if the word is in the dictionary
        if w in count:
            # print the count
            print(f"{w} => {count[w]}")
        else:
            # print 0 if the word is not in the dictionary
            print(f"{w} => 0")

    print("-"*20)
    # print the count of each word in sorted order
    for w in sorted(count):
        print(f"{w} => {count[w]}")


def word_in_file():
    """
    Analyze the contents of a text file and print various statistics:
    - Number of words
    - Number of unique words
    - Number of characters
    - Number of unique characters
    - Number of lines

    If a filename is passed as a command-line argument, it will be used.
    Otherwise, 'Readme.txt' is used as the default file.
    """
    filename = 'Readme.txt'
    # Check if a filename is provided as a command-line argument
    if len(sys.argv) > 1:
        filename = sys.argv[1]

    try:
        # Open and read the contents of the file
        with open(filename, encoding='utf-8') as f:
            contents = f.read()
    except FileNotFoundError:
        # Handle the case where the file does not exist
        print(f"Sorry, the file {filename} does not exist.")
    else:
        # Split the contents into words and count them
        words = contents.split()
        num_words = len(words)
        print(f"The file {filename} has about {num_words} words.")

        # Create a set of unique words and count them
        unique_words = set(words)
        num_unique_words = len(unique_words)
        print(f"The file {filename} has about {num_unique_words} unique words.")

        # Count the number of characters in the file
        num_characters = len(contents)
        print(f"The file {filename} has about {num_characters} characters.")

        # Create a set of unique characters and count them
        unique_characters = set(contents)
        num_unique_characters = len(unique_characters)
        print(f"The file {filename} has about {num_unique_characters} unique characters.")

        # Split the contents into lines and count them
        # Count the approximate number of lines in the file:
        lines = contents.splitlines()
        num_lines = len(lines)
        print(f"The file {filename} has about {num_lines} lines.")


def object_set():
    """
    Demonstrate the use of sets for storing and manipulating a collection of unique objects.
    """
    # Create a set of planets
    planet = set()
    planet.add("Mercury")
    planet.add("Venus")
    planet.add("Earth")
    planet.add("Mars")
    planet.add("Jupiter")
    planet.add("Saturn")
    print(planet)
    print(f"The initial set of planets in the solar system is {len(planet)}")
    print("-" * 40)

    # Create a new set of planets
    new_planet = set()
    new_planet.add("saturn")
    new_planet.add("Neptune")
    new_planet.add("Uranus")
    print(f"New Planets : {new_planet}")
    print("-" * 40)

    # Demonstrate the use of set operations
    print(f"union of planets : {planet.union(new_planet)}")
    print("-" * 40)
    print(f"difference of planets : {planet.symmetric_difference(new_planet)}")
    print("-" * 40)
    print(f"intersection of planets : {planet.intersection(new_planet)}")
    print("-" * 40)
    planet.update(new_planet)
    print(f" new set of planets : {planet}")
    print(f"The number of planets in the solar system is {len(planet)}")
    print("-" * 40)

    # Demonstrate the use of set methods
    planet.remove("Mars")
    print(f"new set of planets : {planet}")
    print(f"The number of planets in the solar system is {len(planet)}")
    print("-" * 40)
    planet.discard("Neptune")
    print(f"new set of planets : {planet}")
    print(f"The number of planets in the solar system is {len(planet)}")
    print("-" * 40)
    planet.clear()
    print(f"new set of planets : {planet}")
    print(f"The number of planets in the solar system is {len(planet)}")
    print("-" * 40)


def num_sets():
    """
    Perform various set operations on two sets a and b.

    This function creates two sets, a and b, and demonstrates several set operations:
    - Union
    - Intersection
    - Difference
    - Symmetric Difference
    """
    a = {1, 2, 3, 4, 5}  # Define set a
    b = {3, 4, 5, 6, 7}  # Define set b
    print(f"a : {a}")  # Print set a
    print(f"b : {b}")  # Print set b
    print(f"a.union(b) : {a.union(b)}")  # Union of a and b
    print(f"a.intersection(b) : {a.intersection(b)}")  # Intersection of a and b
    print(f"a.difference(b) : {a.difference(b)}")  # Difference of a and b
    print(f"a.symmetric_difference(b) : {a.symmetric_difference(b)}")  # Symmetric difference of a and b


def fibonacci():
    """
    Generate the Fibonacci sequence up to a given number of terms.
    
    Asks the user for a number, then generates the Fibonacci sequence up to
    that number of terms. The sequence is printed out.
    """
    n = int(input("Enter a number: "))
    if n == 1:
        return [1]
    if n == 2:
        return [1,1]
    # Initialize the first two terms of the sequence
    fibs = [1,1]
    # Generate the rest of the terms
    for i in range(2, n):
        # The next term is the sum of the previous two terms
        fibs.append(fibs[i-1] + fibs[i-2])
    # Print the sequence
    print(fibs)


def palindrome():
    """
    Check if a given word is a palindrome.

    Prompts the user to enter a word and checks if the word is the same
    forwards and backwards. Prints the result.
    """
    s = input("Enter a word: ")  # Get user input
    # Check if the word is the same forwards and backwards
    if s == s[::-1]:
        print(f"{s} is a palindrome")
    else:
        print(f"{s} is not a palindrome")
        

def statistics():
    """
    Calculate the statistics of a given list of numbers.

    Accepts a list of numbers as command line arguments, and prints
    out the total, average, max, and min of the numbers.
    """
    marks = [int(x) for x in sys.argv[1:]]  # Convert the command line arguments to a list of integers
    print(marks)  # Print the list of numbers
    print(f"total marks is {sum(marks)}")  # Print the total of the numbers
    print(f"average marks is {sum(marks)/len(marks)}")  # Print the average of the numbers
    print(f"max marks is {max(marks)}")  # Print the max of the numbers
    print(f"min marks is {min(marks)}")  # Print the min of the numbers


def factorial():
    """Calculate the factorial of a given number."""
    number = int(input("Enter a number: "))
    result = 1
    for i in range(1, number + 1):
        result *= i
    print(f"The factorial of {number} is {result}")


def bubble_sort():
    list_1 = [int(x) for x in input("Enter a list of numbers: ").split()]
    for i in range(len(list_1)):
        for j in range(0, len(list_1) - i - 1):
            if list_1[j] > list_1[j + 1]:
                list_1[j], list_1[j + 1] = list_1[j + 1], list_1[j]
    print(list_1)






if __name__ == main():
    main()
