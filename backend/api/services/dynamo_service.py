import os
import boto3
from botocore.exceptions import ClientError

class DynamoDBService:
    def __init__(self):
        self.client = boto3.client(
            'dynamodb',
            aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
            aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),
            region_name=os.getenv('AWS_REGION')
        )
        self.table_name = os.getenv('DYNAMODB_TABLE', 'default-table')
    
    # ... rest of the class methods ...