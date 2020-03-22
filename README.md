PyPsi
=====

A Python program for experimenting with psychic abilities.

![Screenshot](https://i.imgur.com/5Xdnwp4.png)

Running
-------

```bash
pip install -r requirements.txt
python -m pypsi
```

Note: For Linux, you might need to install `python3-tk` or `python3-tkinter` before running

Adding a new entropy
--------------------

1.  Create a class that extends `Entropy` and override the `get_bytes` method

    Example:

    ```python
    # pypsi/entropy/dev_hwrng.py
    
    from pypsi.entropy.base import Entropy
    
    
    class DevHwrng(Entropy, friendly_name="/dev/hwrng", order=99):
    
       def get_bytes(self, length):
           return open('/dev/hwrng', 'rb').read(length)
    ```

2.  Register the created class on `config.py`

    ```python
    # pypsi/config.py
    
    from entropy.dev_hwrng import DevHwrng
    
    
    ENTROPY_LIST = [
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
