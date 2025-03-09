from infra.boto3_client import put_object

def put_json_object(json_object, json_name):

    filename =  f'{json_name}.json'

    put_object(
        filename,
        json_object,
        ContentType="application/json"
    )