import boto3
from params_overrides import ParametersFile
params = ParametersFile()

from s3_buckets import S3Bucket
s3 =  S3Bucket()

class CloudFormation:
    "make the magic happen"

    aws_cfn = boto3.client('cloudformation')
    #stack_name = params.GetParameters('StackName')
    
    def CheckIfStackExists(self, StackName):
        try:
            response = aws_cfn.describe_stacks( StackName=StackName)
            return True
        except:    
            print(StackName + " does not exist.")
            return False

    def DeployStack(self, StackName, repo_name, BucketName, s3_template_url):
        if self.CheckIfStackExists(StackName) is False:
            print("No Stack Found, Lets Deploy it.")
            file_name = repo_name + '.yml'
            s3.UploadToS3(file_name, BucketName)
            AlarmEmail = params.GetParameters('AlarmEmail')
            MainQueueName = params.GetParameters('MainQueueName')
            deployment = self.aws_cfn.create_stack(
                        StackName=StackName,
                        TemplateURL=s3_template_url,
                        OnFailure='DELETE',
                        Parameters=[
                            {'ParameterKey': 'RepoName',
                             'ParameterValue': repo_name},
                             {'ParameterKey': 'AlarmEmail',
                             'ParameterValue': AlarmEmail},
                             {'ParameterKey': 'MainQueueName',
                             'ParameterValue': MainQueueName
                             }]
                        )
                                    
        else:
            print("Not doing...")