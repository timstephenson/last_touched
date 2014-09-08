#!/usr/bin/env python

import sys, os.path, time
from datetime import datetime
from operator import itemgetter

"""
  This script takes a list of file names as arguments. It assumes that
  spaces for files have been escaped. If one of the paths does not point to a file,
  a message is printed to let you know what happened. The same is true if the file
  can not be found.

  If the spaces are not escaped, it will report that two files couldn't be found.
  The script does not attempt to handle anything that is not a file.

  This implementation will not provide as much error information if the path does
  not lead to a file. If it is not a file it ignores it and moves to the next item
  in the list.
"""

class LastTouched:

  def __init__(self, paths):
    self.fileStats = []
    self.sortedStats = []
    self.loadFileStats(paths)

  def loadFileStats(self, paths):
    for path in paths:
      if os.path.isfile(path):
        self.fileStats.append({ 'name': path,  'last_accessed': os.path.getatime( path ) })
      else:
        print "-> Sorry '%s' was not a file." % path

  def sortStats(self):
    if len(self.fileStats) > 0:
      self.sortedStats = sorted(self.fileStats, key=itemgetter('last_accessed'), reverse = True)

  def printLastTouched(self):
    self.sortStats()
    if len(self.sortedStats) > 0:
      print "%s" % self.sortedStats[0]['name']
    else:
      print "-> Sorry, no file stats available."

# Test class if running directly.
if __name__ == '__main__':
  touched = LastTouched(sys.argv[1:])
  touched.printLastTouched()