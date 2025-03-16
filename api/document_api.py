import services.document_service as document_service
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api/documents', methods=['POST'])
def insert_document():

    try:

        if not request.is_json:
            return jsonify({"status": "Erro, tem que passar um json válido"}, 400)
        
        model = request.get_json()
        document_service.insert(model)

        return jsonify({"status": "Documento inserido com sucesso"}, 200)
    
    except ValueError as ve:
        return jsonify({"status": f"{ve}"}, 400)