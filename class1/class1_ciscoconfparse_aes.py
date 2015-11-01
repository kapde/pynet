#!/usr/bin/env python

from ciscoconfparse import CiscoConfParse

config = CiscoConfParse("cisco_ipsec.txt");

cmap = config.find_objects_wo_child(parentspec=r"^crypto map CRYPTO", childspec=r"set transform-set AES");

for cm in cmap:
  print cm.text;

for i in range(0,len(cmap)):
  for child in cmap[i].children:
    print child.text;
