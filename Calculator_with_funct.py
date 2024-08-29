# Calculator with Function and return value
def main():
    x = int(input("Enter the Value of X: "))
    y = int(input("Enter the Value of Y: "))
    z = int(input("Enter the Value of Z: "))

    def sqrt(x):
        return x**2
    
    def cub(y):
        return pow(y, 3)
    
    def add(x, y, z):
        return x + y + z
    
    def sub(x, y, z):
        return x - y - z
    
    def mul(x, y, z):
        return x * y * z
    
    def div(x, y, z):
        return x / y / z
    
    
    print("Square is:", sqrt(x))
    print("Cube is:", cub(y))
    print("Addition is:", add(x, y, z))
    print("Subtraction is:", sub(x, y, z))
    print("Multiplication is:", mul(x, y, z))
    print("Division is:", div(x, y, z))
    
main()