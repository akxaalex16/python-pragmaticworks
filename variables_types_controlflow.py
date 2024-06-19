import math

# python has 3 basic types:
# strings of text
# numbers
# booleans: True or False

first_name = "Akxa"
last_name = "Alex"
print("Hello " + first_name + " " + last_name)

# formatted strings
print(f'My name is {first_name} {last_name}')

# methods
print(first_name.upper())
print(first_name.lower())
print(len(first_name))
print(last_name.replace("Al", "Fl"))
print(first_name.islower())
print(first_name.upper().isupper())
print(first_name[2])

# you can change the value of the variable
print("What is your fav color? ")
color = input()
print(color + " is an excellent choice!")
color = "purple"
print(color + " is also my fav color!")

current_age_string = "29"
current_age_number = 29
is_young = True

# \n for next line
print("hello\nworld")

# int value can be pos or neg; without decimal point
x = 2

# you can add underscores between numbers to make it easier to read, python ignores the _ between numbers
gdp = 23_315_000_000

a, b, c = 16, 3, 9

# floating point number, a decimal number
y = 2.0
z = 3.6

# operations: addition, subtraction, multiplication, division, etc.
# follows order of operations: PEMDAS
print(y + z)
print(x / y + z)
print(x / (y + z))

name = "Beans"
print(str(x) + " " + name)
num = "50"
print(y + int(num))
d = -2
print(abs(d))
print(max(x, z))

print(math.sqrt(3))

# control flow
is_morning = True
is_hungry = True

if is_hungry:
    if is_morning:
        print("Eat breakfast")

    print("Eating")

morning = True
hungry = False

if hungry:
    print("Eating")
elif morning:
    print("Go for a run")
else:
    print("Go to sleep instead")


has_diploma = True
is_experienced = True

# True and True = True
# True and False = False
# True or False = True
# True or True = True
# False or False = False
# True and (not False) = True
if has_diploma and is_experienced:
    print("Hire them on the spot")
elif has_diploma and not is_experienced:
    print('Hire an intern')
elif has_diploma or is_experienced:
    print("Bring in for an interview")
else:
    print("Politely decline")


location = "Home"

if location == "Home":
    print("Welcome home!")


e = 16
f = 3

if e < f:
    print("E is less than F")
else:
    print("F is than or equal to E")

g = 16
h = 16

if a <= b:
    print("g is than or equal to h")
else:
    print("h is less than g")

i = 2
j = 5
k = 4

if i < j and i < k:
    print('i is less than j and k')

# can write the code all in one line
# ternary operator
l = 3
m = 16
print("l is bigger") if l > m else print("m is bigger")
