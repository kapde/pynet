#!/usr/bin/env python

import json

list=['un','dos','tres',{'primer':'un','segon':'dos'}];
print json.dumps(list);

with open("class1.json", "w") as f:
  json.dump(list,f);
