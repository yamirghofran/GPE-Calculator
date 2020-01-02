from Tkinter import *

window = Tk()
window.title("MGH App")
lbl = Label(window, text="Gravitational Potential Energy Calculator")
lbl.grid(column=0, row=0)
window.geometry("600x600")
mass_q = Label(window, text="What is the mass in kilograms?")
mass_q.grid(column=0, row=1)
Mass = Entry(window, width=5)
Mass.grid(column=1, row=1)
kg = Label(window, text = "kg")
kg.grid(column = 2, row = 1)
height_q = Label(window, text="What is the height in meters?")
height_q.grid(column=0, row=2)
Height = Entry(window, width=5)
Height.grid(column=1, row=2)
meters = Label(window, text = "meters")
meters.grid(column = 2, row = 2)




def solve_gpe():
    sol = str(float(Mass.get()) * 9.8 * float(Height.get()))
    answer = "The GPE is " + sol + " KJ"
    solution.configure(text = answer)
    return sol

solve = Button(window, text="Solve GPE", command = solve_gpe)
solve.grid(column=1, row=3)
solution = Label(window, text = "The GDP will show here")
solution.grid(column = 0, row = 4)

window.mainloop()
