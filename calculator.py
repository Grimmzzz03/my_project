# test calculator
def main():
    x = input("Enter a number: ")
    print("x squared is ", square(x))
    
def square(x):
    return x*x

if __name__ == "__main__":
    main()