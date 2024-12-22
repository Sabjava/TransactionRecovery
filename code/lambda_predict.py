import json

import boto3
import json
import os

ENDPOINT_NAME = "transaction-predict-1"
def lambda_handler(event, context):
    sagemaker_runtime = boto3.client('sagemaker-runtime')
    endpoint_name = ENDPOINT_NAME
    input_data = event.get('input_data')  # Default example data

    try:
        response = sagemaker_runtime.invoke_endpoint(
            EndpointName=endpoint_name,
            ContentType='text/csv',  
            Body=input_data
        )

        result = response['Body'].read().decode('utf-8')
        return {
            'statusCode': 200,
            'body': json.dumps({'prediction': result})
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
