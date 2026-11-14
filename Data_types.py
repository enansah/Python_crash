# print(7+8)
# print("hello "+ "world")

# print(7+"8")
#this will throw an error

# print(type("a"))
# print(type(2))
# print(type(2.5))


# print(7+8.5)
# print("a"+"b"+"c")
# print("This " + "is " + "pretty " + "neat!")


""" base = 6
height = 3
area = (base*height)/2
print("The area of the triangle is: " + str(area))  """

""" # The following lines assign the variable to the left of the = 
# assignment operator with the values and arithmetic expressions 
# on the right side of the = assignment operator.
hotel_room = 100
tax = hotel_room * 0.08
total = hotel_room + tax
room_guests = 4
share_per_person = total/room_guests


# This line outputs the result of the final calculation stored
# in the variable "share_per_person"
print("Each person needs to pay: " + str(share_per_person)) # change a data type """

""" # The following 5 lines assign strings to a list of variables.
salutation = "Dr."
first_name = "Prisha"
middle_name = "Jai"
last_name = "Agarwal"
suffix = "Ph.D."
 
print(salutation + " " + first_name + " " + middle_name + " " + last_name + ", " + suffix) 
# The comma as a string ", " adds the conventional use of a comma plus a 
# space to separate the last name from the suffix.
 
# Alternatively, you could use commas in place of the + connector:
print(salutation, first_name, middle_name, last_name,",", suffix)
# However, you will find that this produces a space before a comma within a string. """

""" # The following code causes a type error between a string 
# and an integer:

print("5 * 3 = " + (5*3)) 


# Resolution: 
# print("5 * 3 = " + str(5*3))
#
# To avoid a type error between the string and the integer within the
# print() function, you can make an explicit data type conversion by
# using the str() function to convert the integer to a string.   """


""" numerator = 7
denominator = 0   # Possible resolution: Change the denominator value 
result = numerator / denominator
print(result)


# One possible assumption for a number divided by zero error might
# include the issue of a null value as a denominator (could happen when
# using a loop to iterate over values in a database). In such cases, the
# desired outcome may be to leave the numerator value intact. The
# numerator value can be preserved by reassigning the denominator with 
# the integer value of 1. The result would then equal the numerator. """


""" def greeting(name):
    print("Welcome, " + name)
    
greeting("Kay")
greeting("Cameron") """


""" def greeting(name, department):
    print("Welcome, " + name)
    print("You are part of " + department)
    
greeting("Blake", "Software engineering")
greeting("Ellis", "Software engineering") """


""" def area_triangle(base, height):
    return base*height/2
area_a = area_triangle(5,4)
area_b = area_triangle(7,3)
sum = area_a + area_b
print("The sum of both areas is: " + str(sum)) """

""" def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds
 
hours, minutes, seconds = convert_seconds(5000)
print(hours, minutes, seconds) """


""" def greeting(name):
    print("Welcome, " + name)
result = greeting("Christine")
print(result) """

""" name = "Kay"
number = len(name) * 9

print("Hello " + name + ". Your lucky number is " + str(number))

name = "Cameron"
number = len(name) * 9

print("Hello " + name + ". Your lucky number is " + str(number)) """


""" def lucky_number(name):
    number = len(name) * 9
    print("Hello " + name + ". Your lucky number is " + str(number))

lucky_number("Kay")
lucky_number("Cameron") """


""" def calculate(d):
    q = 3.14
    z = q * (d ** 2)
    print(z)

calculate(5)
#Output is 78.5 """

""" def circle_area(radius):
    pi = 3.14
    area = pi * (radius ** 2)
    print(area)

circle_area(5)
#Output is 78.5 """

""" name = "Kay"
number = len(name) * 9

print("Hello " + name + ". Your lucky number is " + str(number))

name = "Cameron"
number = len(name) * 9

print("Hello " + name + ". Your lucky number is " + str(number)) """


""" def lucky_number(name):
    number = len(name) * 9
    print("Hello " + name + ". Your lucky number is " + str(number))

lucky_number("Kay")
lucky_number("Cameron") """


""" def calculate(d):
    q = 3.14
    z = q * (d ** 2)
    print(z)

calculate(5)
#Output is 78.5 """

""" def circle_area(radius):
    pi = 3.14
    area = pi * (radius ** 2)
    print(area)

circle_area(5)
#Output is 78.5 """


