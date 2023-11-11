import requests, logging, json

page = 1
pageCount = 1
per_page = 5
baseUrl = "https://api.discogs.com/artists/1/releases"

# Loop through the pages of results
while page <= pageCount:
    # Fetch a page of results
    querystring = {"page": page, "per_page": per_page}
    req = requests.get(baseUrl, params=querystring)

    # Load the JSON string into a Python dictionary
    results = json.loads(req.text)

    releases = json.dumps(results["releases"], indent=3)
    pagination = results["pagination"]
    # Update the pageCount based on the results
    pageCount = int(pagination["pages"])

    # Print the first query releases
    print(releases)

    # Ask the user if they want to continue to next page
    if page < pageCount:
        input(f"Page: {page} of {pageCount}. Press any key to continue...")
    else:
        input("End of results.")

    page += 1
