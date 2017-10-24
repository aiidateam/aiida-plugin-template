""" Tests for calculations

"""
import os
import mock

from aiida.utils.fixtures import PluginTestCase
from aiida.utils.capturing import Capturing

import aiida_plugin_template

# computer for tests
test_computer_input = [
    "localhost",
    "my computer",
    "",
    "True",
    "ssh",
    "direct",
    "/tmp",
    "",
    "1",
    EOFError,
    EOFError,
]

plugin_path = os.path.abspath(aiida_plugin_template.__file__)

# code for tests
test_code_input = [
    "plugin-template",
    "simple script",
    "False",
    "template.multiply",
    "localhost",
    "{}/code.py".format(plugin_path),
    EOFError,
    EOFError,
]


class TestMultiply(PluginTestCase):
    BACKEND = os.environ.get('TEST_BACKEND')

    # load the backend to be tested from the environment variable
    # proceed the test command with TEST_BACKEND='django' | 'sqlalchemy

    def setUp(self):

        # set up test computer
        from aiida.cmdline.commands.computer import Computer
        test_computer = Computer()
        with mock.patch(
                '__builtin__.raw_input', side_effect=test_computer_input):
            with Capturing():
                test_computer.computer_setup()
        # load my test data

        # set up test code for test computer
        from aiida.cmdline.commands.code import Code
        test_code = Code()
        with mock.patch('__builtin__.raw_input', side_effect=test_code_input):
            with Capturing():
                test_code.code_setup()

    def test_submit(self):
        """Test submitting a calculation"""

        from aiida.orm import Code, Computer, DataFactory

        code = Code.get_from_string('plugin-template')
        computer = Computer.get('localhost')

        # Prepare input parameters
        MultiplyParameters = DataFactory('template.factors')
        parameters = MultiplyParameters(x1=2, x2=3)

        # set up calculation
        calc = code.new_calc()
        calc.label = "aiida_plugin_template computes 2*3"
        calc.description = "Test job submission with the aiida_plugin_template plugin"
        calc.set_max_wallclock_seconds(30)
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
