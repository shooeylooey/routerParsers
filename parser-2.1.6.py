#!/usr/bin/python
# Tommy Shiou

import sys
import re
import pprint

def countAS(filein, fileout):
  
  fi = open(filein, 'r')
  fo = open('updates-ASu.txt', 'w')
  line = fi.readline()

  count = 0
  ASes = []

  while line:
    start = line.split()
    if start[2] not in ASes:
      fo.write(start[2] + '\n') 
      count += 1
      ASes.insert(0, start[2])
    line = fi.readline()
  
  fi.close()
  fo.close() 

  print str(count)

def main():
  args = sys.argv[1:]

  if len(sys.argv) != 3:
    print 'usage: ./parser.py inputfile outputfile'
    sys.exit(1)

  infile = sys.argv[1]
  outfile = sys.argv[2]
  
  countAS(infile, outfile)

if __name__== '__main__':
  main()
