# Star Print using for Loop
def main():
    num = int(input("Enter number: "))
    print_square(num)
def print_square(size):
    
    for i in range(size):
        for j in range(size):
            print("*", end=" ")
        
        print()

main()