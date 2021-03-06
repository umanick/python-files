#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

"""Wordcount exercise
Google's Python class

The main() below is already defined and complete. It calls print_words()
and print_top() functions which you write.

1. For the --count flag, implement a print_words(filename) function that counts
how often each word appears in the text and prints:
word1 count1
word2 count2
...

Print the above list in order sorted by word (python will sort punctuation to
come before letters -- that's fine). Store all the words as lowercase,
so 'The' and 'the' count as the same word.

2. For the --topcount flag, implement a print_top(filename) which is similar
to print_words() but which prints just the top 20 most common words sorted
so the most common word is first, then the next most common, and so on.

Use str.split() (no arguments) to split on all whitespace.

Workflow: don't build the whole program at once. Get it to an intermediate
milestone and print your data structure and sys.exit(0).
When that's working, try for the next milestone.

Optional: define a helper function to avoid code duplication inside
print_words() and print_top().

"""

import sys

# +++your code here+++
# Define print_words(filename) and print_top(filename) functions.
# You could write a helper utility function that reads a file
# and builds and returns a word/count dict for it.
# Then print_words() and print_top() can just call the utility function.

###

# This basic command line argument parsing code is provided and
# calls the print_words() and print_top() functions which you must define.
def main():
  if len(sys.argv) != 3:
    print 'usage: ./wordcount.py {--count | --topcount} file'
    sys.exit(1)

  option = sys.argv[1]
  filename = sys.argv[2]
  if option == '--count':
    print_words(filename)
  elif option == '--topcount':
    print_top(filename)
  else:
    print 'unknown option: ' + option
    sys.exit(1)

def get_map(filename):
  in_file = open(filename)
  indata = in_file.read()
  map = {}
  for string in indata.split():
    string = strip_string(string.lower())
    if string in map:
      map[string] = map[string] + 1
    else:
      map[string] = 1
  in_file.close()   
  return map

#This method will string the trailing and leading non-alpha numeric characters
#If the string contains all non-alphanumerics, it will return the string as is.
def strip_string(string):
  front = False
  index = 0
  right = left = 0
  for c in string:
      if c.isalnum():
          right = index
          if not front:
              left = index
              front = True
      index += 1
  if front:
    return string[left:right+1]
  else:
    return string

def print_words(filename):
  map = get_map(filename)
  for key in sorted(map.keys()):
    print key + ' - ' + str(map[key])
  return

def get_count(tuple):
  return tuple[1]

def print_top(filename):
  map = get_map(filename)
  map = sorted(map.items(), key=get_count, reverse=True)
  for item in map[:20]:
    print item[0] + ' - %d' % item[1]
  return

if __name__ == '__main__':
  main()