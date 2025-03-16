import infra.boto3_client as boto3_client

def put_json_file(json_file, json_name):

    filename =  f'{json_name}.json'

    boto3_client.put_object(
        filename,
        json_file,
        "application/json"
    )


def file_exists(path):
    file = boto3_client.get_file_by_path(path)

    return file
   