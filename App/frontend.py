from flask import Flask, jsonify, request
import backend

app = Flask(__name__)

# API call to get SID
@app.route('/api/sid/<string:airport_code>', methods=['GET'])
def get_sid(airport_code):
    
    response = backend.calculate_sid(airport_code)
    
    return jsonify(response)

# API call to get Stars
@app.route('/api/stars/<string:airport_code>', methods=['GET'])
def get_stars(airport_code):
    response = backend.calculate_stars(airport_code)
    
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=False, port=8000)