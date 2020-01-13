class Hand:
    def __str__(self):
        return ', '.join(map(str, self.card))

    def __repr__(self):
        return '{__class__.__name__} ({dealer_card!r}, {_cards_str})'.format(
            ___class__=self.__class__, __cards_str=', '.join(map(repr, self.card)),
            **self.__dict__)


class Hand_Lazy(Hand):
    def __init__(self, dealer_card, *cards):
        self.dealer_card = dealer_card
        self._cards = list(cards)

    @property
    def total(self):
        delta_soft = max(c.soft-c.hard for c in self._cards)
        hard_total = sum(c.hard for c in self._cards)
        if hard_total + delta_soft <= 21:
            return hard_total + delta_soft
        return hard_total

    @property
    def card(self):
        return self._cards

    @card.setter
    def card(self, aCard):
        self._cards.append(aCard)

    @card.deleter
    def card(self):
        self._cards.pop(-1)


class UnitValue_1:
    def __init__(self, unit):
        self.value = None
        self.unit = unit
        self.default_format = '5.2f'

    def __set__(self, instance, value):
        self.value = value

    def __str__(self):
        return "{value:{spec}} {unit}".format(spec=self.default_format, **self.__dict__)

    def __format__(self, spec='5.2f'):
        if spec == '':
            spec = self.default_format
        return '{value:{spec}} {unit}'.format(spec=spec, **self.__dict__)


class RTD_1:
    rate = UnitValue_1('kt')
    time = UnitValue_1('hr')
    distance = UnitValue_1('nm')

    def __init__(self, rate=None, time=None, distance=None):
        if rate is None:
            self.time = time
            self.distance = distance
            self.rate = distance / time
        if time is None:
            self.rate = rate
            self.distance = distance
            self.time = distance / rate
        if distance is None:
            self.rate = rate
            self.time = time
            self.distance = rate * time

    def __str__(self):
        return 'rate: {0.rate} time: {0.time} distance: {0.distance}'.format(self)


class Unit:
    conversion = 1.0

    def __get__(self, instance, owner):
        return instance.kph * self.conversion

    def __set__(self, instance, value):
        instance.kph = value / self.conversion


class Knots(Unit):
    conversion = 0.5399568


class MPH(Unit):
    conversion = 0.62137119


class KPH(Unit):
    def __get__(self, instance, owner):
        return instance._kph

    def __set__(self, instance, value):
        instance._kph = value


class Measurement:
    kph = KPH()
    knots = Knots()
    mph = MPH()

    def __init__(self, kph=None, mph=None, knots=None):
        if kph:
            self.kph = kph
        elif mph:
            self.mph = mph
        elif knots:
            self.knots = knots
        else:
            raise TypeError

    def __str__(self):
        return 'rate: {0.kph} kph = {0.mph} mph = {0.knots} knots'.format(self)