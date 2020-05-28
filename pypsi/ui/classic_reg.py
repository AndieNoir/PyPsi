# Copyright (C) 2020 AndieNoir
#
# This file is part of PyPsi.
#
# PyPsi is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PyPsi is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with PyPsi.  If not, see <https://www.gnu.org/licenses/>.

import math
import os
import threading
import time
import tkinter

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from pypsi import config


class ClassicRegExperimentFrame(tkinter.Frame):

    def __init__(self, parent, *args, **kwargs):
        tkinter.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.generator_objects = sorted([generator_class() for generator_class in config.GENERATOR_CLASSES], key=lambda x: x.order)

        self.parent.wm_title('Classic REG Experiment - PyPsi')
        self.parent.configure(background='black')
        if os.name == 'nt':
            self.parent.state('zoomed')
        else:
            self.parent.attributes('-zoomed', True)

        plt.style.use('dark_background')
        figure = Figure()
        self.plot = figure.add_subplot(1, 1, 1)
        self.cumdev_x = [0]
        self.cumdev_y = [0]
        self.canvas = FigureCanvasTkAgg(figure, master=self.parent)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

        self.z_score_label = tkinter.Label(master=self.parent, text='Z-Score: +0.000', bg='black', fg='white', font='TkFixedFont')
        self.z_score_label.pack(side=tkinter.TOP)

        generator_options_frame = tkinter.Frame(master=self.parent, bg='black')
        generator_options_frame.pack(side=tkinter.TOP, pady=(25, 0))

        generator_options_label = tkinter.Label(master=generator_options_frame, text='Generator:', bg='black', fg='white')
        generator_options_label.pack(side=tkinter.LEFT)

        generator_options = [generator_object.friendly_name for generator_object in sorted(self.generator_objects, key=lambda x: x.order)]
        self.generator_options_menu_variable = tkinter.StringVar(self.parent, value=generator_options[0])
        self.generator_options_menu = tkinter.OptionMenu(generator_options_frame, self.generator_options_menu_variable, *generator_options)
        self.generator_options_menu.configure(width=30, highlightthickness=0)
        self.generator_options_menu.pack(side=tkinter.TOP, padx=(5, 0))

        self.amplifier_checkbutton_variable = tkinter.BooleanVar(master=self.parent, value=False)
        self.amplifier_checkbutton = tkinter.Checkbutton(master=self.parent, text='Enable bias amplifier', variable=self.amplifier_checkbutton_variable,
                                                         bg='black', fg='white', activebackground='black', activeforeground='white', selectcolor='black', highlightthickness=0)
        self.amplifier_checkbutton.pack(side=tkinter.TOP, pady=(15, 0))

        self.start_reset_button = tkinter.Button(master=self.parent, text='Start', width=5, highlightthickness=0, command=lambda: threading.Thread(target=self.on_start_reset_button_click).start())
        self.start_reset_button.pack(side=tkinter.TOP, pady=15)

        self.update_graph()

    def on_start_reset_button_click(self):
        if self.start_reset_button.cget('text') == 'Start':
            self.start_reset_button.configure(state=tkinter.DISABLED)
            self.generator_options_menu.configure(state=tkinter.DISABLED)
            self.amplifier_checkbutton.configure(state=tkinter.DISABLED)
            selected_generator = next(filter(lambda x: x.friendly_name == self.generator_options_menu_variable.get(), self.generator_objects))
            enable_bias_amplifier = self.amplifier_checkbutton_variable.get()
            for _ in range(0, 100):
                start_time = time.time()
                trial_result = 0
                random_bytes = selected_generator.get_bias_amplified_bytes(config.BITS_PER_TRIAL // 8) if enable_bias_amplifier else selected_generator.get_bytes(config.BITS_PER_TRIAL // 8)
                for byte in random_bytes:
                    for k in range(0, 8):
                        trial_result += 0.5 if (byte >> k & 1 == 1) else -0.5
                self.cumdev_x.append(self.cumdev_x[-1] + 1)
                self.cumdev_y.append(self.cumdev_y[-1] + trial_result)
                self.update_graph()
                self.z_score_label['text'] = 'Z-Score: %+.3f' % (self.cumdev_y[-1] / (math.sqrt(len(self.cumdev_y) * config.BITS_PER_TRIAL) / 2))
                sleep_duration = 0.5 - (time.time() - start_time)
                if sleep_duration > 0:
                    time.sleep(sleep_duration)
            self.start_reset_button.configure(text='Reset')
            self.start_reset_button.configure(state=tkinter.NORMAL)
            self.generator_options_menu.configure(state=tkinter.NORMAL)
            self.amplifier_checkbutton.configure(state=tkinter.NORMAL)
        else:
            self.start_reset_button.configure(text='Start')
            self.cumdev_x = [0]
            self.cumdev_y = [0]
            self.update_graph()

    def update_graph(self):
        self.plot.clear()
        self.plot.set_xlim(left=0, right=100)
        self.plot.set_ylim(top=1.645 * math.sqrt(100 * config.BITS_PER_TRIAL), bottom=-1.645 * math.sqrt(100 * config.BITS_PER_TRIAL))
        self.plot.set_xticks(np.arange(0, 100, 10))
        self.plot.set_yticks([])
        self.plot.plot(np.arange(0, 100, 0.01), 1.645 * np.sqrt(np.arange(0, 100, 0.01) * config.BITS_PER_TRIAL) / 2, 'red')
        self.plot.plot(np.arange(0, 100, 0.01), -1.645 * np.sqrt(np.arange(0, 100, 0.01) * config.BITS_PER_TRIAL) / 2, 'blue')
        self.plot.plot(np.arange(0, 100, 0.01), 0 * np.arange(0, 100, 0.01), 'lime')
        self.plot.plot(self.cumdev_x, self.cumdev_y, 'white')
        self.canvas.draw()
