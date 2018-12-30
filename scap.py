import tkinter
import random
import tkinter.messagebox

colours = ['Red', 'Brown', 'Pink', 'Blue', 'Green', 'Purple', 'Violet', 'Yellow', 'Black', 'Orange']
score =0
timeleft = 30

def startGame(Event):
    if timeleft== 30:
        countdown()
    elif timeleft ==0:
        endgame()
    nextcolor()

def endgame():
    global score
    tkinter.messagebox.showinfo("GAME OVER", " SCORE :"+ str(score))


def nextcolor():
    global score
    global timeleft
    if timeleft >0:
        e.focus_set()
        if e.get().lower() == colours[1].lower():
            score = score+1
        e.delete(0, tkinter.END)

        random.shuffle(colours)
        label.config(fg=str(colours[1]), text=str(colours[0]))
        scorelabel.config(text= " Score : "+ str(score))

def countdown():
    global timeleft
    if timeleft > 0:
        timeleft = timeleft - 1
        timelabel.config(text = "Time Left:"+ str(timeleft) )

        timelabel.after(1000, countdown)

root = tkinter.Tk()
root.title("COLOR GAME")
root.geometry("800x200")

instruction = tkinter.Label(root, text ="Enter the name of the colour and not the text!!", font = ('Helvetica', 20))
instruction.pack()
scorelabel = tkinter.Label(root, text ="Press enter to start", font = ('Helvetica', 20))
scorelabel.pack()
timelabel = tkinter.Label(root, text = "Time Left:"+ str(timeleft), font = ('Helvetica', 20))
timelabel.pack()

label = tkinter.Label(root, font = ('Helvetica', 20))
label.pack()

e = tkinter.Entry(root)
root.bind('<Return>', startGame)
e.pack()
e.focus_set()

root.mainloop()