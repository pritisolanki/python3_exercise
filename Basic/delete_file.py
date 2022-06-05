"""
File Deletion - By Priti
    - use remove or unlink(unix) to delete a file
    - user shutils to remove file dir tree
"""
import os
import shutil

try:
    os.remove("test.txt")
except FileNotFoundError as notfounderr:
    print("test.txt not found!")
except BaseException as err:
    print(format(err))
    raise

# shutil.rmtree() deletes a directory and all its contents.
try:
    shutil.rmtree("test")
except FileNotFoundError as notfounderr:
    print(notfounderr)
except BaseException as err:
    print(format(err))
    raise
