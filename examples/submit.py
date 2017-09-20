#!/usr/bin/env runaiida
# -*- coding: utf-8 -*-
import os

# use code name specified using 'verdi code setup'
code = Code.get_from_string('aiida_mul2')

# use computer name specified using 'verdi computer setup'
computer = Computer.get('localhost')

# Prepare input parameters
ParameterData = DataFactory('parameter')
parameters = ParameterData(dict={'x1':2,'x2':3})

# set up calculation
calc = code.new_calc()
calc.label = "aiida_mul test"
calc.description = "Test job submission with the aiida_mul plugin"
calc.set_max_wallclock_seconds(30*60) # 30 min
# This line is only needed for local codes, otherwise the computer is
# automatically set from the code
calc.set_computer(computer)
calc.set_withmpi(False)
calc.set_resources({"num_machines": 1})
calc.use_parameters(parameters)

calc.store_all()
calc.submit()
print("submitted calculation; calc=Calculation(uuid='{}') # ID={}"\
        .format(calc.uuid,calc.dbnode.pk))