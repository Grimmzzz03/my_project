# function with loop
def main():
    number = get_number()
    star(number)

def get_number():
    while True:
        num = int(input("Number: "))
        if num > 0:
            break
    return num
    
      
def star(n):
        for _ in range(n):
         print("*")

main()