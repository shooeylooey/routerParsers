#!/usr/bin/python
# Tommy Shiou

import sys
import re
import pprint

def findshortest(infile, start, dest):
  fi = open(infile, 'r')
  lines = fi.read()  

  curr1 = start
  curr2 = dest
  connected = False
  pool1 = [start]
  pool2 = [dest]

  while not connected:
    for line in lines:
      if line[0] == '#':
        break
      relationship = line.split()
      if int(relationship[0]) == curr1:
        if int(relationship[2]) <= 0:
          pool1.append(int(relationship[1]))
      if int(relationship[0]) == curr2:
        if int(relationship[2]) <= 0:
          pool2.append(int(relationship[1]))
    for AS in pool1:
      if pool2.find(AS) > -1:
        connected = True
        print(str(AS) + str(pool2[pool2.find(AS)]))
      else:

    

  fi.close()

def main():
  args = sys.argv[1:]

  if len(sys.argv) != 4:
    print 'usage: ./parser.py originAS destinationAS inputfile'
    sys.exit(1)

  origin = sys.argv[1]
  dest = sys.argv[2]
  infile = sys.argv[3]

  findshortest(infile, origin, dest)

if __name__== '__main__':
  main()
