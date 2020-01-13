class Programmer:
    def __init__(self, name, age):
        self.name = name
        if isinstance(age, int):
            self.age = age
        else:
            raise Exception('age must be int')

    def __eq__(self, other):
        if isinstance(other, Programmer):
            return True if self.age == other.age else False
        else:
            raise Exception('The type of object must be Programmer')

    def __add__(self, other):
        if isinstance(other, Programmer):
            return self.age + other.age
        else:
            raise Exception('The type of object must be Programmer')

    def __str__(self):
        return '{} is {} years old'.format(self.name, self.age)

    def __dir__(self):
        return self.__dict__.keys()

    def __setattr__(self, key, value):
        self.__dict__[key] = value

    def __getattribute__(self, item):
        return super(Programmer, self).__getattribute__(item)

    def __delattr__(self, item):
        pass


if __name__ == '__main__':
    p1 = Programmer('wang', 21)
    p2 = Programmer('xi', 18)
    # print(p1 == p2)
    # print(p1 + p2)
    # print(p1)
    # print(dir(p1))
    print(p1.name)