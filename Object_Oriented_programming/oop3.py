class LowercaseMeta(type):
    def __new__(mcs, name, bases, attrs):
        lower_attrs = {}
        for k, v in attrs.items():
            if not k.startswith('__'):
                lower_attrs[k.lower()] = v
            else:
                lower_attrs[k] = v
        return type.__new__(mcs, name, bases, lower_attrs)


class My(metaclass=LowercaseMeta):
    NAME = 'w'

    def HELLO(self):
        print('hello')


my = My()
print(dir(my))