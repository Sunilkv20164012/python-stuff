import requests
import json

url = 'localhost:7601/coupons/tag/recon/schedules?isManual=true'

def getHeaders():
    headers = {
    'content-type': 'application/json',
    'x-mynt-ctx: storeid=2297;'
    }
    return header

def singlePostCall(url, payload):
    r = requests.post(url, data=json.dumps(payload), headers=getHeaders())
    # print(r.content)
    return r.content

def singleGetCall():
    r = requests.get(url, data=json.dumps(payload), headers=getHeaders())
    # print(r.content)
    return r.content



async def threadPool(url, threadCount):
    with concurrent.futures.ThreadPoolExecutor(max_workers=threadCount) as executor:

        loop = asyncio.get_event_loop()
        futures = [
            loop.run_in_executor(
                executor, 
                requests.get, 
                'http://example.org/'
            )
            for i in range(threadCount)
        ]
        for response in await asyncio.gather(*futures):
            print response
            pass


loop = asyncio.get_event_loop()
loop.run_until_complete(threadPool())


