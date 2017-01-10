#!/usr/bin/env python

import json
import sys

in_file = sys.argv[1]
out_file = sys.argv[2]

with open(in_file) as f:
    in_dict = json.load(f)

out_dict = {'product': in_dict['x1'] * in_dict['x2']}

with open(out_file, 'w') as f:
    json.dump(out_dict, f)
