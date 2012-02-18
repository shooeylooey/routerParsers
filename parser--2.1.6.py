#!/usr/bin/python
# Tommy Shiou

import sys
import re
import pprint

def clearout(filein, fileout):
  
  fi = open(filein, 'r')
  line = fi.readline()

  fo = open(fileout, "w")
  num = 0
  ASes = []

  while line:
    ###line = str(line)
    start = line.index("AS")
    if line[start:] not in ASes:
      ASes.insert(0,line[start:])
      fo.write(line[start:])
      num += 1
    line = fi.readline
 
  fi.close()
  fo.close() 

  print(str(num))

def main():
  args = sys.argv[1:]

  if len(sys.argv) != 3:
    print 'usage: ./parser-2.1.3.py inputfile outputfile'
    sys.exit(1)

  infile = sys.argv[1]
  outfile = sys.argv[2]
  
  clearout(infile, outfile)

if __name__== '__main__':
  main()
