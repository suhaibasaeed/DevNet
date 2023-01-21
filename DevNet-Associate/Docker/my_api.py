from flask import Flask, jsonify

app = Flask(__name__)

# URL we're going to hit with GET request
@app.route('/api/endpoint', methods=['GET'])
def get_data():
    """
    :return: Returns JSON response indicating 200 - OK
    """
    return (jsonify({'message': 'received'}), 200)

# Run the flask API on the localhost server
if __name__ == '__main__':
    app.run(host='0.0.0.0')