def main():
    student = get_student()
    print (f"{student['name']} is from House: {student['house']}")
    
def get_student():
    name= input("student name: ")
    house= input("house name: ")
    return {"name": name, "house": house}

if __name__ == "__main__":
    main()
