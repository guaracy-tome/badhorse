

class CfnTemplates:
    "deal with CloudFormation Templates"

    def GenerateTemplateURL(self, BucketName, aws_region, repo_name):
        s3_template_url = 'https://' + BucketName + '.s3-' + aws_region + '.amazonaws.com/' + repo_name + '.yml'
        return s3_template_url
