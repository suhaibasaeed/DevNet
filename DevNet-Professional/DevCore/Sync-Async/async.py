import asyncio
from aiohttp import ClientSession

base_url = "http://httpbin.org/"


# Count to 5 and call .sleep() for 1 second each time
async def count():
    for i in range(1, 9):
        print(i)
        # Go do something else for 1 second
        await asyncio.sleep(1)


# Same function as get_delay() in sync.py
async def get_delay(seconds):
    # Hit delay endpoint with seconds delayed reponse
    endpoint = f"delay/{seconds}"

    print(f"Getting with {seconds} seconds delay")

    # Context manager used to isntead instance of ClientSession
    async with ClientSession() as session:
        # Execute GET request on session object
        async with session.get(base_url + endpoint) as response:
            # While waiting for response, go do something else
            response = await response.json()
            print(response)


# Pass in both async functions and run asynchronously
async def main():
    await asyncio.gather(get_delay(5), count())


asyncio.run(main())

print("Done")
