import json
import os

class ParametersFile:
    "Deals with Parameters file"

    def FilesNames(self):
        files_list = os.listdir(os.getcwd())
        for files in files_list:
            if files.endswith('.yml'):
                template_name = files[:-4]
                file_name = files
            elif files.endswith('.yaml'):
                template_name = files[:-5]
                file_name = files
        parameters_file = template_name + '_parameters.json'
        return file_name, template_name, parameters_file

    def ReadParameters(self):
        file_name, template_name, parameters_file = self.FilesNames()
        with open(parameters_file) as json_file:
            parameters_data = json.load(json_file)
        return parameters_data

    def GetParameters(self, parameter_name):
        parameters_data = self.ReadParameters()
        for key in parameters_data['Parameters']:
            value = key['ParameterValue']
        return value  

    def StackParameters(self):
        parameters_data = self.ReadParameters()
        stack_params = parameters_data['Parameters']
        return stack_params
