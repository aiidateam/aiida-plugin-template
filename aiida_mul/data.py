# -*- coding: utf-8 -*-
from aiida.orm.data.parameter import ParameterData

# you can directly subclass aiida.orm.data.Data 
# or any other data type listed under 'verdi data'
class MultiplyParameters(ParameterData):
    """Input parameters for multiply calculation.
    """

    def __init__(self, x1=1, x2=1, **kwargs):
        """Constructor

        Usage: MultiplyParameters(x1=3, x2=4)

        Note: As of 2017-09, the constructor must also support a single dbnode
        argument (to reconstruct the object from a database node).
        For this reason, positional arguments are not allowed.
        """
        if 'dbnode' in kwargs:
            super(ParameterData, self).__init__(**kwargs)
        else:
            # set dictionary of ParameterData
            input_dict = { 'x1': x1, 'x2': x2 }
            super(ParameterData, self).__init__(dict=input_dict, **kwargs)

    @property
    def x1(self):
        return self.get_attr('x1', None)

    @property
    def x2(self):
        return self.get_attr('x2', None)


    def __str__(self):
        s = "x1: {}, x2: {}".format(self.x1, self.x2)
        return s
