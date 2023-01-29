from time import sleep
import requests

base_url = "https://api.discogs.com/"

backoffs = {
    # Multiply wait time by this factor
    "factor": 1.3,
    # Initial wait time
    "wait": 1,
    # Stop infinite loop
    "max_tries": 5
}

def get_releases(release_id):
    # Hit delay endpoint with seconds delayed reponse
    endpoint = f"releases/{release_id}"

    print(f"Getting release {release_id}")
    # GET request
    response = requests.get(base_url + endpoint)
    data = response.json()
    resp_code = response.status_code
    
    return resp_code

for i in range(30):
    tries = 0
    resp_code = 0
    # While response isn't -1, keep trying
    while resp_code != -1:
        # Check if we've hit max tries
        if tries <= backoffs["max_tries"]:
            resp_code = get_releases(249504)
            # If response code is 429, backoff
            if resp_code == 429:
                print(f"Too many requests - Backing off for {backoffs['wait']} seconds")
                sleep(backoffs["wait"])
                # Increase wait time by factor 1.3
                backoffs["wait"] *= backoffs["factor"]
                tries += 1
            
            # Exit while loop if response code is 200
            elif resp_code == 200:
                tries = 0
                resp_code = -1
        # If we did hit max tries, set resp_code to -1 to break while loop
        else:
            print(f"Reached max tries - {tries}")
            resp_code = -1
