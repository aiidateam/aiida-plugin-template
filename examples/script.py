#!/usr/bin/env runaiida
# -*- coding: utf-8 -*-
import os

# use aiida.calculations entry point registered in setup.json
code_name = 'aiida_mul'
code = Code.get_from_string(code_name)

# The following line is only needed for local codes, otherwise the
# computer is automatically set from the code
computer_name = 'localhost'
computer = Computer.get(computer_name) 

# Prepare input parameters
ParameterData = DataFactory('parameter')
parameters = ParameterData(dict={'x1':2,'x2':3})

# set up calculation
calc = code.new_calc()
calc.label = "aiida_mul test"
calc.description = "Test job submission with the aiida_mul plugin"
calc.set_max_wallclock_seconds(30*60) # 30 min
calc.set_computer(computer)
calc.set_withmpi(False)
calc.set_resources({"num_machines": 1})
calc.use_parameters(parameters)

#if send:
#    submit_test = False
#else:
#    submit_test = True

#if submit_test:
#    subfolder, script_filename = calc.submit_test()
#    print "Test submit file in {}".format(os.path.join(
#        os.path.relpath(subfolder.abspath),
#        script_filename
#        ))
#else:
calc.store_all()
calc.submit()
print("submitted calculation; calc=Calculation(uuid='{}') # ID={}"\
        .format(calc.uuid,calc.dbnode.pk))
