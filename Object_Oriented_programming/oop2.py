class Programmer:
    wang = 'WANG'

    def __init__(self, name, age, weight):
        self.name = name
        self._age = age
        self.__weight = weight

    @classmethod
    def get_wang(cls):
        return cls.wang

    @property
    def get_weight(self):
        return self.__weight

    def self_introduction(self):
        print('My name is {} an {} years old'.format(self.name, self._age))


class BackedProgrammer(Programmer):
    def __init__(self, name, age, weight, language):
        super(BackedProgrammer, self).__init__(name, age, weight)
        self.language = language

    def self_introduction(self):
        print('My name is {} My favorite language is {}'.format(self.name, self.language))


def introduce(programmer):
    if isinstance(programmer, Programmer):
        programmer.self_introduction()


if __name__ == '__main__':
    programmer = Programmer('xi', 20, 90)
    backed_programmer = BackedProgrammer('Guo', 21, 100, 'python')
    introduce(programmer)
    introduce(backed_programmer)