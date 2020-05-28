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

from pypsi import config


class Generator:

    def __init_subclass__(cls, friendly_name, order, **kwargs):
        super().__init_subclass__(**kwargs)
        cls.friendly_name = friendly_name
        cls.order = order

    def get_bytes(self, length):
        pass

    def get_bias_amplified_bytes(self, length):
        # Scott A. Wilber, "Advances in Mind-Matter Interaction Technology: Is 100 Percent Effect Size Possible?", 2013
        amplified_bytes = []
        amplified_byte = 0
        amplified_byte_set_bit_count = 0
        random_walk_deviation = 0
        while len(amplified_bytes) < length:
            unamplified_bytes = self.get_bytes(math.ceil(1.5 * length * (config.BIAS_AMPLIFICATION_FACTOR ** 2)))
            for byte in unamplified_bytes:
                for k in range(8):
                    random_walk_deviation += 1 if (byte >> k & 1 == 1) else -1
                    if random_walk_deviation == config.BIAS_AMPLIFICATION_FACTOR or random_walk_deviation == -config.BIAS_AMPLIFICATION_FACTOR:
                        amplified_byte = amplified_byte << 1 | (1 if random_walk_deviation > 0 else 0)
                        random_walk_deviation = 0
                        amplified_byte_set_bit_count += 1
                        if amplified_byte_set_bit_count == 8:
                            amplified_bytes.append(amplified_byte)
                            amplified_byte = 0
                            amplified_byte_set_bit_count = 0
        return bytes(amplified_bytes[:length])
