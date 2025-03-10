import utils.json_converter as json_converter
import services.bucket_service as bucket_service
import uuid

def insert(json):
    content = json_converter.to_json(json)
    filename = f'arquivo-{uuid.uuid4()}'
    
    bucket_service.put_json_file(content, filename)