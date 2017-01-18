#!/usr/bin/env runaiida
# -*- coding: utf-8 -*-
import sys
import os
import click

@click.command('submit_mul')
@click.argument('codename') #, help='Name of the Code')
@click.argument('computer_name') #, help='Name of the Computer')
@click.option('--send', is_flag=True)
def main(codename, computer_name, send):
    from aiida.common.exceptions import NotExistent
    ParameterData = DataFactory('parameter')

# The name of the code setup in AiiDA

################################################################
    if send:
        submit_test = False
    else:
        submit_test = True

    code = Code.get_from_string(codename)
# The following line is only needed for local codes, otherwise the
# computer is automatically set from the code
    computer = Computer.get(computer_name) 

# These are the two numbers to sum
    parameters = ParameterData(dict={'x1':2,'x2':3})

    calc = code.new_calc()
    calc.label = "Test mul"
    calc.description = "Test calculation with the aiida_mul code"
    calc.set_max_wallclock_seconds(30*60) # 30 min
    calc.set_computer(computer)
    calc.set_withmpi(False)
    calc.set_resources({"num_machines": 1})

    calc.use_parameters(parameters)

    if submit_test:
        subfolder, script_filename = calc.submit_test()
        print "Test submit file in {}".format(os.path.join(
            os.path.relpath(subfolder.abspath),
            script_filename
            ))
    else:
        calc.store_all()
        calc.submit()
        print "submitted calculation; calc=Calculation(uuid='{}') # ID={}".format(
            calc.uuid,calc.dbnode.pk)

if __name__ == '__main__':
    main()
