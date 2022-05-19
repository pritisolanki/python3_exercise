# read the URL and create the html file along with error handling - By Priti
from urllib.request import urlopen
from urllib.error import HTTPError, URLError

try:
    with urlopen('https://www.google.com/') as response:
        content = response.read()
        character_set = response.headers.get_content_charset()
        content = content.decode(character_set)
        with open("google.html", encoding="utf-8", mode="w") as file:
            file.write(content)    
except HTTPError as error:
    print(error.status,error.reason)
except URLError as error:
    print(error.reason)
except NameError as error:
    print(error)
except Exception as ex:
    print(ex)