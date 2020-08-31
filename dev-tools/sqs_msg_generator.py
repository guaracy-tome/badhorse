#!/usr/bin/python

import json
import boto3
import sys

queue_url = sys.argv[1]
how_many = int(sys.argv[2])

# Create SQS client
sqs_aws = boto3.client('sqs')

class sqs_generator:
    def sendsqs(self):
        for _ in range(how_many):
            # Send message to SQS queue
            response = sqs_aws.send_message(
                QueueUrl=queue_url,
                DelaySeconds=10,
                MessageAttributes={
                    'Title': {
                        'DataType': 'String',
                        'StringValue': 'BadHorseTest'
                    },
                    'Author': {
                        'DataType': 'String',
                        'StringValue': 'Guaracy Tome'
                    },
                    'WeeksOn': {
                        'DataType': 'Number',
                        'StringValue': '2'
                    }
                },
                MessageBody=(
                    'Information about current NY Times fiction bestseller for '
                    'week ofhdgakdghkasgdkagdkga016.'
                )
        )

            print(response['MessageId'])

    def sqs_delete(self, receipt_handle, message):
        # Delete received message from queue
        sqs_aws.delete_message(
            QueueUrl=queue_url,
            ReceiptHandle=receipt_handle
        )
        print('Received and deleted message: %s' % message)

    def sqs_reader(self):
        # Receive message from SQS queue
        response = sqs_aws.receive_message(
            QueueUrl=queue_url,
            AttributeNames=[
                'SentTimestamp'
            ],
            MaxNumberOfMessages=2,
            MessageAttributeNames=[
                'All'
            ],
            VisibilityTimeout=0,
            WaitTimeSeconds=0
        )
        message = response['Messages'][0]
        receipt_handle = message['ReceiptHandle']
        sqs_delete(self, receipt_handle, message)
    
    

sqs = sqs_generator()
sqs.sqs_reader()
#sqs.sendsqs()