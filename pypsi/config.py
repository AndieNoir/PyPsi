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

from pypsi.generator.anu import Anu
from pypsi.generator.pseudo import Pseudo
from pypsi.generator.random_org import RandomOrg
from pypsi.generator.temporal import Temporal


GENERATOR_CLASSES = [
    Anu,
    RandomOrg,
    Temporal,
    Pseudo,
]

BITS_PER_TRIAL = 200

BIAS_AMPLIFICATION_FACTOR = 2
