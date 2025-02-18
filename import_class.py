"""
#from practice_code import Restaurant
#from practice_code import IceCreamStand
#from practice_code import Restaurant, IceCreamStand
#import practice_code

#restaurant = practice_code.Restaurant('the mean queen', 'pizza')
restaurant = Restaurant('the mean queen', 'pizza')
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.set_number_served(20)
restaurant.increment_number_served(10)
print("\n")
#ice_cream_stand = practice_code.IceCreamStand('the mean queen','ice cream')
ice_cream_stand = IceCreamStand('the mean queen','ice cream')
ice_cream_stand.describe_restaurant()
ice_cream_stand.show_flavors()
"""
"""
from practice_code import User, Admin

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
