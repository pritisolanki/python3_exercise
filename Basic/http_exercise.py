from tkinter import EXCEPTION
from urllib.request import urlopen

try:
    with urlopen("https://www.google.com/") as response:
        content = response.read()
        character_set = response.headers.get_content_charset()
        content = content.decode(character_set)
except Exception as ex:
    print(ex)
finally:
    if response is not None:
        response.close()

with open("google.html", encoding="utf-8", mode="w") as file:
        file.write(content)