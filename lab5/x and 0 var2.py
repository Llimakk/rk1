from tkinter import *
from tkinter import messagebox
import time

tk = Tk()
app_run = True

f_size_x = 600
f_size_y = 600

def on_closing():
    global app_run
    if messagebox.askokcancel("Выход из игры", "Вы хотите выйти из игры?"):
        app_run = False
        tk.destroy()


tk.protocol("WM_DELETE_WINDOW", on_closing)

tk.title("Крестики-нолики")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
field = Canvas(tk, width=f_size_x, height=f_size_y, bd=0, highlightthickness=0)
field.create_rectangle(0,0,f_size_x, f_size_y,fill="white")
field.pack()
tk.update()


s_x = 3
s_y = s_x
step_x = f_size_x // s_x
step_y = f_size_y // s_y

def table():
    for i in range(0, s_x + 1):
        field.create_line(0, i * step_y, f_size_x, i * step_y)
    for i in range(0,s_y+1):
         field.create_line(i*step_y,0,i*step_y,f_size_y)


def check_winner(who):
    for j in range(0,s_y):
        win = True
        for i in range(0,s_x):
            if points[j][i] != who:
                win = False
        if win:
            return True
    for j in range(0,s_y):
        win = True
        for i in range(0,s_x):
            if points[i][j] != who:
                win = False
        if win:
            return True

    win = True
    for i in range(0,s_y):
        print(points[i][i])
        if points[i][i] != who:
            win = False
    if win:
        return True


points = [[-1 for i in range(s_x)] for i in range(s_x)]
print(points)
list_ids = []
table()

class Point:
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.type = type

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

def draw_point(x, y, type):
    size = 25
    color = "black"
    id = 0
    if type == 0:
        color = "red"
        id = field.create_oval(x * step_x, y * step_y, x * step_x + step_x, y * step_y + step_y, fill=color)
        id2 = field.create_oval(x * step_x + size, y * step_y + size, x * step_x + step_x - size, y * step_y + step_y - size, fill="white")
        list_ids.append(id)
        list_ids.append(id2)
    if type == 1:
        color = "blue"
        id = field.create_rectangle(x * step_x, y * step_y+ step_y//2-step_y//10, x * step_x+step_x, y * step_y + step_y//2+step_y//10, fill=color)
        id2 = field.create_rectangle(x * step_x+ step_x // 2 - step_x // 10, y * step_y, x * step_x+ step_x // 2 + step_x // 10, y * step_y + step_y, fill=color)
        list_ids.append(id)
        list_ids.append(id2)

    print(type)


def add_points(event):
    global points
    type = 0
    if event.num == 3:
        type = 1
    if points[event.x // step_x][event.y // step_y] == -1:
        points[event.x // step_x][event.y // step_y] = type
        draw_point(event.x // step_x, event.y // step_y, type)
        if check_winner(type):
            print("Победитель", type)
            points = [[10 for i in range(s_x)] for i in range(s_x)]

field.bind_all("<Button-1>", add_points)
field.bind_all("<Button-3>", add_points)

def button_press():
    global list_ids
    global points
    print(list_ids)
    for i in list_ids:
        field.delete(i)
    list_ids = []
    print(list_ids)
    points = [[-1 for i in range(s_x)] for i in range(s_x)]

b1 = Button(tk, text="Начать заново!", command=button_press)
b1.pack()



while app_run:
    if app_run:
        tk.update_idletasks()
        tk.update()
    time.sleep(0.005)
