import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
import math
# creates window so we can add any visuals
window = tk.Tk()
window.title("Learn Python GUI")
window.geometry("800x600")

label = tk.Label(window, text="Welcome to Python", font=('Arial', 25))
# we need to provide the location of where to put the text or image, etc.
# by .pack(), the gird function, or .place() which takes in exact  x and y coordinates
label.pack(pady=20)

# two kind of text, one is an actual text box tk.Text(), the other is an entry form tk.Entry()
text = tk.Entry(window)
text.pack()
# there are other ones like tk.Checkbox(), tk.Menu(), tk.Listbox(), etc.

# install from packages : matplotlib-venn and matplotlib
# import it at the top of page
# dpi is dots per inches, the resolution
# make the graph image
fig = Figure(figsize=(5,5), dpi=100)

y = [math.sin(i / 4) for i in range(101)]
# 111 row 1 column 1 and index 1
sub_plot = fig.add_subplot(111)
sub_plot.plot(y)

# place the graph on canvas
canvas = FigureCanvasTkAgg(fig, master=window)
canvas.draw()
canvas.get_tk_widget().pack()

# gives us tools to zoom in and move around on the image
toolbar = NavigationToolbar2Tk(canvas, window)
toolbar.update()
canvas.get_tk_widget().pack()

window.mainloop()
