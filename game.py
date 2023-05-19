from tkinter import *
from cell import Cell
import settings
import utils

root = Tk()

# Override the setting of the window
root.configure(bg="black")
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.title("Minesweeper Game")
root.resizable(False, False)

top_frame = utils.create_frame(
    root, 'black', settings.WIDTH, utils.height_prct(25), 0, 0)
game_title = Label(
    top_frame,
    bg='black',
    fg='white',
    text='Minesweeper Game',
    font=('',35)
)
game_title.place(x=utils.width_prct(25),y=0)
left_frame = utils.create_frame(root, 'black', utils.width_prct(
    25), utils.height_prct(75), 0, utils.height_prct(25))
centre_frame = utils.create_frame(root, 'black', utils.width_prct(75), utils.height_prct(
    75), utils.width_prct(25), utils.height_prct(25))

for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x,y)
        c.create_btn_object(centre_frame)
        c.cell_btn_obj.grid(column=x,row=y)

Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place(x=20,y=10)

Cell.randomize_mines()

# Run the Window
root.mainloop()
