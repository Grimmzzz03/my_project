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
    print(f"\nperson_{num}")
    person = {}
    person['first_name'] = input("Enter the First name: ").title()
    person['last_name'] = input("Enter the last name: ").title()
    person['age'] = int(input("Enter the age: "))
    person['city'] = input("Enter the city name: ").title()
    person_num.append(person)

print(f"\nThe list of person: ")
print(person_num)


for person in person_num:
    print(f"\nPerson{person_num.index(person) + 1}: ")
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

"""
# while loop with break condition
while active= 'true':
    city = input("Enter the name of your city: ")
    if city == 'quit':
        break
        
    else:
        print(f"I would love to go to {city.title()}")
"""

"""
# while loop with countinue condition
current_no= 0 
while current_no < 10:
    current_no += 1
    if current_no % 2 == 0:
        print(f"{current_no} is an even number")
        continue
    print(current_no)
"""
    
"""    
while True:
    pizza_toppings = input("Enter the toppings for pizza: ")
    if pizza_toppings == 'quit':
        break
        
    else:
        print(f"I would add {pizza_toppings} topping to your pizza")
"""

"""
while True:
    age = (input("Enter your age: "))
    if age == 'quit':
        break
    age = int(age)
    if age < 3:
        print("  You get in free!")
    elif age <= 12:
        print("  Your ticket is $10.")
    else:
        print("  Your ticket is $15.")
"""
"""
# while loop with lists and dictionaries
unconfirmed_users = ['admin', 'user1', 'user2', 'user3']  
confirmed_users = [] 

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    
    print(f"Verified user: {current_user.title()}")
    confirmed_users.append(current_user)
    
print("The following users are confirmed")
for confirmed in confirmed_users:
    print(confirmed.title())
"""

"""
# while loop with dictionary keys
responses = {}

polling_active = True

while polling_active:
    name = input("Enter your name: ").title()
    response = input("Which mountain would you like to climb someday: ").title()
    
    responses[name] = response
    
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False
        
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")
"""

"""
# restuarant order of responses
orders = ['burger', 'fries', 'salad', 'chips']

finished_orders = []

while orders:
    current_order = orders.pop()
    print(f"Your order is {current_order}")
    finished_orders.append(current_order)
    
print("The following orders have been completed")
for order in finished_orders:
    print(order)
"""    

"""
orders = ['burger', 'fries', 'salad', 'chips','burger', 'chowmein', 'pasta', 'burger']

print(orders)

while 'burger' in orders:
    orders.remove('burger')
    
print(orders)
"""

"""
# user and theirs dream destination
respones = {}

polling_active = True

while polling_active:
    name = input("Enter your name: ").title()
    travel = input("Enter your dream destination: ").title()
    
    respones[name] = travel
    
    repeat = input("Would you like to let another person respond? (yes/ no) ")
    if repeat == 'no':
        polling_active = False
        
print("\n--- Poll Results ---")
for name, travel in respones.items():
    print(f"{name} would like to go {travel}.")
"""

"""
# functions
def display_message():
    print("I am learning about functions")
    
display_message()

def favourite_book(title):
    print(f"My favourite book is {title}")
    
favourite_book('Alice in Wonderland')
"""

"""
def make_shirt(message, size):
    
    print(f"The size of the shirt is {size} and message is {message}")
    
make_shirt('large t-shirt', 'large')
make_shirt('medium t-shirt', 'medium')
make_shirt('small t-shirt', 'small')
"""
"""
def describe_city(city, country):
    print(f"{city.title()} is in {country.title()}")
    
describe_city('chennai', 'india')
describe_city('new delhi', 'india')
describe_city('london', 'uk')
describe_city('reykjavik', 'iceland')
"""

"""
def build_person(first_name, last_name, age=None):
    #Return a dictionary of information about a person.
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', 27)
print(musician)
"""

"""
# return a value
def get_formatted_name(first_name, last_name, middle_name=None):
    if middle_name:
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name} {last_name}"
    return full_name.title()

while True:
    print("\nPlease tell me your name: ")
    print("(enter 'q' at any time to quit)")
    f_name = input("First name: ")
    if f_name == 'q':
        break
    l_name = input("Last name: ")
    if l_name == 'q':
        break
    m_name  = input("Middle name: ")
    if m_name == 'q':
        break
    
    formatted_name = get_formatted_name(f_name, l_name, m_name)
    print(f"\nHello, {formatted_name}")
"""

"""
# function with default parameter
def city_country(city, country):
    return f"{city.title()}, {country.title()}"

while True:
    print("\nPlease tell me your city and country: ")
    print("(enter 'q' at any time to quit)")
    city = input("City: ")
    if city == 'q':
        break
    country = input("Country: ")
    if country == 'q':
        break
    formatted_name = city_country(city, country)
    print(f"\n{formatted_name}")
"""

"""
# function with list_of_dictionary
def list_cities(city, country, attraction=' '):
    list_city = {'city': city, 'country': country}
    if attraction:
        list_city['attraction'] = attraction
    return list_city

while True:
    print("\nPlease tell me your city and country: ")
    print("(enter 'q' at any time to quit)")
    city = input("city: ")
    if city == 'q':
        break
    country = input("Country: ")
    if country == 'q':
        break
    attraction = input("attraction: ")
    if attraction == 'q':
        break
    formatted_cities = list_cities(city, country, attraction)
    print(f"\n{formatted_cities}")
"""

"""
unprinted_design = ['pentagonal','octagonal','hexagonal']
completed_design = []

print(f"Current Designs")
while unprinted_design:
    current_design = unprinted_design.pop()
    print(current_design)
    completed_design.append(current_design)

print(f"\ncompleted designs")
for design in completed_design:
    print(design)
"""

"""
def print_design(unprinted_design, completed_design):
    while unprinted_design:
        current_design = unprinted_design.pop()
        print(f"current design: {current_design}")
        completed_design.append(current_design)

def show_completed_design(completed_design):
    print(f"\nCompleted Designs:")
    for design in completed_design:
        print(design)

unprinted_design = ['pentagonal','hexagonal','heptagonal','octagonal','nonagon','decagon']
completed_design = []

print_design(unprinted_design,completed_design)
show_completed_design(completed_design)
"""

"""
def send_message(messages):
    for copy_message in messages:
        print(f"{copy_message}")
    print("Done")

messages = ["hello there", "how are u?", ":)"]
send_message(messages[:])
print(f"original list: {messages}")
"""

"""
def pizza(size,*toppings):
    print(f"\nMaking a {size} pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

pizza(12,'pepperoni')
pizza(16,'mushrooms', 'green peppers', 'extra cheese')
"""

"""
# **kwargs
def build_profile(first, last, **user_info):
    profile = {'first_name': first, 'last_name': last}
    for key, value in user_info.items():
        profile[key] = value
    return profile

user_profile = build_profile('rishav', 'dhiman', location='dharamshala', field='Computer Science and Engg', age=21)
print(user_profile)
"""

"""
# *args
def sandwich(*toppings):
    print(f"\nMaking a sandwich with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

sandwich('pepperoni')
sandwich('mushrooms', 'green peppers', 'extra cheese')
sandwich('ham', 'cheese', 'lettuce')
"""

"""
# make car with **kwargs 
def make_car(manufacturer, model, **car_info):
    car = {'manufacturer': manufacturer, 'model': model}
    for key, value in car_info.items():
        car[key] = value
    return car

car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)
"""

"""
# make cupcake with *args
def make_cupcakes(size,price, *toppings):
    print(f"\nMaking {size} & {price} cupcake with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")

make_cupcakes('small', '5$','chocolate', 'cocoa powder', 'sprinkles')
make_cupcakes('large', '10$','chocolate', 'cocoa powder', 'sprinkles', 'caramel sauce')
make_cupcakes('large', '15$','chocolate', 'cocoa powder', 'sprinkles', 'caramel sauce', 'cocoa powder')
make_cupcakes('large', '20$','chocolate', 'cocoa powder', 'sprinkles', 'caramel sauce', 'cocoa powder', 'sprinkles')
make_cupcakes('large', '25$','chocolate', 'cocoa powder', 'sprinkles', 'caramel sauce', 'cocoa powder', 'sprinkles', 'caramel sauce')
make_cupcakes('large', '30$','chocolate', 'cocoa powder', 'sprinkles', 'caramel sauce', 'cocoa powder', 'sprinkles', 'caramel sauce', 'eggs')
"""
"""
# importing function
def pizza(size,*toppings):
    print(f"\nMaking a {size} pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")
"""

"""
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        print(f"{self.name} rolled over!")

my_dog = Dog('willie', 6)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()
my_dog.roll_over()

your_dog = Dog('lucy', 3)
print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()
your_dog.roll_over()
"""

"""
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type


    def describe_restaurant(self):
        print(f"\n{self.restaurant_name} is a {self.cuisine_type} restaurant.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open.")


restaurant = Restaurant('the mean queen', 'pizza')
restaurant.describe_restaurant()
restaurant.open_restaurant()

restaurant_2 = Restaurant('mcdonalds', 'fast food')
restaurant_2.describe_restaurant()
restaurant_2.open_restaurant()

restaurant_3 = Restaurant('dominos', 'pizza')
restaurant_3.describe_restaurant()
restaurant_3.open_restaurant()
"""

"""
class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        print(f"\n{self.first_name} {self.last_name} is {self.age} years old.")

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}!")

user = User('rishav', 'dhiman', 21)
user.describe_user()
user.greet_user()
"""

"""
class Car:

    def __init__(self,make,model,year,mileage):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage

    def get_descriptive_name(self):
        long_name = f"{self.make} {self.model} {self.year}"
        return long_name.title

    def read_odometer(self):
        print(f"This car has meter readings of {self.mileage} kms on it")

car_make = str(input("Enter the manufacturer: "))
car_model = str(input("Enter the Model no: "))
car_year = int(input("Enter the manufactured year: "))
car_mileage = int(input("Enter the odometer reading: "))
my_car = Car(car_make,car_model,car_year,car_mileage)
my_car.get_descriptive_name()
my_car.read_odometer()
"""

"""
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.make} {self.model} {self.year}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has meter readings of {self.odometer_reading} kms on it")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("you can't roll back")

    def increment_odometer(self,miles):
        self.odometer_reading += miles

car_name = str(input("Enter the brand of your car: "))
car_model = str(input("Enter the model of your car: "))
car_year = int(input("Enter the year of your car: "))

my_car = Car(car_name, car_model, car_year)
print(my_car.get_descriptive_name())

my_car.update_odometer(999)
my_car.read_odometer()

my_car.increment_odometer(100)
my_car.read_odometer()
"""

"""
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"\n{self.restaurant_name} is a {self.cuisine_type} restaurant.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open.")

    def set_number_served(self, number):
        self.number_served = number
        print(f"Total number of customers served is {self.number_served}")

    def increment_number_served(self, number):
        self.number_served += number
        print(f"Total number of customers served is {self.number_served}")

restaurant = Restaurant('the mean queen', 'pizza')
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.set_number_served(20)
restaurant.increment_number_served(10)
"""

"""
class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0

    def describe_user(self):
        print(f"\n{self.first_name} {self.last_name} is {self.age} years old.")

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}!")

    def increment_login_attempts(self):
        self.login_attempts += 1
        print(f"Total number of login attempts is {self.login_attempts}")

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f"Total number of login attempts is {self.login_attempts}")

user = User('rishav', 'dhiman', 31)
user.describe_user()
user.greet_user()
user.increment_login_attempts()
user.increment_login_attempts()
user.reset_login_attempts()
"""

"""
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.make} {self.model} {self.year}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has meter readings of {self.odometer_reading} kms on it")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("you can't roll back")

    def increment_odometer(self,miles):
        self.odometer_reading += miles

class Electric_Car(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery_size = 40

    def describe_battery(self):
        print(f"The Battery Size of the car is {self.battery_size} Kwh capacity.")

    def fill_gas_tank(self):
        print("Electric cars don't have gas tanks\n")

my_tesla = Electric_Car('Tesla','Model S',2022)
print(my_tesla.get_descriptive_name())
my_tesla.update_odometer(1000)
my_tesla.read_odometer()
my_tesla.increment_odometer(100)
my_tesla.read_odometer()
my_tesla.battery_size = 75
my_tesla.describe_battery()
my_tesla.fill_gas_tank()
my_nexon = Electric_Car('TATA','NEXON-EV',2024)
print(my_nexon.get_descriptive_name())
my_nexon.update_odometer(500)
my_nexon.read_odometer()
my_nexon.increment_odometer(100)
my_nexon.read_odometer()
my_nexon.describe_battery()
my_nexon.fill_gas_tank()
"""

"""
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.make} {self.model} {self.year}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has meter readings of {self.odometer_reading} kms on it")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("you can't roll back")

    def increment_odometer(self,miles):
        self.odometer_reading += miles

class Battery:
    def __init__(self,battery_size=85):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"The Battery Size of the car is {self.battery_size} Kwh capacity.")

    def fill_gas_tank(self):
        print("Electric cars don't have gas tanks")

    def get_range(self):
        if self.battery_size == 60:
            distance = 140
        elif self.battery_size == 85:
            distance = 225
        message = f"This car can go approximately {distance} miles on a full charge\n"
        print(message)

class Electric_Car(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery = Battery()


my_tesla = Electric_Car('Tesla','Model S',2022)
print(my_tesla.get_descriptive_name())
my_tesla.update_odometer(1000)
my_tesla.read_odometer()
my_tesla.increment_odometer(100)
my_tesla.read_odometer()
my_tesla.battery.describe_battery()
my_tesla.battery.fill_gas_tank()
my_tesla.battery.get_range()
"""

"""
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"The restaurant name is {self.restaurant_name}")
        print(f"The cuisine type is {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open")

    def set_number_served(self, number):
        self.number_served = number
        print(f"Total number of customers served is {self.number_served}")

    def increment_number_served(self, number):
        self.number_served += number
        print(f"Total number of customers served is {self.number_served}")

class IceCreamStand(Restaurant):
    def __init__(self,restaurant_name,cuisine_type):
        super().__init__(restaurant_name,cuisine_type)
        self.flavors = ['vanilla','chocolate','strawberry','coffee']

    def show_flavors(self):
        for flavor in self.flavors:
            print(f"\t{flavor}")

restaurant = Restaurant('the mean queen', 'pizza')
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.set_number_served(20)
restaurant.increment_number_served(10)

ice_cream_stand = IceCreamStand('the mean queen','ice cream')
ice_cream_stand.describe_restaurant()
ice_cream_stand.show_flavors()
"""

"""
class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.login_attempts = 0


    def describe_user(self):
        print(f"\n{self.first_name} {self.last_name} is {self.age} years old.")

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}!")

    def increment_login_attempts(self):
        self.login_attempts += 1
        print(f"Total number of login attempts is {self.login_attempts}")

    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f"Total number of login attempts is {self.login_attempts}")

class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges

    def show_privileges(self):
        print("The Admin has the following privileges:")
        for privilege in self.privileges:
            print(f"\t{privilege}")

class Admin(User):
    def __init__(self, first_name, last_name, age):
        super().__init__(first_name, last_name, age)
        self.privileges = Privileges(['can add post', 'can delete post', 'can ban user'])

user = User('rishav', 'dhiman', 32)
user.describe_user()
user.greet_user()
user.increment_login_attempts()
user.increment_login_attempts()
user.reset_login_attempts()
user = Admin('rishav', 'dhiman', 31)
user.describe_user()
user.greet_user()
user.privileges.show_privileges()

admin = Admin('rishav', 'dhiman', 31)
admin.describe_user()
admin.greet_user()
admin.increment_login_attempts()
admin.increment_login_attempts()
admin.reset_login_attempts()
admin.privileges.show_privileges()
"""

"""
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.make} {self.model} {self.year}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has meter readings of {self.odometer_reading} kms on it")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("you can't roll back")

    def increment_odometer(self,miles):
        self.odometer_reading += miles

class Battery:
    def __init__(self, battery_size=65):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def update_battery(self):
        if self.battery_size == 65:
            self.battery_size = 85
        else:
            self.battery_size = 65
    def get_range(self):
        if self.battery_size == 65:
            distance = 260
        elif self.battery_size == 85:
            distance = 315
        print(f"This car can go about {distance} Kms on a full charge.")

    def fill_gas_tank(self):
        print("This car doesn't need a gas tank!")

class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()

my_tesla = ElectricCar('tesla', 'model s', 2019)
my_tesla.battery.get_range()
my_tesla.battery.update_battery()
my_tesla.battery.get_range()
my_tesla.battery.describe_battery()
my_tesla.battery.update_battery()
my_tesla.battery.get_range()
my_tesla.battery.describe_battery()
my_tesla.battery.fill_gas_tank()
"""

"""
people = {
    'first_name': 'rishav',
    'last_name': 'dhiman',
    'age': 32,
    'city': 'dharamshala'}

for key, value in people.items():
    print(f"{key}: {value}")
"""

