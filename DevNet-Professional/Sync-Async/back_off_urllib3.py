from requests.adapters import HTTPAdapter
from requests import Session
import logging
from urllib3.util.retry import Retry

base_url = "https://api.discogs.com/"
# To see all output
logging.basicConfig(level=logging.DEBUG)


def get_releases(release_id):
    endpoint = f"releases/{release_id}"
    # Create session object
    session = Session()
    # Create retry object passing in details about retries and when we want to retry
    retries = Retry(
        total=5, backoff_factor=1, status_forcelist=[429, 500, 502, 503, 504]
    )
    # Call mount method on session object and pass in base_url and HTTPAdapter object wiht retries obj
    session.mount(base_url, HTTPAdapter(max_retries=retries))

    print(f"Getting release {release_id}")

    # Get request
    response = session.get(base_url + endpoint)
    response_code = response.status_code

    return response_code


for i in range(30):
    get_releases(i)
