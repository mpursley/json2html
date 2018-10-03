import os, sys

lib_path = os.path.abspath(os.path.join('..'))
sys.path.append(lib_path)

from json2html import *

_texttable_example1 = """
 _________________________________________________
| name        | name test                         |
| desription  | converts json 2 text table format |
| test3       | test3 test                        |
| test4       | | test4a | test4b |               |
| test5       | | test5a | test5b |               |
 -------------------------------------------------
"""

_texttable_example2 = """
 ___________________________
|               |   |   |   |
|               | a | c | b |
|   sampleData  |---|---|---|
|               | 1 | 3 | 2 |
|               | 5 | 7 | 6 |
 ---------------------------
"""


_json_example1 = {
    "name": "name test",
    "desription": "converts json 2 text table format",
    "test3": "test3 test",
    "test4": { "test4a": "test4b"},
    "test5": { "test5a": "test5b"},
}

_json_example2 = {
  "sampleData": [
    {
      "a1": "aa1",
      "b1": "bb1",
      "c1": "cc1"
    },
    {
      "a2": "aa2",
      "b2": "bb2",
      "c2": "cc2"
    }
  ]
}


print("\nexample1: text table output")
print(_texttable_example1)

output = json2html.convert(json = _json_example1)
print("\nexample1: html output: \n")
print(output)

output = json2texttable.convert(json = _json_example1)
print("\nexample1: text output: \n")
print(output)

print("\nexample2: text table output:")
output = json2html.convert(json = _json_example2)

print(_texttable_example2)
print(output)

output = json2texttable.convert(json = _json_example2)
print("\nexample2: text output: \n")
print(output)

output = json2html.convert(json = _json_example2)
print("\nexample2: html output: \n")
print(output)

print("\n")
