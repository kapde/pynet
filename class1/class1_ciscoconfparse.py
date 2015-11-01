#!/usr/bin/env python

from ciscoconfparse import CiscoConfParse

config = CiscoConfParse("cisco_ipsec.txt");

cmap = config.find_objects(r"^crypto map CRYPTO");

for i in range(0,len(cmap)):
  for child in cmap[i].children:
    print child.text;
