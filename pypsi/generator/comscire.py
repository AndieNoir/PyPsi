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

import win32com.client

from pypsi.generator.base import Generator


class ComScire(Generator, friendly_name="ComScire QNG", order=3):

    def __init__(self):
        self.qng = win32com.client.Dispatch('QWQNG.QNG')  # Windows only

    def get_bytes(self, length):
        if length <= 8192:
            self.qng.Clear()
            return self.qng.RandBytes(length)
        else:
            self.qng.Clear()
            data = bytearray()
            for x in range(int(length / 8192)):
                data.extend(bytearray(self.qng.RandBytes(8192)))
            if length % 8192 != 0:
                data.extend(bytearray(self.qng.RandBytes(length % 8192)))
            return bytes(data)
