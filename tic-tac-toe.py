import tkinter as tk
import tkinter.messagebox

window = tk.Tk()

window.geometry("400x560")
window.title("Tic-Tac-Toe")

#  window.resizable(0, 0)

empty_spaces = 0
p1_wins = tk.IntVar(0)
p2_wins = tk.IntVar(0)

btn_click = True


btn1 = tk.Button(window, text="", width=10, height=10, font="Helvetica", borderwidth=4, relief="groove",
                 justify="center", padx=1, pady=1, command=lambda: on_button_click(btn1))
btn1.grid(row=1, column=1)  # need this to be separate

btn2 = tk.Button(window, text="", width=10, height=10, font="Helvetica", borderwidth=4, relief="groove",
                 justify="center", padx=1, pady=1, command=lambda: on_button_click(btn2))
btn2.grid(row=1, column=2)

btn3 = tk.Button(window, text="", width=10, height=10, font="Helvetica", borderwidth=4, relief="groove",
                 justify="center", padx=1, pady=1, command=lambda: on_button_click(btn3))
btn3.grid(row=1, column=3)

btn4 = tk.Button(window, text="", width=10, height=10, font="Helvetica", borderwidth=4, relief="groove",
                 justify="center", padx=1, pady=1, command=lambda: on_button_click(btn4))
btn4.grid(row=2, column=1)
btn5 = tk.Button(window, text="", width=10, height=10, font="Helvetica", borderwidth=4, relief="groove",
                 justify="center", padx=1, pady=1, command=lambda: on_button_click(btn5))
btn5.grid(row=2, column=2)

btn6 = tk.Button(window, text="", width=10, height=10, font="Helvetica", borderwidth=4, relief="groove",
                 justify="center", padx=1, pady=1, command=lambda: on_button_click(btn6))
btn6.grid(row=2, column=3)

btn7 = tk.Button(window, text="", width=10, height=10, font="Helvetica", borderwidth=4, relief="groove",
                 justify="center", padx=1, pady=1, command=lambda: on_button_click(btn7))
btn7.grid(row=3, column=1)

btn8 = tk.Button(window, text="", width=10, height=10, font="Helvetica", borderwidth=4, relief="groove",
                 justify="center", padx=1, pady=1, command=lambda: on_button_click(btn8))
btn8.grid(row=3, column=2)

btn9 = tk.Button(window, text="", width=10, height=10, font="Helvetica", borderwidth=4, relief="groove",
                 justify="center", padx=1, pady=1, command=lambda: on_button_click(btn9))
btn9.grid(row=3, column=3)


def on_button_click(button):
    global btn_click
    global empty_spaces
    if btn_click is True and len(button["text"]) == 0:  # check whose turn it is and if string is empty
        btn_click = False
        button["text"] = "X"
        button.config(fg="blue")  # button had no text color before, need to configure this new option
        empty_spaces += 1
        check()  # check after we change button text so we can identify winning situation after X or O placed
    elif btn_click is False and len(button["text"]) == 0:
        btn_click = True
        button["text"] = "O"
        button.config(fg="red")
        empty_spaces += 1
        check()


def check():  # all the winning situations, also adds 1 to the winner's total score
    global p1_wins
    global p2_wins
    if (btn1["text"] == "X") and (btn2["text"] == "X") and (btn3["text"] == "X"):
        tk.messagebox.showinfo("Winning Situation!", "Player 1 Wins!")
        p1_wins.set(p1_wins.get() + 1)
        new_game()
    elif (btn1["text"] == "O") and (btn2["text"] == "O") and (btn3["text"] == "O"):
        tk.messagebox.showinfo("Winning Situation!", "Player 2 Wins!")
        p2_wins.set(p2_wins.get() + 1)
        new_game()
    elif (btn1["text"] == "X") and (btn4["text"] == "X") and (btn7["text"] == "X"):
        tk.messagebox.showinfo("Winning Situation!", "Player 1 Wins!")
        p1_wins.set(p1_wins.get() + 1)
        new_game()
    elif (btn1["text"] == "O") and (btn4["text"] == "O") and (btn7["text"] == "O"):
        tk.messagebox.showinfo("Winning Situation!", "Player 2 Wins!")
        p2_wins.set(p2_wins.get() + 1)
        new_game()
    elif (btn1["text"] == "X") and (btn5["text"] == "X") and (btn9["text"] == "X"):
        tk.messagebox.showinfo("Winning Situation!", "Player 1 Wins!")
        p1_wins.set(p1_wins.get() + 1)
        new_game()
    elif (btn1["text"] == "O") and (btn5["text"] == "O") and (btn9["text"] == "O"):
        tk.messagebox.showinfo("Winning Situation!", "Player 2 Wins!")
        p2_wins.set(p2_wins.get() + 1)
        new_game()
    elif (btn1["text"] == "X") and (btn4["text"] == "X") and (btn7["text"] == "X"):
        tk.messagebox.showinfo("Winning Situation!", "Player 1 Wins!")
        p1_wins.set(p1_wins.get() + 1)
        new_game()
    elif (btn1["text"] == "O") and (btn4["text"] == "O") and (btn7["text"] == "O"):
        tk.messagebox.showinfo("Winning Situation!", "Player 2 Wins!")
        p2_wins.set(p2_wins.get() + 1)
        new_game()
    elif (btn2["text"] == "X") and (btn5["text"] == "X") and (btn8["text"] == "X"):
        tk.messagebox.showinfo("Winning Situation!", "Player 1 Wins!")
        p1_wins.set(p1_wins.get() + 1)
        new_game()
    elif (btn2["text"] == "O") and (btn5["text"] == "O") and (btn8["text"] == "O"):
        tk.messagebox.showinfo("Winning Situation!", "Player 2 Wins!")
        p2_wins.set(p2_wins.get() + 1)
        new_game()
    elif (btn3["text"] == "X") and (btn6["text"] == "X") and (btn9["text"] == "X"):
        tk.messagebox.showinfo("Winning Situation!", "Player 1 Wins!")
        p1_wins.set(p1_wins.get() + 1)
        new_game()
    elif (btn3["text"] == "O") and (btn6["text"] == "O") and (btn9["text"] == "O"):
        tk.messagebox.showinfo("Winning Situation!", "Player 2 Wins!")
        p2_wins.set(p2_wins.get() + 1)
        new_game()
    elif (btn4["text"] == "X") and (btn5["text"] == "X") and (btn6["text"] == "X"):
        tk.messagebox.showinfo("Winning Situation!", "Player 1 Wins!")
        p1_wins.set(p1_wins.get() + 1)
        new_game()
    elif (btn4["text"] == "O") and (btn5["text"] == "O") and (btn6["text"] == "O"):
        tk.messagebox.showinfo("Winning Situation!", "Player 2 Wins!")
        p2_wins.set(p2_wins.get() + 1)
        new_game()
    elif (btn7["text"] == "X") and (btn8["text"] == "X") and (btn9["text"] == "X"):
        tk.messagebox.showinfo("Winning Situation!", "Player 1 Wins!")
        p1_wins.set(p1_wins.get() + 1)
        new_game()
    elif (btn7["text"] == "O") and (btn8["text"] == "O") and (btn9["text"] == "O"):
        tk.messagebox.showinfo("Winning Situation!", "Player 2 Wins!")
        p2_wins.set(p2_wins.get() + 1)
        new_game()
    elif (btn3["text"] == "X") and (btn5["text"] == "X") and (btn7["text"] == "X"):
        tk.messagebox.showinfo("Winning Situation!", "Player 1 Wins!")
        p1_wins.set(p1_wins.get() + 1)
        new_game()
    elif (btn3["text"] == "O") and (btn5["text"] == "O") and (btn7["text"] == "O"):
        tk.messagebox.showinfo("Winning Situation!", "Player 2 Wins!")
        p2_wins.set(p2_wins.get() + 1)
        new_game()
    elif empty_spaces == 9:
        tk.messagebox.showinfo("No winner!", "Cat's Game!")
        new_game()


def reset_board():
    global btn_click
    global empty_spaces
    btn_click = btn_click  # the player who lost starts next
    empty_spaces = 0
    btn1["text"] = ""
    btn2["text"] = ""
    btn3["text"] = ""
    btn4["text"] = ""
    btn5["text"] = ""
    btn6["text"] = ""
    btn7["text"] = ""
    btn8["text"] = ""
    btn9["text"] = ""


def new_game():
    global p1_wins
    global p2_wins
    again = tk.messagebox.askyesno("Next Game?", "Do you want to play again?")
    if again == 1:
        reset_board()
    else:
        if p1_wins.get() > p2_wins.get():
            tk.messagebox.showinfo("Winner!", "Player 1 is the Winner!")
            window.quit()
        elif p1_wins.get() < p2_wins.get():
            tk.messagebox.showinfo("Winner", "Player 2 is the winner!")
            window.quit()
        else:
            tk.messagebox.showinfo("Tie", "You tied!")
            window.quit()


tk.Label(window, textvariable=p1_wins, fg="blue", font="Helvetica").grid(row=4, column=1)

tk.Label(window, textvariable=p2_wins, fg="red", font="Helvetica").grid(row=4, column=2)


window.mainloop()
