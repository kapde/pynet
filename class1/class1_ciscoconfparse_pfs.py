#!/usr/bin/env python

from ciscoconfparse import CiscoConfParse

config = CiscoConfParse("cisco_ipsec.txt");

cmap = config.find_objects_w_child(parentspec=r"^crypto map CRYPTO", childspec=r"set pfs group2");

for cm in cmap:
  print cm.text;

for i in range(0,len(cmap)):
  for child in cmap[i].children:
    print child.text;
