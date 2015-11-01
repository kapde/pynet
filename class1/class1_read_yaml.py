#!/usr/bin/env python

import yaml


with file("class1.yml") as f:
  list=yaml.load(f);

print list;
