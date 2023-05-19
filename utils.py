from tkinter import Frame
import settings


def height_prct(percentage):
    return (settings.HEIGHT/100)*percentage
def width_prct(percentage):
    return (settings.WIDTH/100)*percentage
def create_frame(root,bg,width, height, x, y):
    obj =  Frame(root,bg=bg,width=width,height=height)
    obj.place(x=x,y=y)
    return obj