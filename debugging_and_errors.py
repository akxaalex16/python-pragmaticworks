# calculate times table for 1-10
for x in range(1,10):
    for y in range(1, 10):
        print(x * y)

# if you click in the gutter, you get a red dot, the breakpoint
# breakpoint is a place in code that we have noted, that when the application is running,
#     under debug mode, we want the application to stop for us.
#     we can see the variables and what the state of things are, and to see if everything is running as intended.

# 1 - make a breakpoint
# 2 - click the bug at the top to start the debugging process
# 3 - in this case you will see x:1 and y:1, it is telling us the state of the variables
#     tells us the current x and current y
# 4 - click the step over button, which is going to make it skip over the breakpoint for this one iteration
# 5 - now the console will show 1 as the result, and go to the next iteration
# 6 - now it shows the new state of the variable, x:1 and y:2

# try catch of exceptions
# errors can be caught and handled

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("ERROR: Cannot divide by zero.")

#this will go into the exception block of code and not break and stop the whole app
divide(10, 0)

# built-in exceptions
# https://www.w3schools.com/python/python_ref_exceptions.asp

