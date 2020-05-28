PyPsi
=====

A Python program that imitates [Psyleron Reflector](http://www.psyleron.com/software_reflector.html) to aid psychic
abilities experiments.

![Screenshot](https://i.imgur.com/tCTOjOk.png)

Running
-------

```bash
pip install -r requirements.txt
python -m pypsi
```

*Note: If you're on Linux, you need to have `python3-tk` or `python3-tkinter` installed.*

Adding a new random number generator
------------------------------------

1.  Create a class that extends `Generator` and override the `get_bytes` method

    Example:

    ```python
    # pypsi/generator/dev_hwrng.py
    
    from pypsi.generator.base import Generator
    
    
    class DevHwrng(Generator, friendly_name="/dev/hwrng", order=99):
    
       def get_bytes(self, length):
           with open('/dev/hwrng', 'rb') as f:
               return f.read(length)
    ```

2.  Register the generator class on `config.py`

    ```python
    # pypsi/config.py
    
    from pypsi.generator.dev_hwrng import DevHwrng
    
    
    GENERATOR_CLASSES = [
       DevHwrng,
       # ...
    ]
    ```

License
-------

    Copyright (C) 2020 AndieNoir

    PyPsi is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    PyPsi is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with PyPsi.  If not, see <https://www.gnu.org/licenses/>.
