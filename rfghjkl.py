import tkinter
import math

class a():
    def __init__(self, bar_radius, bar_border_width, bar_in_start, width_scale, from_, to, color_bar, color_bar_border):
        self.bar_radius, self.bar_border_width, self.bar_in_start, self.width_scale, self.from_, self.to = bar_radius, bar_border_width, bar_in_start, width_scale, from_, to
        self.color_bar, self.color_bar_border = color_bar, color_bar_border
        
        self.C = tkinter.Canvas(
            height = bar_radius + bar_border_width * 2,
            width = width_scale,
            bg = 'red'
        )
        self.C.pack()
        pos = (self.bar_in_start - self.from_) * (self.width_scale / (self.to - self.from_))

        self.C.create_rectangle(
            math.ceil(pos - self.bar_radius / 2 - self.bar_border_width / 2),
            self.bar_border_width,
            # 0,
            math.ceil(pos + self.bar_radius / 2 + self.bar_border_width / 2),
            self.bar_radius + self.bar_border_width * 2,
            # 10,

            fill = self.color_bar,
            outline = self.color_bar_border,
            width = self.bar_border_width
        )

if __name__ == '__main__':
    window = tkinter.Tk()
    window.geometry('1000x100+1000+750')

    tkS = a(
        from_ = 0,
        to = 10,
        width_scale = 1000,
        bar_in_start = 5,
        bar_radius = 7,
        bar_border_width = 0,
        color_bar = '#ffffff',
        color_bar_border = '#bababa'

    )

    window.mainloop()
