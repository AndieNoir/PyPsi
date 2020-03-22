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

import threading
import tkinter

from pypsi import config


class RedGreenGameFrame(tkinter.Frame):

    def __init__(self, parent, *args, **kwargs):
        tkinter.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.entropy_objects = [entropy_class() for entropy_class in config.ENTROPY_LIST]

        self.parent.wm_title('Red/Green Game - PyPsi')
        self.parent.configure(background='black')

        self.trial_result_canvas = tkinter.Canvas(master=self.parent, width=152, height=152, bg='black', highlightthickness=0)
        self.rect_id = self.trial_result_canvas.create_rectangle(0, 0, 150, 150, outline='white', fill='black')
        self.trial_result_canvas.pack(side=tkinter.TOP, pady=(50, 0))

        entropy_options_frame = tkinter.Frame(master=self.parent, bg='black')
        entropy_options_frame.pack(side=tkinter.TOP, pady=(50, 0), padx=25)

        entropy_options_label = tkinter.Label(master=entropy_options_frame, text='Entropy:', bg='black', fg='white')
        entropy_options_label.pack(side=tkinter.LEFT)

        entropy_options = [entropy_object.friendly_name for entropy_object in sorted(self.entropy_objects, key=lambda x: x.order)]
        self.entropy_options_menu_variable = tkinter.StringVar(self.parent, value=entropy_options[0])
        self.entropy_options_menu = tkinter.OptionMenu(entropy_options_frame, self.entropy_options_menu_variable, *entropy_options)
        self.entropy_options_menu.configure(width=30, highlightthickness=0)
        self.entropy_options_menu.pack(side=tkinter.TOP, padx=(5, 0))

        self.amplifier_checkbutton_variable = tkinter.BooleanVar(master=self.parent, value=False)
        self.amplifier_checkbutton = tkinter.Checkbutton(master=self.parent, text='Enable bias amplifier', variable=self.amplifier_checkbutton_variable,
                                                         bg='black', fg='white', activebackground='black', activeforeground='white', selectcolor='black', highlightthickness=0)
        self.amplifier_checkbutton.pack(side=tkinter.TOP, pady=(15, 0))

        self.run_reset_button = tkinter.Button(master=self.parent, text='Run', width=5, highlightthickness=0, command=lambda: threading.Thread(target=self.on_run_reset_button_click).start())
        self.run_reset_button.pack(side=tkinter.TOP, pady=15)

    def on_run_reset_button_click(self):
        if self.run_reset_button.cget('text') == 'Run':
            self.run_reset_button.configure(state=tkinter.DISABLED)
            selected_entropy = next(filter(lambda x: x.friendly_name == self.entropy_options_menu_variable.get(), self.entropy_objects))
            enable_bias_amplifier = self.amplifier_checkbutton_variable.get()
            trial_result = 0
            random_bytes = selected_entropy.get_bytes_amplified(config.BITS_PER_TRIAL // 8) if enable_bias_amplifier else selected_entropy.get_bytes(config.BITS_PER_TRIAL // 8)
            for i in range(0, len(random_bytes)):
                for k in range(0, 8 if i < len(random_bytes) - 1 else 7):  # use even bits to prevent a tie
                    trial_result += 0.5 if (random_bytes[i] >> k & 1 == 1) else -0.5
            self.trial_result_canvas.itemconfig(self.rect_id, fill='lime' if trial_result > 0 else 'red')
            self.run_reset_button.configure(text='Reset')
            self.run_reset_button.configure(state=tkinter.NORMAL)
        else:
            self.trial_result_canvas.itemconfig(self.rect_id, fill='black')
            self.run_reset_button.configure(text='Run')
