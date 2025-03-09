import boto3
from dotenv import load_dotenv
import os

load_dotenv()
bucket_name = os.getenv('S3_BUCKET_NAME')


def get_session():
    return boto3.Session()

def get_bucket():
    return get_session().resource('s3').Bucket(bucket_name)

def put_object(key, json_object, content_type):

    get_bucket().put_object(
        Bucket=bucket_name, 
        Key=key,
        Body=json_object,
        ContentType=content_type
    )