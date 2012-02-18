#!/usr/bin/python
# Tommy Shiou

import sys
import re
import pprint

def clearout(filein, fileout):
  
  fi = open(filein, 'r')
  line = fi.readline()

  fo = open(fileout, "w")
  IPs = []
  count = 0

  while line:
    start = line.find('> ')
    end = line.find(': ', start)
    curr = line[start:end]
    if(curr not in IPs):
      fo.write(curr)
      count += 1
      IPs.insert(0, curr)
    line = fi.readline() 

  fi.close()
  fo.close() 

  print(str(count))

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
