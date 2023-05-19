

import math
from matplotlib.backend_bases import MouseEvent
import tkinter as tk
from tkinter.filedialog import asksaveasfile

import numpy as np
import penciptaan as ciptakan


class coba(object):
    def __init__(self):
        self._figure, self._axes, self._line = None, None, None
        self._dragging_point = None
        self._points = {250:0,500:0,750:0,1000:0,1250:0,1500:0,1750:0,2000:0,2250:0,2500:0,2750:0,3000:0,3250:0,3500:0,3750:0,4000:0,4250:0,4500:0,4750:0,5000:0,5250:0,5500:0,5750:0,6000:0,6250:0,6500:0,6750:0,7000:0,7250:0,7500:0,7750:0,8000:0,8250:0,8500:0,8750:0,9000:0,9250:0,9500:0,9750:0,10000:0,10250:0,10500:0,10750:0,11000:0,11250:0,11500:0,11750:0,12000:0,12250:0,12500:0,12750:0,13000:0,13250:0,13500:0,13750:0,14000:0,14250:0,14500:0,14750:0,15000:0,15250:0,15500:0,15750:0,16000:0,16250:0,16500:0,16750:0,17000:0,17250:0,17500:0,17750:0,18000:0,18250:0,18500:0,18750:0,19000:0,19250:0,19500:0,19750:0,20000:0}
        self._textbox=[]
        self._tk=tk.Tk()
        self._tampung=[]
        self.convert=[]
        self._init_plot()
        
    
    def _init_plot(self):        
        ciptakan.menu_bar(self,tk)
        ciptakan.entry_box_di_kanan(self,tk,80)
        ciptakan.preset_dan_com(self,tk)
        ciptakan.grafik_interaktif(self)
        # ciptakan.get_preset()

    ######################## \/ \/ \/ BERHUBUNGAN DENGAN TKINTER \/ \/ \/ ############################


    def _quit(self):
        self._tk.quit()
        self._tk.destroy() 

    def _save_file(self):
        f = asksaveasfile(initialfile = 'Untitled.fck',
        defaultextension=".fck",filetypes=[("FCK Documents","*.fck")])
        f.write(str(self._points))

    def _on_mousewheel(self, event):
        self.canvas.yview_scroll(int(-1*(event.delta/120)), "units")

    ######################## /\ /\ /\ BERHUBUNGAN DENGAN TKINTER /\ /\ /\ ############################
    


    ######################## \/ \/ \/ GRAFIK INTERAKTIF \/ \/ \/ ############################

    
    def entryupdate(self, sv, i):
        # print(sv, i, sv.get())
        koordinat = i*250
        hasil=sv.get()
        self._points.update ({koordinat:round(float(hasil), 1)})
        # print(self._dragging_point, "di motion")
        self._update_plot()
        # print("\n",(sorted(self._points.items())))

    def _remove_point(self, x, _):
        if x in self._points:
            self._points.pop(x)
            
    def _find_neighbor_point(self, event):
        """ Find point around mouse position
        :rtype: ((int, int)|None)
        :return: (x, y) if there are any point around mouse else None
        """
        distance_threshold = 500.0
        nearest_point = None
        min_distance = math.sqrt(2 * (100 ** 2))
        for x, y in self._points.items():
            distance = math.hypot(event.xdata - x, event.ydata - y)
            if distance < min_distance:
                min_distance = distance
                nearest_point = (x, y)
        if min_distance < distance_threshold:
            return nearest_point
        return None
    
    def _add_point(self, x, y=None):
        if isinstance(x, MouseEvent):
            
            x, y = float(x.xdata),float(x.ydata)
      
        self._points.update ({x:round(y, 1)})
        
        return round(y, 1)
       
    def _update_plot(self):
        if not self._points:
            self._line.set_data([], [])
        else:
            x, y = zip(*sorted(self._points.items()))
            # Add new plot
            if not self._line:
                self._line, = self._axes.plot(x, y, "b", marker="o", markersize=5)
            # Update current plot
            else:
                self._line.set_data(x, y)
        self._figure.canvas.draw()
    ######################## /\ /\ /\ GRAFIK INTERAKTIF /\ /\ /\ ############################


    ######################## \/ \/ \/ EVENT HANDLER \/ \/ \/ ############################

    def _on_click(self, event):
        if event.button == 1 and event.inaxes in [self._axes]:
            point = self._find_neighbor_point(event)
            if point:
                self._dragging_point = point
                

            # self._update_plot()
            # print(point[0],"neighbor")
        
    def _on_release(self, event):
        u""" callback method for mouse release event
        :type event: MouseEvent
        """
        self.convert=[]
        if event.button == 1 and event.inaxes in [self._axes] and self._dragging_point:
            # print("hehe",self._dragging_point)
            self._dragging_point = None
            self._update_plot()
            print("\n",(sorted(self._points.items())))
            hehe = dict(sorted(((self._points.items()))))
            ubah=list(hehe.values())
            self.convert = list(map(lambda x: np.uint16((x*10)), ubah))
            
            # print((self.convert[0]))
            # self.fetch()
    def _on_motion(self, event):
        u""" callback method for mouse motion event
        :type event: MouseEvent
        """
        
        if not self._dragging_point:
            return
        if event.xdata is None or event.ydata is None:
            return
        
        a=self._dragging_point[0]
        # print(a,"motion")
        self._remove_point(*self._dragging_point)
        b = self._add_point(a,event.ydata)
        self._dragging_point = a,b
        # print(self._dragging_point, "di motion")
        self._update_plot()
        
        ((self._enteries)[(int(self._dragging_point[0]/250))]).delete(0,tk.END)
        ((self._enteries)[(int(self._dragging_point[0]/250))]).insert(0,self._dragging_point[1])

    ######################## /\ /\ /\ EVENT HANDLER /\ /\ /\ ############################

if __name__ == "__main__":

    plot = coba()
    plot._tk.mainloop()


