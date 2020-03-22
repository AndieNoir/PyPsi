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

import tkinter

from pypsi.ui.classic_reg import ClassicRegExperimentFrame
from pypsi.ui.red_green import RedGreenGameFrame


class HomeFrame(tkinter.Frame):

    def __init__(self, parent, *args, **kwargs):
        tkinter.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.parent.wm_title('PyPsi')
        self.parent.configure(background='black')

        classic_reg_experiment_button = tkinter.Button(master=self.parent, text='Classic REG Experiment', width=30, highlightthickness=0, command=lambda: ClassicRegExperimentFrame(tkinter.Toplevel(self.parent)))
        classic_reg_experiment_button.pack(side=tkinter.TOP, padx=25, pady=(25, 0))

        red_green_game_button = tkinter.Button(master=self.parent, text='Red/Green Game', width=30, highlightthickness=0, command=lambda: RedGreenGameFrame(tkinter.Toplevel(self.parent)))
        red_green_game_button.pack(side=tkinter.TOP, padx=25, pady=(15, 25))

