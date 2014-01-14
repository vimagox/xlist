l = [1,2,3,4,'x','y','z'] # list
d = {'a':1, 'b':2, 'c':3} # dictionary


#Python Collections
# list
for x in l:
	print x, type(x)
# dictionary
for k in d.keys():
	print k, d[k]

x = True
while(x):
	print 'x'
	x = False


class SimpleClass(object):
	def __init__(self, x, y, z):
		self.x = x
		self.y = y
		self.z = z

	def inc_x(self):
		self.x += 1
		return self.x

	def inc_y(self):
		self.y += 1
		return self.y

simple_class = SimpleClass(1, 2, 3)
print 'x>', simple_class.x
print 'y>', simple_class.y
print 'inc_x>', simple_class.inc_x()
print 'inc_y>', simple_class.inc_y()



