import tkinter
import colorama
colorama.init(autoreset = True)


class tkSlider(tkinter.Widget):
    def __init__(
            self,
            
            # Required arguments
            master:        object,
            past:          int|float,
            to:            int|float,
            width_scale:   int,
            bar_in_start:  int|float,

            # Scale
            color_scale:        str = '#cacaca',
            rounding_ends:      bool = True,
            color_to_bar:       bool|str = False,
            height_scale:       int = 2,
            scale_border_width: int = 1,
            color_scale_border: str = '#9d9d9d',

            # Bar
            bar_radius:       int = 10,
            color_bar:        str = '#ffffff',
            bar_border_width: int = 1,
            color_bar_border: str = '#bababa'
    ) -> None:
        
        tkinter.Frame.__init__(
            self, 
            master, 
            height = bar_radius, 
            width = width_scale
        )

        # Init variables
        self.master = master

        # Value
        self.past = past
        self.to = to

        # Scale
        self.width_scale =        width_scale
        self.color_scale =        color_scale
        self.rounding_ends =      rounding_ends
        self.color_to_bar =       color_to_bar
        self.scale_border_width = scale_border_width
        self.color_scale_border = color_scale_border
        self.height_scale =       height_scale
        # Bar
        self.bar_radius =       bar_radius
        self.color_bar =        color_bar
        self.bar_border_width = bar_border_width
        self.color_bar_border = color_bar_border
        self.bar_in_start =     bar_in_start 

        self.C = tkinter.Canvas(
            height = bar_radius,
            width = width_scale
        )
        self.C.pack()

        self.draw_scale(
            start_X = self.bar_radius,
            start_Y = self.bar_radius - self.height_scale / 2,
            end_X = self.width_scale - self.bar_radius,
            end_Y = self.bar_radius - self.height_scale / 2,
            fill = self.color_scale
        )
        
    def draw_scale(
            self,
            start_X,
            start_Y,
            end_X,
            end_Y,
            fill
    ):       
        self.C.create_line(
            start_X,
            start_Y,
            end_X,
            end_Y,
            width = self.height_scale,
            fill = fill
        )



if __name__ == '__main__':
    window = tkinter.Tk()
    window.geometry('200x200+1000+750')

    tkS = tkSlider(
        master = window,
        past = 0,
        to = 10,
        width_scale = 1000,
        bar_in_start = 5,
        bar_radius = 10,
        height_scale = 2
    )

    window.mainloop()
