import random

# Loops run a section of code over and over until a condition is met

# while loops
i = 1
while i <= 5:
    print(i)
    i += 1


ingredients = []

while True:
    ingredient = input("Sandwich ingredient: ")
    if not ingredient:
        break
    else:
        ingredients.append(ingredient)

print(ingredients)


# the continue statement stops the current loop, but continues with others

j = 0
while j <= 5:
    j += 1
    if j == 3:
        continue

    print(j)

# the else statement is just like if statements but will run when false
k = 0
while k < 3:
    print(k)
    k += 1
else:
    print("Loop is now false")


# for loops
# iterate over each item in a collection

todo_list = ["wash car", "do laundry", "cut the grass"]

for item in todo_list:
    print(item)

for item in "test":
    print(item)

point_in_space = (1.5, 3.9, 6.6)

for coordinate in point_in_space:
    print(coordinate)

# range function
for x in range(5):
    print(x)

# calculate times table for 1-10
for y in range(1, 10):
    for z in range(1, 10):
        print(y * z)

# guessing game
# imported random class at the top

secret_number = random.randint(1, 100)

guess = int(input("Guess a number between 1-100: "))

while guess != secret_number:
    if guess < secret_number:
        print("Sorry, number is too lows.")
    else:
        print("Sorry, number is too high")

    guess = int(input("Guess a number between 1-100: "))

print("Good guess!")


# Rock paper scissors
# imported random class at the top

def choice_to_text(c):
    if c == 1:
        return "Rock"
    elif c == 2:
        return "Paper"
    else:
        return "Scissors"


while True:
    print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n")

    choice = int(input("Enter your choice: "))
    choice_text = (choice_to_text(choice))

    computer_choice = random.randint(1,3)
    computer_choice_text = (choice_to_text(computer_choice))

    print(choice_text, "Vs", computer_choice_text)

    if choice == computer_choice:
        print("Draw!")
    else:
        # User picks paper beats rocks
        if choice == 2 and computer_choice == 1:
            print("User Wins!")
        # User picks scissors beats paper
        elif choice == 3 and computer_choice == 2:
            print("User Wins!")
        # User picks rocks beats scissors
        elif choice == 1 and computer_choice == 3:
            print("User Wins!")
        else:
            print("Computer wins!")

    quit_game = input("Do you wish to continue y/n: ")
    if quit_game.lower() == "n":
        break
