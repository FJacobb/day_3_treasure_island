from tkinter import *
from tkinter import messagebox
def close():
    home.destroy()
def end():
    if answer_3.get() == "yellow":
        home.geometry("320x400")
        stage_4 = Label(home, image=img6)
        stage_4.place(x=0, y=0)
        canves = Canvas(width=305, height=94)
        canves.configure(bg="#E4BD62", highlightthickness=0)
        canves.create_image(155, 50, image=img3)
        canves.create_text(155, 45, justify=CENTER, font=("Eras Bold ITC", 9), fill="#ffffff",
            text="You found the treasure! You Win!")
        canves.place(x=8, y=290)
        butten_4 = Button(home, text="Play again", bg="#E4BD62", fg="#ffffff", command=next)
        butten_4.place(x=210, y=350)
        butten_5 = Button(home, text="The End", bg="#E4BD62", fg="#ffffff", command=close)
        butten_5.place(x=70, y=350)
    elif answer_3.get() == "red":
        messagebox.showerror("Game result", "It's a room full of fire. Game Over.")
        home.destroy()
    elif answer_3.get() == "blue":
        messagebox.showerror("Game result", "You enter a room of beasts. Game Over.")
        home.destroy()
def question_3():
    global answer_3
    if answer_2.get() == "wait":
        home.geometry("320x400")
        stage_3 = Label(home, image=img5)
        stage_3.place(x=0, y=0)
        canves = Canvas(width=305, height=94)
        canves.configure(bg="#E4BD62", highlightthickness=0)
        canves.create_image(155, 50, image=img3)
        canves.create_text(155, 45, justify=CENTER, font=("Eras Bold ITC", 9), fill="#ffffff",
            text="You arrive at the island unharmed. There is a house\nwith 3 doors. One red, one yellow and one blue.\nWhich colour do you choose?")
        canves.place(x=8, y=290)
        answer_3 = Entry(home, width=25, bg="#E4BD62")
        answer_3.place(x=60, y=360)
        butten_3 = Button(home, text="Sure", bg="#E4BD62", fg="#ffffff", command=end)
        butten_3.place(x=230, y=356)
    else:
        messagebox.showerror("Game result","You get attacked by an angry trout. Game Over.")
        home.destroy()
def question_2():
    global answer_2
    if answer_1.get() == "left":
        home.geometry("320x400")
        stage_2 = Label(home, image=img2)
        stage_2.place(x=0, y=0)
        canves = Canvas(width=305, height=94)
        canves.configure(bg="#E4BD62", highlightthickness=0)
        canves.create_image(155, 50, image=img3)
        canves.create_text(155, 45, justify=CENTER, font=("Eras Bold ITC", 9), fill="#ffffff",
            text="You've come to a lake. There is an island \nin the middle of the lake. Type 'wait' to wait \nfor a boat. Type 'swim' to swim across.")
        canves.place(x=8, y=290)
        answer_2 = Entry(home, width=25, bg="#E4BD62")
        answer_2.place(x=60, y=360)
        butten_2 = Button(home, text="Sure", bg="#E4BD62", fg="#ffffff", command=question_3)
        butten_2.place(x=230, y=356)
    else:
        messagebox.showerror("Game result", "You fell into a hole. Game Over.")
        home.destroy()


def next():
    global answer_1
    messagebox.showinfo("Mission", "Your mission is to find the treasure.")
    start.destroy()
    home.geometry("320x400")
    stage_1 = Label(home, image=img4)
    stage_1.place(x=0, y=0)
    canves = Canvas(width=305, height=94)
    canves.create_image(155, 50, image=img3)
    canves.configure(bg="#E4BD62", highlightthickness=0)
    canves.create_text(155, 45, justify=CENTER, font=("Eras Bold ITC", 9), fill="#ffffff",
        text="'You're at a cross road. Where do you want to go?\nType 'left' or 'right'")
    canves.place(x=8, y=290)
    answer_1 = Entry(home, width=25, bg="#E4BD62")
    answer_1.place(x=60, y=360)
    butten_1 = Button(home, text="Sure", bg="#E4BD62", fg="#ffffff", command=question_2)
    butten_1.place(x=230, y=356)
home = Tk()
home.title("Treasure Island")
home.geometry("320x247")
home.config(bg="#E4BD62")
img = PhotoImage(file="image/Treasure-Island.png")
img2 = PhotoImage(file="image/Asset.png")
img3 = PhotoImage(file="image/Layer 2.png")
img4 = PhotoImage(file="image/road.png")
img5 = PhotoImage(file="image/door.png")
img6 = PhotoImage(file="image/win.png")
start = Label(home, image=img)
start.place(x=-1, y=0)
wel = Label(home, text="Welcome to Treasure Island.", font=("arel", 10, "bold"))
wel.place(x=70, y=-2)
home.after(5000, next)

home.mainloop()

