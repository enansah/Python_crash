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

product = 1
for n in range(1,10):
  product = product * n

print(product)


""" def to_celsius(x):
  return (x-32)*5/9

for x in range(0,101,10):
  print(x, to_celsius(x)) """


