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

from pypsi.entropy.anu import Anu
from pypsi.entropy.pseudo import Pseudo
from pypsi.entropy.random_org import RandomOrg
from pypsi.entropy.temporal import Temporal


ENTROPY_CLASSES = [
    Anu,
    RandomOrg,
    Temporal,
    Pseudo,
]

BITS_PER_TRIAL = 200
