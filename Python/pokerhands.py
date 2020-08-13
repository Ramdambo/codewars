# -*- coding:: utf-8 -*-
from collections import Counter
from random import shuffle, sample
from itertools import chain

from collections import Counter

class PokerHand(object):

    results = ['Tie', 'Win', 'Loss']

    order = '23456789TJQKA'

    def __init__(self, hand):
        self.hand = hand
        self.card_values = [self.order.find(card[0]) for card in hand.split()]
        self.card_colours = [card[1] for card in hand.split()]
        self.count = Counter(self.card_values)

    def is_flush(self):
        return 1 if len(set(self.card_colours)) == 1 else 0

    def is_straight(self):
        vals = sorted(self.card_values)
        if vals == [0, 1, 2, 3, 12]:
            return 1
        for i in range(10):
            if vals == range(i, i + 5):
                return 1
        return 0

    def lowest_straight(self):
        return self.is_straight() and 0 in self.card_values

    def highest_card(self, cardname=False):
        if self.is_straight() and 0 in self.card_values:
            return max([x % 12 for x in self.card_values])
        highcard = max(self.card_values)
        return self.order[highcard] if cardname else highcard

    def is_fullhouse(self):
        return 1 if (len(self.multiples(2)) == 1 and len(self.multiples(3)) == 1) else 0

    def multiples(self, num=2, cardname=False):
        return [self.order[value] if cardname else value for value, count in self.count.iteritems() if count == num]

    def value(self, binval=False):
        value = self.encode(self.card_values, ace_low=self.lowest_straight())                                                # highest cards
        value |= self.encode(self.multiples(2)) << 20                                        # pairs
        value |= self.encode(self.multiples(3)) << 28                                        # 3s
        value |= self.is_straight() << 32                                                    # straight
        value |= self.is_flush() << 33                                                       # flush
        value |= self.is_fullhouse() << 34                                                   # full house
        value |= self.encode(self.multiples(4)) << 35                                        # quads
        value |= (self.is_flush() & self.is_straight()) << 39                                # straight flush
        value |= (self.is_straight() & self.is_flush() & (1 if self.highest_card() == 12 else 0)) << 40  # royal flush
        return '{:#043b}'.format(value) if binval else value

    @staticmethod
    def encode(values, ace_low=False):
        val = 0
        if ace_low:
            s = sorted([x % 12 for x in values])[::-1]
        else:
            s = sorted(values)[::-1]
        for v in s:
            val = (val << 4) | v
        return val

    def __eq__(self, other):
        return self.hand == other.hand

    def __lt__(self, other):
        return self.value() > other.value()

    def __repr__(self):
        return self.hand

if __name__ == '__main__':
    hands = list(map(PokerHand, [ 'KS AS TS QS JS',
                                  '2H 3H 4H 5H 6H',
                                  'AS AD AC AH JD',
                                  'JS JD JC JH 3D',
                                  '2S AH 2H AS AC',
                                  'AS 3S 4S 8S 2S',
                                  '2H 3H 5H 6H 7H',
                                  '2S 3H 4H 5S 6C',
                                  '2D AC 3H 4H 5S',
                                  'AH AC 5H 6H AS',
                                  '2S 2H 4H 5S 4C',
                                  'AH AC 5H 6H 7S',
                                  'AH AC 4H 6H 7S',
                                  '2S AH 4H 5S KC',
                                  '2S 3H 6H 7S 9C']))
    lstCopy = hands[:]
    shuffle(lstCopy)
    userSortedHands = chain(sorted(lstCopy))

    for hand in hands:
        uhand = next(userSortedHands)
        print uhand.value(True), '|\t', uhand, '\t|\t', hand, " ", 1 if uhand == hand else 0

    #
    # pair = PokerHand('KS AS AH 2Q 5C')
    # print pair.value(True)
    # three = PokerHand('KS AS AH AQ 5C')
    # print three.value(True)
    # quad = PokerHand('KS AS AH AQ AC')
    # print quad.value(True)
    #
    # sf = PokerHand('2H 3H 4H 5H 6H')
    # fh = PokerHand('KS AS AH KQ KC')


    # straightformat = '{}H ' * 5
    # abc = 'A23456789TJQKA'
    # colours = 'HSDC'
    #
    # for i in range(10):
    #     hand = straightformat.format(*abc[i:i + 5])
    #     print hand
    #     print PokerHand(hand).is_straight()
