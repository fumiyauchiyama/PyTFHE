import numpy as np
from typing import Union

class torus32(np.uint32):
    def __new__(cls, value:float):
        uint32_value = np.uint32(np.round((value%1) * (2**32)))
        return super().__new__(cls, uint32_value)

if __name__ == "__main__":

    a = np.linspace(-3, 3, 17)
    for i in a:
        t = torus32(i)
        print(f"{i:<10} {format(t, '032b'):<10}")