from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg
)

import matplotlib.pyplot as plt

from tkinter import ttk

import serial.tools.list_ports

import os
import json
import ast


def menu_bar(self,tk):
    menubar = tk.Menu(self._tk)
    filemenu = tk.Menu(menubar, tearoff=0)
    filemenu.add_command(label="Open")
    filemenu.add_command(label="Save As", command=self._save_file)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=self._quit)
    menubar.add_cascade(label="File", menu=filemenu)
    self._tk.config(menu=menubar)

def entry_box_di_kanan(self,tk,banyaknya):
    container = tk.Frame(self._tk)
    container.pack(side=tk.RIGHT)
    self.canvas = tk.Canvas(container,width=110,height=490)
    self.scrollbar = tk.Scrollbar(container, orient="vertical", command=self.canvas.yview,)
    self.scrollable_frame = tk.Frame(self.canvas)
    
    
    self.scrollable_frame.bind(
        "<Configure>",
        lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
    )

    self.canvas.bind_all("<MouseWheel>", self._on_mousewheel)

    # self._tk.bind_all("<MouseWheel>", self._on_mousewheel,  add='+')

    self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

    self.canvas.configure(yscrollcommand=self.scrollbar.set)
    count=0
    self._enteries=[]
    self.string_vars = []
    for i in range(banyaknya):
        # i = len(self.string_vars)
        self.string_vars.append(tk.StringVar())
        self.string_vars[i].trace("w", lambda name, index, mode, var=self.string_vars[i], i=i:self.entryupdate(var, i))            
        count=i
        test = tk.Label(self.scrollable_frame, text=((i+1)*250))
        e=tk.Entry(self.scrollable_frame, textvariable=self.string_vars[i], width=10)
        # for j in range(3):
        test.configure(bg='white')
        print(len(self.string_vars))
        test.grid(row = count, column=0)
        e.grid(row = count, column=1)
        self._enteries.append(e)
    
    self.scrollable_frame.configure(bg='white')
    self.scrollbar.configure(bg='white')
    self.canvas.configure(bg='white')
    container.configure(bg='white')

        
    self.canvas.grid(column=0,row=0)
        # self.scrollbar.pack(side="right", fill="y")   
    self.scrollbar.grid(column=1,row=0, sticky="ns")

    self.canvas_send_serial = tk.Canvas(container,width=110,height=60)
    
    self.canvas_send_serial.grid(column=0,row=1,columnspan=2)
    save_button = tk.Button(self.canvas_send_serial, text="Save File", command=self._save_file)
    save_button.pack()


def grafik_interaktif(self):
    self._figure = plt.figure(figsize=(16, 5), dpi=100)
    figure_canvas = FigureCanvasTkAgg(self._figure, self._tk)
    self._tk.title("CDI Mapping Software")

    figure_canvas.get_tk_widget().pack(expand=False)
    
    axes = plt.subplot(1, 1, 1)
    # axes.set_xlim(0,55000)
    axes.set_ylim(-20, 80)
    axes.grid(which="both")
    self._axes = axes
    # self._figure.set_size_inches(6, 6)
    plt.subplots_adjust(left=0.04, right=0.99, top=0.95, bottom=0.1)
    # self._figure.canvas.toolbar.pack_forget()

    #initialize coordinate awal
    x, y = zip(*sorted(self._points.items()))
    self._line, = self._axes.plot(x, y, marker="o", markersize=5,color="red")
    axes.set_facecolor("black")
    self._figure.canvas.draw()

    #event handler
    self._figure.canvas.mpl_connect('button_press_event', self._on_click)
    self._figure.canvas.mpl_connect('button_release_event', self._on_release)
    self._figure.canvas.mpl_connect('motion_notify_event', self._on_motion)
    
    # create FigureCanvasTkAgg object
    self._tk.protocol("WM_DELETE_WINDOW", self._quit)

    # self._tk.mainloop()

    # plt.show()

from watchpoints import watch

global tampung

def preset_dan_com(self,tk):
    container_preset = tk.Frame(self._tk, bg= "white")
    self.canvas_preset = tk.Canvas(container_preset,width=110,height=20,bg="white",border=1)
    self.combo = ttk.Combobox(self.canvas_preset,state="readonly",values=["Preset 1", "Preset 2", "Preset 3", "Preset 4"])
    self.combo.bind("<<ComboboxSelected>>", lambda e: selection_changed(self))
    self.combo.grid(column=1,row=0)
    preset = tk.Label(self.canvas_preset, text="Preset",bg="white")
    preset.grid(column=0,row=0)
    
    B = tk.Button(self.canvas_preset,text ="Refresh", command = lambda : get_com_ports(self))
    B.grid(column=2,row=0)
    self.combo_port = ttk.Combobox(self.canvas_preset,state="readonly",values=self._tampung)
    self.combo_port.grid(column=3,row=0)
    # watch(self._tampung)
    # print(self._tampung)
    container_preset.pack(fill=tk.X)
    self.canvas_preset.pack()



def selection_changed(self):
    selection = self.combo.get()

    f = open(("presets/{}.fck").format(selection), "r")
    test=f.read()
    # print((test))
    res = ast.literal_eval(test)
    # print(type(res))
    self._points=res
    self._update_plot()
    # print(selection)

def get_preset():
    file = os.listdir("presets")
    for file in os.listdir("../presets"):
        if (file.endswith(".fck")):
            print(os.path.join("/mydir", file))
    print(file)

def get_com_ports(self):
   # Get a list of available serial ports
    ports = serial.tools.list_ports.comports()
    self._tampung=[]
    
    # Print each port name
    for port in ports:
        # print(port.device)
        self._tampung.append(port.device)
    
    self.combo_port['values']=self._tampung
    if not self._tampung:
        self.combo_port.set("")        
    else:
        self.combo_port.current(0)
    # print(self._tampung)
    # return self._tampung
    



