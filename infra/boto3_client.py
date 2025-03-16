import boto3
from dotenv import load_dotenv
import os

load_dotenv()
bucket_name = os.getenv('S3_BUCKET_NAME')
profile = os.getenv('PROFILE_NAME')


def get_session():
    return boto3.Session(profile_name=profile)

def get_bucket():
    return get_session().resource('s3').Bucket(bucket_name)

def put_object(key, json_object, content_type):

    print(bucket_name)

    get_bucket().put_object(
        Bucket=bucket_name, 
        Key=key,
        Body=json_object,
        ContentType=content_type
    )

def get_file_by_path(path):
    bucket = get_bucket()

    return list(bucket.objects.filter(Prefix=path))