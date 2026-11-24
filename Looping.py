""" x =   0
while x < 5:
    print("Not there yet, x=" + str(x))
    x = x + 1
print("x=" + str(x)) """

""" def attempts(n):
    x = 1
    while x <= n:
        print("Attempt " + str(x))
        x += 1
    print("Done")

attempts(5) """

""" username = get_username()
while not valid_username(username):
    print("Invalid username")
    username = get_username()
#This code will give an error because get_username is not defined """


"""my_variable = 5 
while my_variable < 10:
    print("Hello")
    my_variable += 1
#This code will give a NameError
#Variable is not defined  """

""" x = 1
sum = 0
while x < 10:
    sum = sum + x
    x = x + 1

product = 1
while x < 10:
    product = product * x
    x = x + 1

print(sum, product)
#Ouput 45 1 """

""" while x % 2 == 0:
    x = x / 2
#No output """

""" if x != 0:
    while x % 2 == 0:
        x = x / 2
#No output """


""" while x != 0 and x % 2 == 0:
    x = x / 2
#No output """


""" while True:
    do_something_cool()
    if user_requested_to_stop():
        break
#This code will give an error because do_something_cool is not defined """


# For Loops
""" for x in range(5):
    print(x) """

""" friends = ['Taylor', 'Alex', 'Pat', 'Eli']
for friend in friends:
    print("Hi " + friend) """

""" values = [ 23, 52, 59, 37, 48 ]
sum = 0
length = 0
for value in values:
    sum += value
    length += 1

print("Total sum: " + str(sum) + " - Average: " + str(sum/length)) """

# while loops are used when the number of iterations is not known but breaks out when a condition is met,
# for loops are used when the number of iterations is known.

""" product = 1
for n in range(1,10):
  product = product * n

print(product) """


""" def to_celsius(x):
  return (x-32)*5/9

for x in range(0,101,10):
  print(x, to_celsius(x)) """

# Range function can take 1, 2 or 3 arguments. 
# If it takes 1 argument, it will generate numbers from 0 to that number. 
# If it takes 2 arguments, it will generate numbers from the first argument to the second argument. 
# If it takes 3 arguments, it will generate numbers from the first argument to the second argument with a step size of the third argument.

# Nested for loops 
""" for left in range(7):
  for right in range(left, 7):
    print("[" + str(left) + "|" + str(right) + "]", end=" ")
  print() """

# Looping over a string 
""" greeting = 'Hello'
index = 0
while index < len(greeting):
    print(greeting[index:index+1])
    index += 1 """

""" numbers = [1, 2, 3, 4, 5]
squared_numbers = [x ** 2 for x in numbers]
print(squared_numbers) """


#Slice and join Strings
# Slice
""" string1 = "Greetings, Earthlings"
print(string1[0])   # Prints “G”
print(string1[4:8]) # Prints “ting”
print(string1[11:]) # Prints “Earthlings”
print(string1[:5])  # Prints “Greet” """


""" # Prints “Getns atlns”
print(string1[0::2])

# Prints “sgnilhtraE ,sgniteerG”
print(string1[::-1]) """

#join using + and the join method
""" greetings = ["Hello", "world"]
print(" ".join(greetings))  # Prints "Hello world"

# You can also concatenate a combination of strings and variables like in the following example.
name = "Alice"
print("Hello, " + name + "!")  # Prints "Hello, Alice!" """

""" def format_phone(phonenum):
    area_code = "(" + phonenum[:3] + ")"
    exchange = phonenum[3:6]
    line = phonenum[-4:]
    return area_code + " " + exchange + "-" + line

format_phone('2025551212') """


# Common errors in for loops 
""" def greet_friends(friends):
    for friend in friends:
        print("Hi " + friend)

greet_friends(['Taylor', 'Luisa', 'Jamaal', 'Eli']) """
