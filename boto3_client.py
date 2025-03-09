import boto3
from dotenv import load_dotenv
import os

load_dotenv()

def get_session():
    return boto3.Session()

def get_bucket():
    bucket_name = os.getenv('S3_BUCKET_NAME')
    return get_session().resource('s3').Bucket(bucket_name)
