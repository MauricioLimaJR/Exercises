from sys import argv

scrpit, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CRTL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening tha file..."
target = open(filename, 'w')
print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file." 

text = line1 + "\n" + line2 + "\n" + line3

target.write(text)

print "And finally, we close it."
target.close()