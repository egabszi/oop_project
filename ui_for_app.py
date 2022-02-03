# csinálunk egy fő frame-t
# létrehozunk eg ycanvas objectumot
# canvashoz hozzáadjuk a scrollbart
# a canvast beállítjuk
# létre fogunk hozni egy másodlagos frame-t, amit a canvasra fogunk ráilleszteni

import os
import json
import tkinter as tk
from tkinter import Frame, ttk
from PIL import Image, ImageTk

meta_data_path = r"D:\oop_project\meta_data"

all_data = []

for item in os.listdir(meta_data_path):
    with open(os.path.join(meta_data_path, item), 'r') as data:
        all_data.append(json.load(data))

print(all_data)

class MovieMetaViewer(tk.Tk):
    def __init__(self, image_data ,*args,**kwargs):
        super().__init__(*args, **kwargs)

        container = tk.Frame(self)
        self.geometry("850x600")

        self.columnconfigure(0, weight = 1)
        self.rowconfigure(0, weight = 1)

        container.grid(row=0, column=0, sticky='nsew')
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.canvas = ImageListCanvas(container, image_data) # ide kellene egy olyan osztály példányosítás,
                                                             # amely a canvasra ráilleszti a képekkel megjelenített frame-t

class ImageListCanvas(tk.Canvas):
    def __init__(self, container, image_data):
        super().__init__(container)

        self.container = container

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.grid(row=0, column=0, sticky='nsew')

        # add scrollbar to canvas
        self.my_scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.yview)
        self.my_scrollbar.grid_columnconfigure(0, weight=1)
        self.my_scrollbar.grid_rowconfigure(0, weight=1)
        self.my_scrollbar.grid(row=0, column=0, sticky='nse')

        self.bind_all("<MouseWheel>", self._on_mousewheel)

        self.update_idletasks()
        self.yview_moveto(1.0)

        self.configure(yscrollcommand=self.my_scrollbar.set)
        self.bind("<Configure>", lambda e: self.configure(scrollregion=self.bbox('all')))

        self.frames= {}

        for FrameClass in (ImageListFrame, DetailFrame):
            if FrameClass == ImageListFrame:
                frame = FrameClass(container, self, image_data)
                self.frames[FrameClass] = frame

        self.show_frame(ImageListFrame)


    def show_frame(self, frame_class, data=None):
        self.delete('all')
        if frame_class == DetailFrame:
            frame = DetailFrame(self.container, self, data)
        else:
            frame = self.frames[frame_class]

        frame.grid(row=0, column=0, sticky='nsew')
        self.create_window(0, 0, window=frame, anchor='nw')
        frame.tkraise()


    def _on_mousewheel(self, event):
        self.yview_scroll(int(-1*(event.delta/120)), "units")

class ImageListFrame(ttk.Frame):
    def __init__(self, container, controller, image_data):
        super().__init__(container)

        self.container = container
        self.image_data = image_data
        self.image = None
        self.controller = controller

        # frame settings
        
        self.columnconfigure(0, weight=1)

        self.images_to_grid()

    def images_to_grid(self):
        row_num = -1
        col_num = -1
        for _idx, item in enumerate(self.image_data):
            # itt meg kell nyitni a képet
            # létrehozok egy labelt és a labelnek állítom be a képet mint háttér image
            self.image = ImageFrame(self, self.controller, item)
            label = ttk.Label(self)
            label.image = self.image
            col_num += 1
            if _idx%4 == 0:
                row_num += 1
                col_num = 0
            self.image.grid(row=row_num, column=col_num, columnspan=1, sticky='nsew')

class ImageFrame(ttk.Frame):
    def __init__(self, container, controller, image_data):
        super().__init__(container)

        self.image = ImageTk.PhotoImage(Image.open(image_data['poster_location']).resize((200,350)))
        
        self.label = ttk.Label(self, image=self.image, text=image_data['original_title'])
        self.label.bind('<Button-1>', lambda e: controller.show_frame(DetailFrame, image_data))

        self.label.grid(row=0, column=0, sticky= 'nsew')

class DetailFrame(ttk.Frame):
    def __init__(self, container, controller, image_data):
        super().__init__(container)

        self.grid(row=0, column=0, sticky='nsew')
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.image = ImageTk.PhotoImage(Image.open(image_data['poster_location']).resize((200,350)))
        self.image_label = ttk.Label(self, image=self.image, text=image_data['original_title'])

        self.image_label.grid(row=1, column=0, rowspan=2, sticky='new', padx=(0,10), pady=(5,0))

        overview_label = ttk.Label(self,
        text=image_data['overview'],
        wraplength=200,
        anchor='w',
        justify='left')

        overview_label.grid(row=1, column=1, sticky='w')

        back_button = ttk.Button(
            self,
            text='Back',
            command=lambda: controller.show_frame(ImageListFrame)
            )

        back_button.grid(row=0, column=0, sticky='w')

        # play_button = ttk.Button(
        #     self,
        #     text='Play me',
        #     command= lambda: os.system("start" + r"D:\oop_project\movies\Aladdin.mkv")
        #     command= lambda: os.system("start" + image_data['data_location'])
        # )
        play_button = ttk.Button(self, text = 'Play me')

        play_button.grid(row=2, column=1, sticky='W')

        def reconfigure_message_label(envet):
            overview_label.configure(wraplength=min(container.winfo_width()- 130, 400))

        container.bind("<Configure>", reconfigure_message_label)


if __name__ == '__main__':
    app = MovieMetaViewer(all_data)
    app.mainloop()

