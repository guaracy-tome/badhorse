# badhorse
Any parameters file structure (*_parameters.json) 
{"parameter_name":"value"}

https://badhorse.s3-eu-west-1.amazonaws.com/sqs_consumer_infra.yml

The specified queue does not exist for this wsdl version. (Service: AmazonSQS; Status Code: 400; Error Code: AWS.SimpleQueueService.NonExistentQueue; Request ID: e7f39307-aae5-5aa9-bd2b-c4c1a92d117d; Proxy: null)

{
                                        'ParameterKey': 'RepoName',
                                        'ParameterValue': 'sqs_consumer_infra',
                                        'ParameterKey': 'AlarmEmail',
                                        'ParameterValue': 'tome.guaracy@gmail.com',
                                        'ParameterKey': 'MainQueueName',
                                        'ParameterValue': 'BadHorseMainQueue',
                                        'ParameterKey': 'StackName',
                                        'ParameterValue': 'BadHorseSQSInfra'
                                    })


                                    curl -d "Action=SendMessage&Version=2011-10-01&MessageBody=example" <your queue url>

                                    https://sqs.eu-west-1.amazonaws.com/646115910218/BadHorseMainQueue