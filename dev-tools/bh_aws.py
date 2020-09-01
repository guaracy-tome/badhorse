#!/usr/local/bin/python3

import json
import boto3
import sys
from s3_buckets import S3Bucket
from params_overrides import ParametersFile
from cfn_templates import CfnTemplates
from cfn_stacks import CloudFormation

### Load external functions ####
params = ParametersFile() 
s3 = S3Bucket()
cfnt = CfnTemplates()
cfns = CloudFormation()

### Genaral variables ####
BucketName = 'badhorse'
aws_region = 'eu-west-1'
stack_name = params.GetParameters('StackName')
file_name, template_name, parameters_file = params.FilesNames()
s3_template_url = cfnt.GenerateTemplateURL(BucketName, aws_region, file_name)

def GetAction():
    try:
        action = sys.argv[1]
        return action
    except:
        return False

def RunAction():
    action = GetAction()
    if action == "run":
        try:
            run_command = sys.argv[2] + '.'+ sys.argv[3]
            eval(run_command+'()')
        except:
            print("No Commands defined or any other problem. Go Home!")
    elif action == "deploy":
        cfns.DeployStack(file_name, stack_name, BucketName, s3_template_url)
    elif action == "delete":
        cfns.DeleteStack(stack_name)
    elif action == "validate":
        cfns.DeleteStack(s3_template_url)
    elif action == False:
        print("No Action Defined. Go home!")

#print(cfns.CheckIfStackExists())
### Do Something #####        
RunAction()