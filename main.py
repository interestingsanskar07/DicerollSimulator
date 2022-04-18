import tkinter
import random

root = tkinter.Tk()
root.geometry('600x600')
root.title('Dice Roll Simulator')

lbl1 = tkinter.Label(root, text='', font=('aerial', 260))

lbl2 = tkinter.Label(root, text='CLICK ROLL DICE TO GET RANDOMLY GENERATED DICE ROLL.', font=('aerial', 10))
lbl2.place(x=100, y=400)


def roll_dice():
    value = ['\u2680', '\u2681', '\u2682', '\u2683', '\u2684', '\u2685']
    result = random.choice(value)
    lbl1.configure(text=result)
    lbl1.pack()
    if (result == '\u2680'):
        lbl3 = tkinter.Label(root, text='You rolled a one! Click roll dice to roll again!', font=('aerial', 10))
        lbl3.place(x=100, y=450)
    elif (result == '\u2681'):
        lbl3 = tkinter.Label(root, text='You rolled a two! Click roll dice to roll again.', font=('aerial', 10))
        lbl3.place(x=100, y=450)
    elif (result == '\u2682'):
        lbl3 = tkinter.Label(root, text='You rolled a three! Click roll dice to roll again.', font=('aerial', 10))
        lbl3.place(x=100, y=450)
    elif (result == '\u2683'):
        lbl3 = tkinter.Label(root, text='You rolled a four! Click roll dice to roll again.', font=('aerial', 10))
        lbl3.place(x=100, y=450)
    elif (result == '\u2684'):
        lbl3 = tkinter.Label(root, text='You rolled a five! Click roll dice to roll again.', font=('aerial', 10))
        lbl3.place(x=100, y=450)
    elif (result == '\u2685'):
        lbl3 = tkinter.Label(root, text='You rolled a six! Click roll dice to roll again.', font=('aerial', 10))
        lbl3.place(x=100, y=450)


button = tkinter.Button(root, text='roll dice', foreground='red', command=roll_dice)
button.place(x=275,y=350)
root.mainloop()

