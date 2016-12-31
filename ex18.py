# this one is like the scripts with argv
def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# Or, just do this
def print_two_again(arg1, arg2):
	print "arg1: %r, arg2: %r" % (arg1, arg2)

#With just one argument
def print_one(arg1):
	print "arg1: %r" % arg1

#With no one argument
def print_none():
	print "I go nothin'."

print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()