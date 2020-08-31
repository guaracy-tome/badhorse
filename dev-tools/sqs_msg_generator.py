#!/usr/bin/python

import json
import boto3
import sys

class sqs_generator:
    def sendsqs(self):
        sqs = boto3.client('sqs')
        queue_url = 'https://sqs.eu-west-1.amazonaws.com/646115910218/BadHorseMainQueue'
        # Send message to SQS queue
        response = sqs.send_message(
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
                    'StringValue': '6'
                }
            },
            MessageBody=(
                'Information about current NY Times fiction bestseller for '
                'week of 12/11/2016.'
            )
    )

        print(response['MessageId'])

    def getsqs():
        # Create SQS client
        sqs = boto3.client('sqs')

        queue_url = 'SQS_QUEUE_URL'

        # Receive message from SQS queue
        response = sqs.receive_message(
            QueueUrl=queue_url,
            AttributeNames=[
                'SentTimestamp'
            ],
            MaxNumberOfMessages=1,
            MessageAttributeNames=[
                'All'
            ],
            VisibilityTimeout=0,
            WaitTimeSeconds=0
        )

        message = response['Messages'][0]
        receipt_handle = message['ReceiptHandle']

        # Delete received message from queue
        sqs.delete_message(
            QueueUrl=queue_url,
            ReceiptHandle=receipt_handle
        )
        print('Received and deleted message: %s' % message)

cfn = CloudFormation()
cfn.sendsqs()