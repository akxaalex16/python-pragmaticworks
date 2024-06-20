# def is used to define a function
def function_name():
    print("My function")


# can be invoked by calling the name with ()
function_name()
# and can be called as many times as we need to reuse it

# parameters are located with in parentheses next to the function name
def greet_user(username):
    print(f"Welcome, {username}")


greet_user("Beans")

# parameters are assigned by the position or order in the parentheses
# can also be assigned by keyword
def greeting(first_name, last_name):
    print(f"Welcome, {first_name} {last_name}")


greeting("Akxa", "Beans")
greeting(first_name="Sean", last_name="Beans")

# parameters can have default values to make them optional
def welcome(first_name, last_name="Beans"):
    print(f"Welcome, {first_name} {last_name}")


welcome("Baby")
welcome("Jovi")

# functions can also return data out to where it was called
def multiply(x, y):
    return x * y


return_value = multiply(3,16)
print(return_value)

# bonus:
# Fibonacci sequence: Sum of the last two numbers
# Index: 0 1 2 3 4 5
# Fib:   0 1 1 2 3 5  ---> so 0+1=1, 1+1=2, 1+2=3, 2+3=5

def fibonacci(index):
    if index == 0 or index == 1:
        return index
    else:
        return fibonacci(index-1) + fibonacci(index-2)


print(fibonacci(10))

