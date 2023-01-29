import requests

base_url = "http://httpbin.org/"


def get_delay(seconds):
    # Hit delay endpoint with seconds delayed reponse
    endpoint = f"delay/{seconds}"

    print(f"Getting with {seconds} seconds delay")
    # GET request
    response = requests.get(base_url + endpoint)
    data = response.json()
    print(data)


# Call get_delay with 5 seconds delay
get_delay(5)

print("Done")
