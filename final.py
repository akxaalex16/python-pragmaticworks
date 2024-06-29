import tkinter as tk

# create window
window = tk.Tk()
window.title('My First Calculator')
window.geometry("450x550")

# current text in text entry box to capture the data
current_text = tk.StringVar(window)
# adding 0 as the value displayed
current_text.set("0")

class Calculator:
    def __init__(self):
        self.last_number = 0
        self.current_operation = ""
        self.current_number = 0

    def set_operation(self, operation):
        self.current_operation = operation
        self.last_number = self.current_number
        self.current_number = 0

    def clear_all(self, text_box):
        self.last_number = 0
        self.current_operation = ""
        self.current_number = 0
        text_box.set("0")

    def set_number(self, num, text_box):
        new_num = str(self.current_number) + str(num)
        self.current_number = int(new_num)
        text_box.set(self.current_number)

    def calculate(self, text_box):
        match self.current_operation:
            case "+":
                self.last_number = self.last_number + self.current_number
            case "-":
                self.last_number = self.last_number - self.current_number
            case _:
                text_box.set("Error, operation not found")
                return

        text_box.set(self.last_number)


calc = Calculator()


# added heading and text entry box
display_frame = tk.Frame(window)
tk.Label(display_frame, text="Python Calculator", font=("Georgia", 25), anchor=tk.CENTER).pack()
# state is disabled so that users cant put in values, it has to be done programmatically, clicked by the user to do the calculations
# display input
output = tk.Entry(display_frame, justify=tk.RIGHT, width=45, font=16, state="disabled", textvariable=current_text)
output.pack(pady=20)
display_frame.pack()

button_frame = tk.Frame(window)


def create_button(text, command=None):
    return tk.Button(button_frame, text=text, height=4, width=10, font=20, command=command)

# def alert():
#     current_text.set("Hello")

# lambda is a shortcut for adding a function, inline function, anonymous function
# when you pass a function as a variable, then don't add the parentheses
create_button("CE", command=lambda: calc.clear_all(current_text)).grid(row=0, column=2)

create_button(7, command=lambda: calc.set_number(7, current_text)).grid(row=1, column=0)
create_button(8, command=lambda: calc.set_number(8, current_text)).grid(row=1, column=1)
create_button(9, command=lambda: calc.set_number(9, current_text)).grid(row=1, column=2)
# create_button("X").grid(row=1, column=3)

create_button(4, command=lambda: calc.set_number(4, current_text)).grid(row=2, column=0)
create_button(5, command=lambda: calc.set_number(5, current_text)).grid(row=2, column=1)
create_button(6, command=lambda: calc.set_number(6, current_text)).grid(row=2, column=2)
create_button("-", command=lambda: calc.set_operation("-")).grid(row=2, column=3)

create_button(1, command=lambda: calc.set_number(1, current_text)).grid(row=3, column=0)
create_button(2, command=lambda: calc.set_number(2, current_text)).grid(row=3, column=1)
create_button(3, command=lambda: calc.set_number(3, current_text)).grid(row=3, column=2)
create_button("+", command=lambda: calc.set_operation("+")).grid(row=3, column=3)

# create_button("+/-").grid(row=4, column=0)
create_button(0, command=lambda: calc.set_number(0, current_text)).grid(row=4, column=1)
# create_button(".").grid(row=4, column=2)
create_button("=", command=lambda: calc.calculate(current_text)).grid(row=4, column=3)



button_frame.pack()


tk.mainloop()
