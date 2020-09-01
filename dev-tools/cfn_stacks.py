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

    def ValidateTemplate(self, file_name):
        ### Not used yet.
        response = aws_cfn.validate_template(
                                            TemplateBody='string',
                                            TemplateURL='string'
                                        )

    def DeployStack(self, file_name, StackName, repo_name, BucketName, s3_template_url):
        s3.UploadToS3(file_name, BucketName)
        if self.CheckIfStackExists(StackName) is False:
            print("No Stack Found, Lets Deploy it.")
            
            Parameters = params.StackParameters()
            deployment = self.aws_cfn.create_stack(
                        StackName=StackName,
                        TemplateURL=s3_template_url,
                        OnFailure='DELETE',
                        Parameters=Parameters )
                                    
        else:
            print("Not doing...")

    def DeleteStack(self, StackName):
        response = aws_cfn.delete_stack( StackName='StackName')