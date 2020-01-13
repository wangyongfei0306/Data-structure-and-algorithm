import functools
import re
import sys
from collections import defaultdict


class Card:
    insure = False

    def __init__(self, rank, suit, hard, soft):
        self.rank = rank
        self.suit = suit
        self.hard = hard
        self.soft = soft

    def __repr__(self):
        return "{__class__.__name__}(suit={suit!r}, rank={rank!r})".format(
            __class__=self.__class__, **self.__dict__
        )

    def __str__(self):
        return "{rank}{suit}".format(**self.__dict__)

    def __bytes__(self):
        class_code = self.__class__.__name__[0]
        rank_number_str = {'A':'1', 'J':'11', 'Q':'12', 'K':'13'}.get(self.rank, self.rank)
        string = '(' + ' '.join([class_code, rank_number_str, self.suit,]) + ')'
        return bytes(string, encoding='utf8')


class NumberCard(Card):
    def __init__(self, rank, suit):
        super().__init__(str(rank), suit, rank, rank)


class AceCard(Card):
    def __init__(self, rank, suit):
        super().__init__(rank, suit, 1, 11)


class FaceCard(Card):
    def __init__(self, rank, suit):
        super().__init__({11:'J', 12:'Q', 13:'K'}[rank], suit, 10, 10)


class Card2:
    insure = False

    def __init__(self, rank, suit, hard, soft):
        self.rank = rank
        self.suit = suit
        self.hard = hard
        self.soft = soft

    def __repr__(self):
        return "{__class__.__name__}(suit={suit!r}, rank={rank!r})".format(
            __class__=self.__class__, **self.__dict__
        )

    def __str__(self):
        return "{rank}{suit}".format(**self.__dict__)

    def __eq__(self, other):
        return self.suit == other.suit and self.rank == other.rank

    def __hash__(self):
        return hash(self.suit) ^ hash(self.rank)


class AceCard2(Card2):
    def __init__(self, rank, suit):
        super().__init__(rank, suit, 1, 11)


class Card3:
    insure = False

    def __init__(self, rank, suit, hard, soft):
        self.rank = rank
        self.suit = suit
        self.hard = hard
        self.soft = soft

    def __repr__(self):
        return "{__class__.__name__}(suit={suit!r}, rank={rank!r})".format(
            __class__=self.__class__, **self.__dict__
        )

    def __str__(self):
        return "{rank}{suit}".format(**self.__dict__)

    def __eq__(self, other):
        return self.suit == other.suit and self.rank == other.rank

    __hash__ = None


class AceCard3(Card3):
    insure = True
    def __init__(self, rank, suit):
        super().__init__(rank, suit, 1, 11)


class Hand:
    def __init__(self, dealer_card, *cards):
        self.dealer_card = dealer_card
        self.cards = list(cards)

    def __str__(self):
        return ','.join(map(str, self.cards))

    def __repr__(self):
        return "{__class__.__name__}({dealer_card!r}, {_cards_str})".format(
            ___class__=self.__class__, __cards_str=",".join(map(str, self.cards)),
            **self.__dict__
        )

    def __eq__(self, other):
        return self.cards == other.cards and self.dealer_card == other.dealer_card

    __hash__ = None


class FrozenHand(Hand):
    def __init__(self, *args, **kwargs):
        if len(args) == 1 and isinstance(args[0], Hand):
            other = args[0]
            self.dealer_card = other.dealer_card
            self.cards = other.cards
        else:
            super().__init__(*args, **kwargs)

    def __hash__(self):
        h = 0
        for c in self.cards:
            h = (h + hash(c)) % sys.hash_info.modulus
        return h


def card_from_bytes(buffer):
    string = buffer.decode('utf8')
    assert string[0] == '(' and string[-1] == ')'
    code, rank_number, suit = string[1:-1].split()
    class_ = {'A':AceCard, 'N':NumberCard, 'F':FaceCard}[code]
    return class_(int(rank_number), suit)


class BlackJackCard_p:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __lt__(self, other):
        print('Compare {0} < {1}'.format(self, other))
        return self.rank < other.rank

    def __eq__(self, other):
        print('Compare {0} == {1}'.format(self, other))
        return self.rank == other.rank

    def __str__(self):
        return '{rank}{suit}'.format(**self.__dict__)


class BlackJackCard:
    def __init__(self, rank, suit, hard, soft):
        self.rank = rank
        self.suit = suit
        self.hard = hard
        self.soft = soft

    def __lt__(self, other):
        if not isinstance(other, BlackJackCard):
            return NotImplemented
        return self.rank < other.rank

    def __le__(self, other):
        try:
            return self.rank <= other.rank
        except AttributeError:
            return NotImplemented

    def __gt__(self, other):
        if not isinstance(other, BlackJackCard):
            return NotImplemented
        return self.rank > other.rank

    def __ge__(self, other):
        if not isinstance(other, BlackJackCard):
            return NotImplemented
        return self.rank >= other.rank

    def __eq__(self, other):
        if not isinstance(other, BlackJackCard):
            return NotImplemented
        return self.rank == other.rank and self.suit == other.suit

    def __ne__(self, other):
        if not isinstance(other, BlackJackCard):
            return NotImplemented   
        return self.rank != other.rank and self.suit != other.suit

    def __str__(self):
        return '{rank}{suit}'.format(**self.__dict__)


if __name__ == '__main__':
    # two = BlackJackCard_p(2, '黑桃')
    # three = BlackJackCard_p(3, '黑桃')
    # print(two==three)
    s = '  -8329f2h38 f72hf'
    print(*re.findall('^[\+\-]?\d+', s.lstrip()))


    pass
