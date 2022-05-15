from email import header
from email.headerregistry import HeaderRegistry
from urllib.error import HTTPError, URLError
from urllib.request import urlopen, Request

def make_request(url, headers=None, data =None):
    request = Request(url,headers=headers or {},data=data)
    try:
        with urlopen(request, timeout=5) as response:
            print(response.status)
            return response.read(), response
    except HTTPError as error:
        print(error.status, error.reason)
    except URLError as error:
        print(error.reason)
    except TimeoutError:
        print("Request timed out")