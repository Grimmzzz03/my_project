#check even odd using functions
def main():
    num=int(input("enter a number: "))
    if is_even(num):
        print(f"{num} is even")
    else:
        print(f"{num} is odd")
        
def is_even(num):
    return num%2==0
    
main()    
    
       
        