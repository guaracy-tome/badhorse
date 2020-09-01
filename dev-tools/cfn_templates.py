

class CfnTemplates:
    "deal with CloudFormation Templates"

    def GenerateTemplateURL(self, BucketName, aws_region, file_name):
        s3_template_url = 'https://' + BucketName + '.s3-' + aws_region + '.amazonaws.com/' + file_name
        return s3_template_url

    