from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# We could do these two on line too, how?
#in_file = open(from_file)
#indata = in_file.read()
#Maybe:
in_file = open(from_file).read()

#print "The input file is %d bytes long" % len(indata)
print "The input file is %d bytes long" % len(in_file)

print "Does the output file exists? %r" % exists(to_file)

out_file = open(to_file, 'w')
#out_file.write(indata)
out_file.write(in_file)

print "Alright, all done."

out_file.close()
#in_file.close()