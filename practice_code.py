"""
# list

guest_list = ['harry', 'tom', 'chris']
list1 = 'tom'
guest_list.remove(list1)
guest_list.append('christina')
guest_list.insert(0,'rishav')
guest_list.insert(2,'parul')
guest_list.append('peter')
guest_list.sort(reverse=True)
print(guest_list)
num = len(guest_list)
print(f"no of guests in the Party: {num}")
for list in guest_list:
    print(f"{list.title()}, you are invited in the party")
    print(f"{list1.title()} can't make to the party because he is ill")
"""
"""
n = int(input("Enter the value of N: "))
for num in range(1,n+1):
    print(f"{num**2} is Squared of {num}")
    print(f"{num**3} is Cubed of {num}")
    print(f"{num**4} is Quarted of {num}")
    
"""
"""
n = int(input("Enter the value of your choice: "))
digits = [num for num in range(0,n+1)]
print(sum(digits))
""" 
"""
n = int(input("Enter the value of your choice: "))
digits = [num for num in range(0,n+1,3)]
print(digits)
"""
"""
list_car = ['kia', 'maruti', 'tata', 'hyundai', 'mahindra', 'mg','byd']
for list in list_car[-3:]:
    print(list.title())

"""
"""
cars = ['kia', 'maruti', 'mahindra', 'tata', 'bmw', 'audi', 'mercedes']
for car in cars:
    if car == 'kia':
        print(f"{car.title()} is a good car")
    else:
        print(f"{car.title()} is not a good car")
         
"""
"""
i = int(input("enter the value of i:" ))
nums = []
for num in range(1,i):
    nums.append(num)
    sums = sum(nums)

print(sums)
"""
"""
alien_color = input("Enter the Color of alien: ")

if alien_color == 'green':
    print("you have earned 5 points")
elif alien_color == 'red':
    print("you have earned 10 points")
elif alien_color == 'blue':
    print("you have earned 15 points")
else:
    print("you have earned 0 points")
"""
"""
age = int(input("Enter the age: "))

if age <= 2:
    print("The person is a baby")
elif age <= 4:
    print("The person is a Toddler")    
elif age <= 13:
    print("The person is a Kid")
elif age <= 20:
    print("The person is a Teenager")
elif age <= 65:
    print("The person is a Adult")
else:
    print("The person is an Elder")
"""
"""
lists = ['admin','joy', 'jordan', 'emily', 'jack', 'bill']

if lists:
    for list in lists:
        if list == 'admin':
            print("Hello admin, would you like to see a status report: ")
        else:
            print(f"Hello {list}, thank you for logging in again: ")   
        
else:
    print("We need to find some users: ")
"""    
"""
current_users = ['bill', 'jill', 'jack', 'rose', 'john']
new_users = ['JOHN', 'jack', 'emily', 'tina', 'dina']

for new_user in new_users:
    if new_user.lower() in current_users:
        print(f"Sorry {new_user}, that name is taken.")
    else:
        print(f"Great, {new_user} is available.")

"""   
"""
n = int(input("Enter the value of: "))      
list = []
names = []
for num in range(1,n):
    list.append(num)
    name = input("Enter the name: ")
    names.append(name)
    

print(f"list of Num: {list}")
print(f"List of Names: {names}")
for num in list:
    n1 = names[num-1]
    if num == 1:
        print(f"{num}st is {n1}")
        
    elif num == 2:
        print(f"{num}nd is {n1}")
    elif num == 3:
        print(f"{num}rd is {n1}")
    else:
        print(f"{num}th {n1}")
"""
"""
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'fast'}
print(alien_0)

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
elif alien_0['speed'] == 'fast':
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New Position: {alien_0['x_position']}")
"""
"""
fav_lang = {
    'rishav' : 'python',
    'anshul' : 'java',
    'parul' : 'c',
    'rahul' : 'c++'  
    }

lang = fav_lang['rishav'].title()
print(f"Favourite lang of Rishav is {lang}")

lang_value = fav_lang.get('points', 'no points value assigned')
print(lang_value)

for name, language in fav_lang.items():
    print(f"{name.title()}, your favourite language is {language.title()}")

for name in fav_lang.keys():
   print(name.title())
   
for language in fav_lang.values():
    print(language.title())

friends = ['rishav', 'anshul']
for name in fav_lang.keys():
    print(f"Hello {name.title()}")
    
    if name in friends:
        print(f"Hi {name.title()}, I see your favourite language is {fav_lang[name].title()}")
    else:
        print(f"Hi {name.title()}, I see your favourite language is {fav_lang[name].title()}")
"""
"""
n = int(input("How many person do you want: "))
person_num = []
for num in range(n):
    print(f"person_{num+13}")
    person = {}
    person['first_name'] = input("Enter the First name: ").title()
    person['last_name'] = input("Enter the last name: ").title()
    person['age'] = int(input("Enter the age: "))
    person['city'] = input("Enter the city name: ").title()
    person_num.append(person)

print(person_num)

for person in person_num:
    for k, v in person.items():
       print(f"{k} is {v}")
"""

"""
list = [3,6,7,8,3,1,10,23,35,3,6,7,8,54,76,102,230,65,46,432,23,12,3,5]
list.sort(reverse=True)
print(f"the largest no in the list is {(list[0])}")
"""
"""
users = {
            'aeinstein' : {
                'first':'albert',
                'last' : 'einstein',
                'location' : 'princetonm',
        },
            'mcurie' : {
                'first' : 'marie',
                'last' : 'curie', 
                'location' : 'paris',        
        }
    }

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
"""
"""
# Rental Car 

rental_car = input("Enter the name of the Rental Car: ")

if rental_car == "subaru":
    print(f"Let me see if i can find you a {rental_car}")
else:
    print(f"Sorry, we don't have {rental_car}")
"""
"""
# dinner party
people = int(input("How many people in the dinner group: "))

if people > 8:
    print(f"Sorry you will have to wait \nWe don't have a seating arrangement for {people} peoples")
else:
    print(f"Welcome to the dinner group \nWe have a seating arrangement for {people} peoples")
    
""" 
"""
# multiple of 10 
num = int(input("Enter the no of your choice: "))

if num % 10 == 0:
    print(f"{num} is a multiple of 10")
else:
    print(f"{num} is not a multiple of 10")
  
"""

