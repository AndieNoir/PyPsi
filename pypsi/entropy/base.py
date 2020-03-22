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


class Entropy:

    def __init_subclass__(cls, friendly_name, order, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.friendly_name = friendly_name
        cls.order = order

    def get_bytes(self, length):
        pass

    def get_bias_amplified_bytes(self, length):
        amplified_bytes = []
        amplified_byte = 0
        bit_counter = 0
        while len(amplified_bytes) < length:
            unamplified_bytes = self.get_bytes(length * 5)
            for byte in unamplified_bytes:
                for k in range(0, 8, 2):
                    bit1 = byte >> k & 1
                    bit2 = byte >> k + 1 & 1
                    if bit1 == bit2:
                        amplified_byte = amplified_byte << 1 | bit1
                        bit_counter += 1
                        if bit_counter == 8:
                            amplified_bytes.append(amplified_byte)
                            amplified_byte = 0
                            bit_counter = 0
        return bytes(amplified_bytes[:length])
