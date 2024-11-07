from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route('/webhooks', methods=['GET', 'POST', 'PUT', 'DELETE'])
def handle_request():
    # Get request data
    request_data = {
        'method': request.method,
        'url': request.url,
        'headers': dict(request.headers),
        'args': request.args.to_dict(),
        'form': request.form.to_dict(),
        'json': request.get_json(silent=True),
        'data': request.data.decode('utf-8')
    }
    
    # Pretty-print the request data
    print(json.dumps(request_data, indent=4))

    # Return a response
    return jsonify({"message": "Request received!"}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)