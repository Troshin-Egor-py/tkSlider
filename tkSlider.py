import tkinter


class tkSilder(tkinter.Widget):
    def __init__(
            self,
            window,

            # Value
            past: int|float,
            to:   int|float,

            # Scale
            len_scale:          int,
            color_scale:        str = 'cacaca',
            rounding_ends:      bool = True,
            color_to_bar:       False|str = False,
            scale_border_width: int = 1,
            color_scale_border: str = '9d9d9d',

            # Bar
            bar_radius:       int = 10,
            color_bar:        str = '#ffffff',
            bar_border_width: int = 1,
            color_bar_border: str = 'bababa'
    ) -> None:
        # Init variables
        # Value
        self.past = past
        self.to = to

        # Scale
        self.len_scale =          len_scale
        self.color_scale =        color_scale
        self.rounding_ends =      rounding_ends
        self.color_to_bar =       color_to_bar
        self.scale_border_width = scale_border_width
        self.color_scale_border = color_scale_border

        # Bar
        self.bar_radius =       bar_radius
        self.color_bar =        color_bar
        self.bar_border_width = bar_border_width
        self.color_bar_border = color_bar_border


        self.Canva = tkinter.Canvas(
            background = 'systemTransparent'
        )
        