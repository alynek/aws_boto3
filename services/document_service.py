import services.bucket_service as bucket_service
import hashlib
import json

def insert(json):
    content = to_json(json)

    hash_content = generate_hash_by_content(content)

    filename = f'arquivo-{hash_content}'

    if the_content_already_exists(filename):   
        raise ValueError(f"O conteúdo: {filename}, já existe no bucket")     
        
    bucket_service.put_json_file(content, filename)
    return "Conteúdo salvo!"    


def generate_hash_by_content(content):
    json_string = json.dumps(content, sort_keys=True)
    return hashlib.sha256(json_string.encode()).hexdigest()


def the_content_already_exists(hash):
        file = bucket_service.file_exists(hash)
        return len(file) > 0

def to_json(object):
     return json.dumps(object)