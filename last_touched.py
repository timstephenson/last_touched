#!/usr/bin/env python

import sys, os.path, time
from datetime import datetime
from operator import itemgetter

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