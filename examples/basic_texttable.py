import os, sys

lib_path = os.path.abspath(os.path.join('..'))
sys.path.append(lib_path)

from json2html import *

_texttable = """
 _________________________________________________
| name        | name test                         |
| desription  | converts json 2 text table format |
| test3       | test3 test                        |
| test4       | | test4a | test4b |               |
 -------------------------------------------------
"""

_texttable = """
 ___________________________
|               |   |   |   |
|               | a | c | b |
|   sampleData  |---|---|---|
|               | 1 | 3 | 2 |
|               | 5 | 7 | 6 |
 ---------------------------
"""


_json = {
    "name": "name test",
    "desription": "converts json 2 text table format",
    "test3": "test3 test",
    "test4": { "test4a": "test4b"}
}

_json = {
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


print("\ntext table output: \n")
print(_texttable)

output = json2texttable.convert(json = _json)
print("\nhtml output: \n")
print(output)
print("\n")
