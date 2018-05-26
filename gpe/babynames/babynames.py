  #!/usr/bin/python
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

import sys
import re

"""Baby Names exercise

Define the extract_names() function below and change main()
to call it.

For writing regex, it's nice to include a copy of the target
text for inspiration.

Here's what the html looks like in the baby.html files:
...
<h3 align="center">Popularity in 1990</h3>
....
<tr align="right"><td>1</td><td>Michael</td><td>Jessica</td>
<tr align="right"><td>2</td><td>Christopher</td><td>Ashley</td>
<tr align="right"><td>3</td><td>Matthew</td><td>Brittany</td>
...

Suggested milestones for incremental development:
 -Extract the year and print it
 -Extract the names and rank numbers and just print them
 -Get the names data into a dict and print it
 -Build the [year, 'name rank', ... ] list and print it
 -Fix main() to use the extract_names list
"""

def extract_names(filename):
  """
  Given a file name for baby.html, returns a list starting with the year string
  followed by the name-rank strings in alphabetical order.
  ['2006', 'Aaliyah 91', Aaron 57', 'Abagail 895', ' ...]
  """
  # +++your code here+++
  list = []
  map = {}
  in_file = open(filename, 'r')
  year = ''
  for line in in_file:
    yearmatch = re.search(r'<h3 align="center">Popularity\sin\s(\d\d\d\d)', line)
    if yearmatch:
      year = yearmatch.group(1)
    babymatch = re.search(r'<tr align="right"><td>(\d+)</td><td>(\w+)</td><td>(\w+)</td>', line)
    if babymatch:
      count = babymatch.group(1)
      name1 = babymatch.group(2)
      name2 = babymatch.group(3)
      map[name1] = map[name2] = count
  in_file.close()
  for key in sorted(map.keys()):
    list.append(key + ' ' + map[key])
  return year, list


def main():
  # This command-line parsing code is provided.
  # Make a list of command line arguments, omitting the [0] element
  # which is the script itself.
  args = sys.argv[1:]

  if not args:
    print 'usage: [--summaryfile] file [file ...]'
    sys.exit(1)

  # Notice the summary flag and remove it from args if it is present.
  summary = False
  if args[0] == '--summaryfile':
    summary = True
    del args[0]
  if len(args)==0:
    print 'No filenames supplied in the input. Please check and rerun.'
    sys.exit(1)

  # +++your code here+++
  # For each filename, get the names, then either print the text output
  # or write it to a summary file
  for filename in args:
    year, list = extract_names(filename)
    if len(list)<1:
      print 'File has no baby names'
      continue
    if summary:
      f = open(filename[:filename.index('.')] + '-summary.txt', 'w')
      f.write('Summary\n')
      f.write('\nYear : ' + year)
      f.write('\nName\t\t Count')
      f.write('\n----\t\t------\n')
      for i in range(0, len(list), 2):
        f.write(list[i][:list[i].index(' ')] + '\t\t' + list[i][list[i].index(' ')+1] + '\n')
      f.close()
    else:
      print 'Year : ' + year
      print 'Name\t\t Count'
      print '----\t\t------'
      for i in range(0, len(list)):
        print list[i][:list[i].index(' ')] + '\t\t' + list[i][list[i].index(' ')+1]
  
if __name__ == '__main__':
  main()
