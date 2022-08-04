#Tic-tac-toe Game this game is play with two members
from tkinter import *
from tkinter import messagebox

window = Tk()
window.title(" Tic-Tac-Toe game ")
window.geometry("500x400")
window.configure(bg='#89d68d')

lbl = Label(text="Tic-tac-toe Game", font=('Times New Roman', '15'), fg='red')
lbl.grid(row=1, column=1)
lbl = Label(text="Player 1 is = X", font=('Times New Roman', '10'))
lbl.grid(row=2, column=1)
lbl = Label(text="Player 2 is = O", font=('Times New Roman', '10'))
lbl.grid(row=3, column=1)

turn = 1  # For first person turn.

def clicked():
    global turn
    if turn == 1:
        turn = 2
        return "X"
    elif turn == 2:
        turn = 1
        return "O"

# For getting the text of a button
def pressbtn1():
    global turn
    if btn1["text"] == " ":  
        btn1["text"] = clicked()
        check()

def pressbtn2():
    global turn
    if btn2["text"] == " ":
        btn2["text"] = clicked()
        check()

def pressbtn3():
    global turn
    if btn3["text"] == " ":
        btn3["text"] = clicked()
        check()

def pressbtn4():
    global turn
    if btn4["text"] == " ":
        btn4["text"] = clicked()
        check()

def pressbtn5():
    global turn
    if btn5["text"] == " ":
        btn5["text"] = clicked()
        check()

def pressbtn6():
    global turn
    if btn6["text"] == " ":
        btn6["text"] = clicked()
        check()

def pressbtn7():
    global turn
    if btn7["text"] == " ":
        btn7["text"] = clicked()
        check()

def pressbtn8():
    global turn
    if btn8["text"] == " ":
        btn8["text"] = clicked()
        check()

def pressbtn9():
    global turn
    if btn9["text"] == " ":
        btn9["text"] = clicked()
        check()
        
# Getting value from each button,
# to check for any possible win event
def check():
    global flag
    a1 = btn1["text"] 
    a2 = btn2["text"] 
    a3 = btn3["text"]
    a4 = btn4["text"]
    a5 = btn5["text"]
    a6 = btn6["text"]
    a7 = btn7["text"]
    a8 = btn8["text"]
    a9 = btn9["text"]
    flag += 1
    # Check every possible win on map
    if a1 == a2 and a1 == a3 and a1 == "O" or a1 == a2 and a1 == a3 and a1 == "X":
        win(a1)
    if a1 == a5 and a1 == a9 and a1 == "O" or a1 == a5 and a1 == a9 and a1 == "X":
        win(a1)
    if a1 == a4 and a1 == a7 and a1 == "O" or a1 == a4 and a1 == a7 and a1 == "X":
        win(a1)
    if a2 == a5 and a2 == a8 and a2 == "O" or a2 == a5 and a2 == a8 and a2 == "X":
        win(a2)
    if a3 == a6 and a3 == a9 and a3 == "O" or a3 == a6 and a3 == a9 and a3 == "X":
        win(a3)
    if a4 == a5 and a4 == a6 and a4 == "O" or a4 == a5 and a4 == a6 and a4 == "X":
        win(a4)
    if a7 == a8 and a7 == a9 and a7 == "O" or a7 == a8 and a7 == a9 and a7 == "X":
        win(a7) 
    if a7 == a5 and a7 == a3 and a7 == "O" or a7 == a5 and a7 == a3 and a7 == "X":
        win(a7)
    elif flag == 9:
        messagebox.showinfo("Tic-Tac-Toe game", "DRAW")
        window.destroy()


def win(player):
    result = "Game complete, player " + player + " wins !!!"
    messagebox.showinfo("Tic-Tac-Toe game", result)
    window.destroy()

# is used to close the program
btn1 = Button(text=" ", width=6, height=4, command=pressbtn1)
btn1.grid(column=2, row=2)
btn2 = Button(text=" ", width=6, height=4, command=pressbtn2)
btn2.grid(column=3, row=2)
btn3 = Button(text=" ", width=6, height=4, command=pressbtn3)
btn3.grid(column=4, row=2)
btn4 = Button(text=" ", width=6, height=4, command=pressbtn4)
btn4.grid(column=2, row=3)
btn5 = Button(text=" ", width=6, height=4, command=pressbtn5)
btn5.grid(column=3, row=3)
btn6 = Button(text=" ", width=6, height=4, command=pressbtn6)
btn6.grid(column=4, row=3)
btn7 = Button(text=" ", width=6, height=4, command=pressbtn7)
btn7.grid(column=2, row=4)
btn8 = Button(text=" ", width=6, height=4, command=pressbtn8)
btn8.grid(column=3, row=4)
btn9 = Button(text=" ", width=6, height=4, command=pressbtn9)
btn9.grid(column=4, row=4)

# Flag used to append (1) in every turn is occurred
flag = 0  

window.mainloop()
