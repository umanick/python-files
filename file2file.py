from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)


# We could do these two on one line too, how?
in_file = open(from_file); indata = in_file.read()

print "The input file is %d long" % len(indata)

print "Does the output file exists? %r" % exists(to_file)
print "Ready, hit ENTER to continue, CTRL-C to abort"
raw_input()

out_file = open(to_file, "w")
out_file.write(indata)

print "All done"

out_file.close()
in_file.close()
