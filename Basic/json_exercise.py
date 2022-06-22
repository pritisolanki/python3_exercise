import json
import pprint

persons = {
    "name": "Priti",
    "age": 21,
    "hobbies": ["walking", "reading"],
    "blackhair": True,
}

print(json.dumps(persons, indent=4))
"""
Output:
{
    "name": "Priti",
    "age": 21,
    "hobbies": [
        "walking",
        "reading"
    ],
    "blackhair": true
}
"""

pprint.pprint(persons, indent=4)
"""
{   'age': 21,
    'blackhair': True,
    'hobbies': ['walking', 'reading'],
    'name': 'Priti'}
"""
