# -*- coding: utf-8 -*-
from aiida.orm.data import Data

# you can subclass Data or or any data type listed under 'verdi data'
class UnsignedInteger(Data):
    """Represents an unsigned integer.
    """

    def __init__(self, value=1):
        """Constructor

        default value is 1.
        """
        super(Data, self).__init__()
        self.value = value

    @property
    def value(self):
        """value attribute.

        Uses get_attr method from aiida.orm.data.Data
        """
        return self.get_attr('value', None)

    @value.setter
    def value(self, value):
        """value setter.

        Convenience method that allows to write 'a.value = 5'
        """
        is_uint = type(value) == int and value >= 0
        if not is_uint:
            raise ValueError("Accept only unsigned integers")

        self._set_attr('value', value)

    def __mul__(self, other):
        """Multiplication operator for unsigned integers.

        Convenience method that allows to write 'c = a * b' instead of  
        c = UnsignedInteger()
        c.value = a.value * b.value )
        """
        if isinstance(other, UnsignedInteger):
            return UnsignedInteger(self.value * other.value)
        elif isinstance(other, int):
            return UnsignedInteger(self.value * other)
        else:
            raise TypeError("addition not implemented for type {}".format(type(other)))


