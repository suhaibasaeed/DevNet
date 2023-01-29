import requests

"""
Example of being rate limited by the API - 429 response code
"""

base_url = "https://api.discogs.com/"

def get_release(release_id):
    # Hit delay endpoint with seconds delayed reponse
    endpoint = f"releases/{release_id}"

    print(f"Getting release {release_id}")
    # GET request
    response = requests.get(base_url + endpoint)
    data = response.json()
    print(response)

for i in range(30):
    get_release(i)