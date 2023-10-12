from flask import Flask, jsonify
import backend
import json

app = Flask(__name__)

#TEST

# API call to get SID
@app.route('/api/sid/<string:airport_code>', methods=['GET'])
def get_sid(airport_code):
    print("Received request: /api/sid/" + airport_code)
    # Query to backend is customizable to get more than 2 top SIDS
    response = backend.get_top_sids(airport_code)
    print("Returning response: " + json.dumps(response,indent=4))
    return jsonify(response)

# API call to get Stars
@app.route('/api/stars/<string:airport_code>', methods=['GET'])
def get_stars(airport_code):
    print("Received request: /api/stars/" + airport_code)
    # Query to backend is customizable to get more than 2 top STARS
    response = backend.get_top_stars(airport_code)
    print("Returning response: " + json.dumps(response,indent=4))
    return jsonify(response)

# API call to get Stars
@app.route('/api/healthcheck', methods=['GET'])
def healthcheck():
    print("Received request: /api/healthchec")

    #TODO - Logic to verify backend is good e.g. data source is not empty. Temporarily, we assume application health is always good
    response = "Application healthcheck is good"
    print("Returning response: " + response)
    return response

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)