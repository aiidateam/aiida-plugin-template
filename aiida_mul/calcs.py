import json

from aiida.orm.calculation.job import JobCalculation
from aiida.common.utils import classproperty
from aiida.common.exceptions import (InputValidationError, ValidationError)
from aiida.common.datastructures import (CalcInfo, CodeInfo)
from aiida.orm import DataFactory

ParameterData = DataFactory('parameter')


class MultiplyCalculation(JobCalculation):
    '''AiiDA plugin for simple "multiplication" code
    
    Simple AiiDA plugin for wrapping a code that adds two numbers.
    '''

    def _init_internal_params(self):
        # reuse base class function
        super(MultiplyCalculation, self)._init_internal_params()

        self._INPUT_FILE_NAME = 'in.json'
        self._OUTPUT_FILE_NAME = 'out.json'
        # mul.product entry point defined in setup.json
        self._default_parser = 'mul.product'

    @classproperty
    def _use_methods(cls):
        """Additional use_* methods for the namelists class.
        """
        retdict = JobCalculation._use_methods
        retdict.update({
            "parameters": {
                'valid_types': ParameterData,
                'additional_parameter': None,
                'linkname': 'parameters',
                'docstring': ("Use a node that specifies the input parameters ")
                },
            })
        return retdict

    def _prepare_for_submission(self, tempfolder, inputdict):
            """Create input files.

            :param tempfolder: aiida.common.folders.Folder subclass where
                the plugin should put all its files.
            :param inputdict: dictionary of the input nodes as they would
                be returned by get_inputs_dict
            """
            # Check inputdict
            try:
                parameters = inputdict.pop(self.get_linkname('parameters'))
            except KeyError:
                raise InputValidationError("No parameters specified for this "
                                           "calculation")
            if not isinstance(parameters, ParameterData):
                raise InputValidationError("parameters is not of type "
                                           "ParameterData")
            try:
                code = inputdict.pop(self.get_linkname('code'))
            except KeyError:
                raise InputValidationError("No code specified for this "
                                           "calculation")
            if inputdict:
                raise ValidationError("Input can only be parameter node")

            # In this example, the input file is simply a json dict.
            # Adapt for your particular code!
            input_json = parameters.get_dict()

            # Write input to file
            input_filename = tempfolder.get_abs_path(self._INPUT_FILE_NAME)
            with open(input_filename, 'w') as infile:
                json.dump(input_json, infile)

            # Prepare CalcInfo to be returned to aiida
            calcinfo = CalcInfo()
            calcinfo.uuid = self.uuid
            calcinfo.local_copy_list = []
            calcinfo.remote_copy_list = []
            calcinfo.retrieve_list = [self._OUTPUT_FILE_NAME]

            codeinfo = CodeInfo()
            codeinfo.cmdline_params = [self._INPUT_FILE_NAME, self._OUTPUT_FILE_NAME]
            codeinfo.code_uuid = code.uuid
            calcinfo.codes_info = [codeinfo]

            return calcinfo
