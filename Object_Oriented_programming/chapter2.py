import collections
import weakref


class Noisy:
    def __del__(self):
        print('Removing {0}'.format(id(self)))


class Parent:
    def __init__(self, *children):
        self.children = list(children)
        for child in self.children:
            child.parent = self

    def __del__(self):
        print('Removing {__class__.__name__} {id:d}'.format(
            __class__=self.__class__, id=id(self)))


class Parent2:
    def __init__(self, *children):
        self.children = list(children)
        for child in self.children:
            child.parent = weakref.ref(self)

    def __del__(self):
        print('Removing {__class__.__name__} {id:d}'.format(
            __class__=self.__class__, id=id(self)))


class Child:
    def __del__(self):
        print('Removing {__class__.__name__} {id:d}'.format(
            __class__=self.__class__, id=id(self)))


class Float_Fail(float):
    def __init__(self, value, unit):
        super().__init__(value)
        self.unit = unit


class Float_Units(float):
    def __new__(cls, value, unit):
        obj = super().__new__(cls, value)
        obj.unit = unit
        return obj


class Ordered_Attributes(type):
    @classmethod
    def __prepare__(mcs, name, bases, **kwds):
        return collections.OrderedDict()

    def __new__(cls, name, bases, namespace, **kwds):
        result = super().__new__(cls, name, bases, namespace)
        result._order = tuple(n for n in namespace if not n.startswith('__'))
        return result


class Order_Preserved(metaclass=Ordered_Attributes):
    pass


class Something(Order_Preserved):
    this = 'text'

    def z(self):
        return False
    b = 'order is preserved'
    a = 'more text'


if __name__ == '__main__':
    # s2 = Float_Fail(6.5, 'knots')
    # speed = Float_Units(6.5, 'knots')
    # print(speed)

    # Useless = type('Useless', (), {})
    # print(Useless)

    o = Ordered_Attributes('n', (), {})
    print(o)

    pass