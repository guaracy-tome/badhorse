import logging
import boto3
from botocore.exceptions import ClientError

class S3Bucket:
    "deal with S3 buckets"

    aws_s3 = boto3.client('s3')
    def UploadToS3(self, file_name, BucketName, object_name=None):
        "Upload a file to an S3 bucket"

        # If S3 object_name was not specified, use file_name
        if object_name is None:
            object_name = file_name

        # Upload the template
        try:
            response = self.aws_s3.upload_file(file_name, BucketName, object_name)
            print("File Uploaded to: " + BucketName )
        except ClientError as e:
            logging.error(e)
            return False
        return True