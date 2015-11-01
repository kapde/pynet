#!/usr/bin/env python

import yaml

list=['un','dos','tres',{'primer':'un','segon':'dos'}];
print yaml.dump(list, default_flow_style=False);

with file("class1.yml", "w") as f:
  f.write(yaml.dump(list, default_flow_style=False));
