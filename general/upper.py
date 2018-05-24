class Upper(object):
    def __init__(self, iterable):
        self._iter = iter(iterable)
    def next(self):                 # Py2-style iterator interface
        return next(self._iter).upper()
    def __iter__(self):
        return self

itr = Upper('hello')
print itr.next(),
for letter in itr:
    print letter,  
         
