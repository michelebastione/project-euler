from itertools import combinations


class Card():
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
        self.order = '23456789TJQKA'

    def __lt__(self, other):
        return self.order.index(self.value) < self.order.index(other.value)

    def __gt__(self, other):
        return self.order.index(self.value) > self.order.index(other.value)


class Hand():
    def __init__(self, cards):
        self.cards = cards
        self.order = '23456789TJQKA'
        self.hc = max(self.cards)

    def highest_card(self):
        self.bck = sorted([i for i in self.cards if i != max(self.cards)], reverse=True)
        self.hc=max(self.cards)
        return self.hc

    def is_same_value(self, l):
        self.hc = max(l)
        self.bck = sorted([i for i in self.cards if i not in l], reverse=True)
        return all(i.value == l[0].value for i in l)

    def one_pair(self):
        if any(self.is_same_value(y) for y in [x for x in combinations(self.cards, 2)]):
            return True
        return False

    def two_pairs(self):
        for i in combinations(self.cards, 2):
            temp = self.cards.copy()
            if self.is_same_value(i):
                hct = self.hc
                temp.remove(i[0])
                temp.remove(i[1])
                if any(self.is_same_value(j) for j in combinations(temp, 2)):
                    temp.remove(self.hc)
                    for i in temp:
                        if i.value == self.hc.value:
                            temp.remove(i)
                    self.hc = max(self.hc, hct)
                    self.bck = [min(self.hc, hct)] + temp
##                    print(self.bck[0].value, self.bck[1].value)
                    return True
        return False

    def three_kind(self):
        if any(self.is_same_value(y) for y in [x for x in combinations(self.cards, 3)]):
            return True
        return False

    def straight(self):
        if any(sorted([i.value for i in self.cards]) == list(self.order[j:j + 5]) for j in range(8)):
            self.hc = self.highest_card()
            return True
        return False

    def flush(self):
        if all(c.suit == self.cards[0].suit for c in self.cards[1:]):
            self.hc = self.highest_card()
            return True
        return False

    def full_house(self):
        for i in combinations(self.cards, 3):
            temp = self.cards.copy()
            if self.is_same_value(i):
                temp.remove(i[0])
                temp.remove(i[1])
                temp.remove(i[2])
            if self.is_same_value(temp):
                self.hc = i[0]
                return True
        return False

    def four_kind(self):
        if any(self.is_same_value(y) for y in [x for x in combinations(self.cards, 4)]):
            return True
        return False

    def straight_flush(self):
        if self.flush():
            if self.straight():
                return True
        return False

    def royal_flush(self):
        if self.flush():
            if all(i in [j.value for j in self.cards] for i in self.order[8:]):
                return True
        return False

    def best(self):
        check = {self.royal_flush: 10, self.straight_flush: 9, self.four_kind: 8, self.full_house: 7, self.flush: 6,
                 self.straight: 5, self.three_kind: 4, self.two_pairs: 3, self.one_pair: 2, self.highest_card: 1}
        for i in check:
            if i():
                return check[i]


class Play():
    def __init__(self, hand_player_1, hand_player_2):
        self.hp1 = hand_player_1
        self.hp2 = hand_player_2

    def win(self):
        if self.hp1.best() == self.hp2.best():
            ##            print(self.hp1.best(),self.hp1.hc.value,self.hp2.hc.value)
            if self.hp1.hc.value == self.hp2.hc.value:
                ##                print(self.hp1.best(),self.hp2.hc.value)
                ##                print([i.value for i in self.hp1.bck],[j.value for j in self.hp2.bck])
                i = 0
                while self.hp1.bck[i].value == self.hp2.bck[i].value:
                    i += 1
                if self.hp1.bck[i].value > self.hp2.bck[i].value:
                    return 1
            if self.hp1.hc > self.hp2.hc:
                return 1
        if self.hp1.best() > self.hp2.best():
            return 1
        return 2


file = open('poker.txt', 'r')
poker = file.read().split()
file.close()

poker_hands = [(tuple(poker[n:n + 5]), tuple(poker[n + 5:n + 10])) for n in range(0, 10000, 10)]

player_1 = 0

for hand in poker_hands:
    x = 1
    y = 6
    for card in hand[0]:
        globals()['card' + str(x)] = Card(card[0], card[1])
        x += 1
    for card in hand[1]:
        globals()['card' + str(y)] = Card(card[0], card[1])
        y += 1
    hand1 = Hand([eval('card' + str(i)) for i in range(1, 6)])
    hand2 = Hand([eval('card' + str(j)) for j in range(6, 11)])
    p = Play(hand1, hand2)
    if p.win() == 1:
        player_1 += 1

print(player_1)
