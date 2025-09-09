from typing import Literal

class NumericIncertitude:
    value: float
    incertitude: float
    incertitude_type: Literal["absolute"] | Literal["relative"]

    def __init__(self, 
                value, 
                magnitude, 
                incertitude, 
                incertitude_type):
        self.value = value*10^magnitude
        self.incertitude_type = incertitude_type
        if incertitude_type == "absolute":
            self.incertitude = incertitude * 10^magnitude
        else:
            self.incertitude = incertitude

    def absolute(self):
        pass

    def relative(self):
        pass

    def __add__(self, other: NumericIncertitude):
        pass

    def __sub__(self, other: NumericIncertitude):
        pass

    def __mul__(self, other: NumericIncertitude):
        pass

    def __truediv__(self, other: NumericIncertitude):
        pass
        