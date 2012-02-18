#!/usr/bin/python
# Tommy Shiou

import sys
import re
import pprint

def makeAStable(filein, fileout):

  AS_map = {}
  AS_list = []

  fi = open(filein, 'r')
  fo = open('ASTable.txt', "w")

  line = fi.readline()
  while line:
    addresses = line[8:].split()
    for i in range(len(addresses) - 1):
      if addresses[i] == addresses[i+1]:
        continue
      if addresses[i] in AS_map and AS_map[addresses[i]].count(addresses[i+1]) != 0:
        continue
      else:
        if addresses[i] not in AS_map:
          AS_map[addresses[i]] = [addresses[i+1]]
	  try:
            AS_list.append(int(addresses[i]))
          except ValueError:
            continue
        else:
          AS_map[addresses[i]].append(addresses[i+1])
    line = fi.readline()

  AS_list.sort()

  for AS in AS_list:
    fo.write(str(AS) + "[" + ",".join(AS_map[str(AS)]) + "]\n")

  fo.close()
  fo = open(fileout, "w")
  count = 0
  num = 0
  for AS in AS_list:
    num = len(AS_map[str(AS)])
    count = count + num
    fo.write(str(num) + "\n")

  fi.close()
  fo.close()

def main():
  args = sys.argv[1:]

  if len(sys.argv) != 3:
    print 'usage: ./parser.py inputfile outputfile'
    sys.exit(1)

  infile = sys.argv[1]
  outfile = sys.argv[2]
  
  ###clearout(infile, outfile)

  makeAStable(infile, outfile)
if __name__== '__main__':
  main()
