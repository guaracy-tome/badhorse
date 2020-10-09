import boto3, sys
from params_overrides import ParametersFile
from s3_buckets import S3Bucket
s3 =  S3Bucket()
params = ParametersFile()

class CloudFormation:
    "make the magic happen"

    aws_cfn = boto3.client('cloudformation')    
    def CheckIfStackExists(self, StackName):
        # if StackName == None:
        #     print("Running Stand alone. I'll take care of everything")
        #     StackName = sys.argv[4]
        try:
            print("testing this stack: "+ StackName)
            response = self.aws_cfn.describe_stacks( StackName=StackName)
            return True
        except:    
            print(StackName + " does not exist.")
            return False

    def ValidateTemplate(self, s3_template_url):
        ### Not used yet.
        response = aws_cfn.validate_template( TemplateURL=s3_template_url )
        print(response)

    def CreateStack(self, StackName, s3_template_url, Parameters):
        print("No Stack Found, Lets Deploy it.")
        response = self.aws_cfn.create_stack(
                    StackName=StackName,
                    TemplateURL=s3_template_url,
                    OnFailure='DELETE',
                    Capabilities=['CAPABILITY_IAM'],
                    Parameters=Parameters )
        print(response)

    def UpdateStack(self, StackName, s3_template_url, Parameters):
        print("Stack Found, Lets Update it.")
        response = self.aws_cfn.update_stack(
                    StackName=StackName,
                    TemplateURL=s3_template_url,
                    Capabilities=['CAPABILITY_IAM'],
                    Parameters=Parameters )
        print(response)

    def DeployStack(self, file_name, StackName, BucketName, s3_template_url):
        s3.UploadToS3(file_name, BucketName)
        Parameters = params.StackParameters()
        if self.CheckIfStackExists(StackName) is False:
            self.CreateStack( StackName, s3_template_url, Parameters )                      
        else:
            self.UpdateStack( StackName, s3_template_url, Parameters)
    
    def DeleteStack(self, StackName):
        response = self.aws_cfn.delete_stack( StackName=StackName)
        print(response) 