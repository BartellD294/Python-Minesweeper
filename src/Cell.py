import tkinter as tk
import Minesweeper

game_over = False
remaining_label:tk.Label

class Cell:
    is_mine=False
    tiles_to_clear = -10
    all_cells=[]
    def __init__(self, root, w, h,x,y, text="", is_mine = False):
        self.is_mine = is_mine
        self.x = x
        self.y = y
        self.is_revealed = False
        self.flagged=False
        Cell.all_cells.append(self)
        Cell.tiles_to_clear += 1
        self.btn = self.create_btn(root, w, h, text)
    
    def create_btn(self, root, w, h, text):
        btn  = tk.Button(root, width=w, height=h, text=text,bg="gray40")#, width=str(5), height=str(int(h)))
        btn.bind('<Button-1>', self.l_click)
        btn.bind('<Button-3>', self.r_click)
        return(btn)
    
    def change_text(self, text):
        self.btn.config(text=text)

    def set_mine(self):
        self.is_mine=True
        #self.btn.config(text="MINE", bg="RED")
        
    def reveal(self):
        if (self.is_revealed==False):
            self.is_revealed=True
            if (self.is_mine):
                self.btn.config(text="MINE", bg="red")
                #for i in range (0, len(Cell.all_cells)):#cell in Cell.all_cells:
                #    Cell.all_cells[i].btn.bind('<Button-1>', None)
                global game_over
                game_over = True
                remaining_label.configure(text="You Lose.", bg="red")
                print(Cell.tiles_to_clear)
                remaining_label.pack()
                Minesweeper.game_over()
            else:
                Cell.tiles_to_clear -= 1
                remaining_label.configure(text=Cell.tiles_to_clear)
                print(Cell.tiles_to_clear)
                remaining_label.pack()
                num=0
                adj = self.get_adjacents()
                for i in range (len(adj)): 
                    if adj[i].is_mine==True:
                        num+=1
                self.btn.config(bg="grey80", text=num)
                if num==0:
                    for i in range (len(adj)): 
                        adj[i].reveal()
                if (Cell.tiles_to_clear == 0):
                    remaining_label.configure(text="You Win!", bg="green2")
                    print(Cell.tiles_to_clear)
                    remaining_label.pack()
                    Minesweeper.game_win()
                    
                    

    def get_cell(x,y):
        for c in Cell.all_cells:
            if c.y == y and c.x==x:
                return c



    def get_adjacents(self):
        cels = [
                Cell.get_cell(self.x-1, self.y-1),
                Cell.get_cell(self.x-1, self.y),
                Cell.get_cell(self.x-1, self.y+1),     
                Cell.get_cell(self.x, self.y-1),
                Cell.get_cell(self.x, self.y+1),
                Cell.get_cell(self.x+1, self.y-1),
                Cell.get_cell(self.x+1, self.y),
                Cell.get_cell(self.x+1, self.y+1)
            ]
        cels = [cell for cell in cels if cell is not None]
        return cels
    
    def l_click(self, event):
        #print(event, "left click")
        #print(self.is_revealed)
        if (self.is_revealed==False and self.flagged==False and game_over==False):
            self.reveal()

    def r_click(self, event):
        #print(event, "right click")
        if (self.flagged==True and game_over==False):
            self.flagged=False
            self.btn.config(bg="gray40", text="")
        elif (self.is_revealed==False and game_over==False):
            self.flagged=True
            self.btn.config(bg="yellow", text="FLAGGED")