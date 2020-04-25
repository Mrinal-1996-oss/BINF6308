#!/usr/bin/env python
# regex.py
# Import re for regular expressions
import re
chromosome = "2L"
regex = "^\d{1,1}\D*$"
if re.match(regex, chromosome):
   print(chromosome)
