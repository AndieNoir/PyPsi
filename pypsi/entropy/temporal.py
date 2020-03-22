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

import requests

from pypsi.entropy.base import Entropy


class Temporal(Entropy, friendly_name="Gamblevore's TemporalLib", order=2):

    def get_bytes(self, length):
        return bytes.fromhex(requests.get('https://devapi.randonauts.com/entropy?size=%d&temporal=true&raw=true' % (length * 2)).json()['Entropy'])
