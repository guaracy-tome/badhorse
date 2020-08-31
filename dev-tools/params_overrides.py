import json

class ParametersFile:
    "Deals with Parameters file"

    def ParamFilepath(self):
        ### Not used yet ###
        path = '../sqs/'
        #print(path)
        return path

    def ParamFileName(self):
        template_name = 'sqs_consumer_infra'
        parameters_file = template_name + '_parameters.json'
        return parameters_file

    def ReadParameters(self):
        parameters_file = self.ParamFileName()
        with open(parameters_file) as json_file:
            parameters_data = json.load(json_file)
        #print(parameters_data) ### Debug - Delete it
        return parameters_data

    def GetParameters(self, parameter_name):
        parameters_data = self.ReadParameters()
        for key, value in parameters_data['Parameters'].items():
            if parameter_name == key:
                #print(value) ### Debug - Delete it
                return value         

    def ListParameters(self):
        parameters_data = self.ReadParameters()
        print('Working on '+ self.ParamFileName())
        print('List of Parameters:')
        print("")
        for key, value in parameters_data['Parameters'].items():
            print(key + ': ' + value)