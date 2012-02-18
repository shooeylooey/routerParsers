#!/usr/bin/python
# Tommy Shiou

import sys
import re
import pprint

def clearout(filein):
  
  fi = open(filein, 'r')
  line = fi.readline()

  count = 0
  while line:
    count += int(line)
  
  fi.close()

  print(str(count))

def main():
  args = sys.argv[1:]

  if len(sys.argv) != 2:
    print 'usage: ./parser-2.1.3.py inputfile'
    sys.exit(1)

  infile = sys.argv[1]
  
  clearout(infile)

if __name__== '__main__':
  main()
