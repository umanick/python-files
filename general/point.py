class Point(object):
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __str__(self):
        return 'Point({self.x}, {self.y})'.format(self=self)


subject = 'Upen'

class Sentence(object):
    def __init__(self, subject, verb, object):
        self.subject, self.verb, self.object = subject, verb, object
    def __str__(self):
        return '{self.subject} {self.verb} {self.object}'.format(self=self)
    def printglobal(self):
        print subject + ' ' + self.verb + ' ' + self.object

p = Point(4, 2)
print str(p)

s = Sentence('He', 'likes', 'books')
print str(s)
s.printglobal()