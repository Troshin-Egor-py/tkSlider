import tkinter
import math


window = tkinter.Tk()
window.geometry('1000x100+1000+750')

from_ = 0
to = 10
width_scale = 1000
bar_in_start = 15
bar_radius = 10
bar_border_width = 0
color_bar = '#ffffff'
color_bar_border = '#bababa'


C =  tkinter.Canvas(
    height = (bar_radius + bar_border_width * 2),
    width = width_scale,
    bg = 'red'
)
C.pack()
pos = (bar_in_start - from_) * (width_scale / (to - from_))

print(
    math.ceil(pos - bar_radius / 2 - bar_border_width / 2),
    bar_border_width,
    math.ceil(pos + bar_radius / 2 + bar_border_width / 2),
    bar_radius + bar_border_width * 2,
)

C.create_rectangle(
    math.ceil(pos - bar_radius / 2 - bar_border_width / 2),
    bar_border_width,
    # 0,
    math.ceil(pos + bar_radius / 2 + bar_border_width / 2),
    bar_radius + bar_border_width * 2,
    # 10,

    fill = color_bar,
    outline = color_bar_border,
    width = bar_border_width
)
window.mainloop()
