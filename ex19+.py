def get_media(number1, number2):
	half_number = ( number1  + number2 ) / 2
	print "the half value bewten %d and %d is:" % (number1, number2)
	print half_number
	return half_number

print "Way 1"
get_media(8, 4)

print "Way 2"
num1 = 44
num2 = 56
get_media(num1, num2)

print "Way 3"
num3 = 20
num4 = 22
get_media(num3 + 6, num4 *2)

print "Way 4"
get_media(3*6, 60 / 4)

print "Way 5"
num5 = get_media(10 , 20)
num6 = get_media(num5, 4)

print "Way 6"
num7 = len('number')
num8 = len('other number')
get_media(num7, num8)

print "Way 7"
get_media(len('Other'), len('way'))

print "Way 8"
num9 = raw_input('type one number')
num10 = raw_input('type other number')
get_media(int(num9), int(num10))

print "Way 9"
vet1 = [5, 2, 6]
vet2 = [9, 25, 64]
get_media(vet1[1]*4, vet2[2])

print "Way 10"
num11 = 1
num12 = 1
while num11 < 40:
	num11 += 2
	num11 *= num11
if num11 % 2 == 0:
	num12 = num11 / 2
else:
	num12 = num11 * 2
get_media(num11, num12)