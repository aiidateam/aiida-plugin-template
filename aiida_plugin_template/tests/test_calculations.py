""" Tests for calculations

"""
import os

from aiida.utils.fixtures import PluginTestCase


class TestMultiply(PluginTestCase):
    BACKEND = os.environ.get('TEST_BACKEND')

    # load the backend to be tested from the environment variable
    # proceed the test command with TEST_BACKEND='django' | 'sqlalchemy

    def get_localhost(localhost_dir='/tmp'):
        """Fixture for a local computer called localhost"""
        from aiida.orm import Computer
        computer = Computer(
            name='localhost',
            description='my computer',
            hostname='localhost',
            workdir=localhost_dir,
            transport_type='local',
            scheduler_type='direct',
            enabled_state=True)
        return computer

    def setUp(self):

        # set up test computer
        computer = self.get_localhost()
        self.computer = computer

    def test_empty(self):
        pass
