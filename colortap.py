import tkinter as tk
import random

def buttons():
    
    def whitefx():
    	global redch
    	button.config(bg = "red")
    	button.config(command = redbx)
    	redch += 1
    
    def redbx():
        global redch
        button.config(bg="white")
        redch -= 1
        button.config(command = whitefx)
        check_restart()

    def check_restart():
        if redch == 0:
            restart()

    def restart():
        global che, ygen, xgen, redch, scorenum
        for widget in w.winfo_children():
            widget.destroy()
        redch = 0
        che = 0
        ygen = 400
        xgen = 63
        scorenum += 1
        score = tk.Label(w, text = "Score: "+str(scorenum), font = ("",10,""), bg = "white",fg = "black")
        score.place(y = 330, x = 280)
		
        for i in range(9):
            buttons()

    global xgen, ygen, che, redch, scorenum
    bg = random.choice(["red", "white"])
    button = tk.Button(w, bg=bg, width=7, height=4)
    button.place(y=ygen, x=xgen)
    xgen += 200
    che += 1
    if che == 3:
        ygen += 180
        xgen = 63
    if che == 6:
        ygen += 180
        xgen = 63
    if bg == "red":
        redch += 1
        button.config(command=redbx)
    if bg == "white":
    	button.config(command = whitefx)

w = tk.Tk()
w.config(bg="black")



redch = 0
che = 0
ygen = 400
xgen = 63
scorenum = 0
score = tk.Label(w, text = "Score: "+str(scorenum), font = ("",10,""), bg = "white",fg = "black")
score.place(y = 330, x = 280)

for i in range(9):
    buttons()

w.mainloop()
