import json
import os
import logging
# request handles the request and response, jsonify converts the response to JSON and give us custom status codes
from flask import Flask, request, jsonify
from flask.logging import create_logger

# Create the Flask app by calling Flask Class
app = Flask(__name__)
# Pass in the app to create_logger to get a logger object
LOG = create_logger(app)

# Set up application and dynamically determine the path that this script is running in
script_dir = os.path.dirname(os.path.realpath(__file__))
# Creat log file in same directory as script - specify format of logs and level of logging to debug
logging.basicConfig(filename=f'{script_dir}\\filename.log', level=logging.DEBUG,
                    format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
LOG.info(f"script directory: {script_dir}")
# Specify DB file in same directory as script
LOG.info(f"DB file: {script_dir}\db.txt")

# Create endpoints
# http://127.0.0.1:5000/


@app.route('/')
def index():
    return jsonify({'name': 'ssaeed',
                    'email': 'suhaib@saeed.com',
                    'locale': 'https://youtube.com/c/ss'})

# GET http://127.0.0.1:5000/routers?hostname=SW1

# Add a GET method to the /routers endpoint
@app.route('/routers', methods=['GET'])
# Run this function when the endpoint is hit
def getRouter():
    try:
        # Parse through query string
        hostname = request.args.get('hostname')
        print(hostname)
        if (hostname is None) or (hostname == ""):
            LOG.warning('No hostname specified')
            raise ValueError
        # Open the DB file and read the data as JSON
        with open(f'{script_dir}\\db.txt', 'r') as f:
            data = f.read()
            records = json.loads(data)
            for record in records:
            # If the hostname matches the hostname in the DB, return the record and 200 OK
                if record['hostname'] == hostname:
                    # Add a log message to the log file
                    LOG.info('Routers returned')
                    return jsonify(record), 200
                if record['hostname'] != hostname:
                    LOG.warning('No matching router')
                    return jsonify({"response": "No match"}), 200
    # If the hostname is not found, return a 400 Bad Request
    except ValueError:
        LOG.error("NO HOSTNAME SPECIFIED")
        return jsonify({"error": "NO_HOSTNAME_SPECIFIED"}), 400
    except Exception as err:
        LOG.error(f'Error during GET {err}')
        return jsonify({"error": err}), 500

# POST http://127.0.0.1:5000/routers

# Add a POST method to the /routers endpoint
@app.route('/routers', methods=['POST'])
def addRouter():
    try:
        record = json.loads(request.data)
        LOG.info(f'inbound record {record}')
        with open(f'{script_dir}\\db.txt', 'r') as f:
            data = f.read()
            records = json.loads(data)
        # Check if record that came in already exists in the DB
        if record in records:
            return jsonify({"status": "Device already exists"}), 200
        # If it doesn't exist, add it to the DB and return 201 Created
        if record not in records:
            records.append(record)
            LOG.info(f"records output {records}")
            LOG.warning(f'router added {record["hostname"]}')
        # Write to DB file
        with open(f'{script_dir}\\db.txt', 'w') as f:
            f.write(json.dumps(records, indent=2))
            # Return copy of record
        return jsonify(record), 201
    except Exception as err:
        LOG.error(f'Error during ADD {err}')
        return jsonify({"error": err})

# DELETE http://127.0.0.1:5000/routers?hostname=SW1

# Delete method
@app.route('/routers', methods=['DELETE'])
def deleteRouter():
    try:
        record = json.loads(request.data)
        new_records = []
        with open(f'{script_dir}\\db.txt', 'r') as f:
            data = f.read()
            records = json.loads(data)
            # Look if record exists in DB
            for r in records:
                if r['hostname'] == record['hostname']:
                    LOG.warning(f'Deleted {r["hostname"]}')
                    continue
                # Append all records that don't match the record to new list
                new_records.append(r)
        # We create new DB file without deleted recored instead of actually deleting the record
        with open(f'{script_dir}\\db.txt', 'w') as f:
            f.write(json.dumps(new_records, indent=2))
        return jsonify(record), 204
    except Exception as err:
        LOG.error(f'ERROR RAISED: {err}')
        return jsonify({"error": err})


# Run the app
if __name__ == "__main__":
    # Run the app on localhost port 5000
    app.run(host='0.0.0.0', port=5000)
