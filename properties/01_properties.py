class C(object):
    def __init__(self):
        self._x = None

    @property
    def x(self):
        """I'm the 'x' property."""
        print("Chiama il getter")
        return self._x

    @x.setter
    def x(self, value):
        print("Chiama il setter")
        self._x = value

    @x.deleter
    def x(self):
        print("Chiama il deleter")
        del self._x

nuova = C()
print nuova.x

nuova.x = 'pippo'
print nuova.x