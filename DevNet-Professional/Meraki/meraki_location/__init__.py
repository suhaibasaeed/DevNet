import logging
import json
import azure.functions as func

def main(req: func.HttpRequest, queueclient: func.Out[func.QueueMessage]) -> str:
    logging.info('Python HTTP trigger function processed a request.')
    print(req.method)
    if req.method == 'GET':
    # Log the request to queue
        queueclient.set('string')
        # Return validator from Meraki dashboard and 200 status code
        return func.HttpResponse(body='650a3212e0a8610f6e9eae1551f9e7e5727932d1', status_code=200)
    elif req.method == 'POST':
        # Parse the request body
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        # Store secret in variable
        else:
            sharedSecret = req_body.get('secret')

        # If secret is correct, log the request to queue and return 201 status code
        if sharedSecret == 'foo':
            queueclient.set(json.dumps(req_body))
            return func.HttpResponse(body=json.dumps(req_body), status_code=201, headers={'Content-Type': 'application/json'})
        # Return 401 unauthorised if secret is not correct
        else:
            return func.HttpResponse(
                body="<h1>Please pass a sharedSecret on the query string or in the request body</h1>",
                status_code=401
            )