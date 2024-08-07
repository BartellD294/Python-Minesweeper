import Cell
from tkinter import *
import random

WIDTH = 600
HEIGHT = 600
TOP_HEIGHT = HEIGHT*(2/10)
BIG_HEIGHT = HEIGHT + TOP_HEIGHT
NUM_ROWS = 10
NUM_COLS = 10
NUM_MINES = 10
CELL_W = WIDTH/NUM_COLS
CELL_H = HEIGHT/NUM_ROWS

class Minesweeper:

    flagCount = 0
    totalMines = 0
    field = [Cell]

    def __init__(self, root):
        top_frame = Frame(root, width=WIDTH, height = TOP_HEIGHT, bg = "gray14")
        top_frame.pack()
        self.remaining_label = Label(text=Cell.Cell.tiles_to_clear)
        self.remaining_label.place(y=TOP_HEIGHT/2)
        main_frame = Frame(root, width=WIDTH, height = HEIGHT, bg = "gray")
        main_frame.pack()
        for i in range (0,NUM_ROWS):
            main_frame.grid_rowconfigure(i, weight=1, uniform=True)
        for i in range (0,NUM_COLS):
            main_frame.grid_columnconfigure(i, weight = 1, uniform=True)
        for i in range (0,NUM_ROWS):
            for j in range (0,NUM_COLS):
                #print(i,j)
                new_c = Cell.Cell(main_frame, w=100, h=100, x=j, y=i,text=(""))#R"+str(i)+"C"+str(j)))
                self.field.append(new_c)
                #print(i,j, self.field[i][j].btn.cget('text'))
                new_c.btn.grid(row=i, column=j, sticky=NSEW)
#button width and height must be set to arbitrarily large numbers to shrink into grid, because they will not expand=
        self.randomize_mines()

    def get_cell(self,x,y):
        for c in self.field:
            if c.x==x and c.y==y:
                return c

    def randomize_mines(self):
        cells = random.sample(self.field, NUM_MINES)
        for cel in cells:
            #print(cel.btn.cget("text"))
            cel.set_mine()

def game_over():
    print("Game Over!")


def game_win():
    print("You Win!")

def main():

    root = Tk()
    root.title("Minesweeper")
    root.geometry(str(WIDTH) + "x" + str(int(BIG_HEIGHT)))
    root.configure(bg="black")
    game = Minesweeper(root)
    root.mainloop()

if __name__ == "__main__":
    main()