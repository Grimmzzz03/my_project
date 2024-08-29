def main():
    x = get_num()
    print(f"The input number is {x}")

def get_num():
    while True:
        try:
            return int(input("Enter a number: "))
        except ValueError:
            pass #print("Invalid input. Please enter an integer.")

main()