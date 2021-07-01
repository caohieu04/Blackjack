import itertools
import random
from tensorflow.keras import *
from tensorflow.keras.layers import *
import numpy as np
ranks = [str(x) for x in list(range(2, 11))] + ['A', 'J', 'Q', 'K']
suits = ['♠', '♣', '♦', '♥']
decks = [x + y for x in ranks for y in suits]

class Deck:
    deck = None
    def __init__(self):
        self.deck = decks[:]
        self.shuffle()
    def draw(self, num_of_cards):
        if num_of_cards > len(self.deck):
            return None
        give_cards = self.deck[:num_of_cards]
        self.deck = self.deck[num_of_cards:]
        return give_cards
    def shuffle(self):
        random.shuffle(self.deck)
    def sample(self, num_of_cards):
        random.shuffle(self.deck)
        if num_of_cards > len(self.deck):
            return None
        give_cards = self.deck[:num_of_cards]
        return give_cards
class BlackJack:
    left = 16
    right = 21
    ace_values = ['1','10','11']
    def eval(self, hands):
        # if not hands:
        #     return "error"
        if hands.count('A') == len(hands):
            return 'xiban'

        hands = [x[:-1] for x in hands]
        hands = ['10' if x in ['J','Q','K'] else x  for x in hands ]
        num_of_aces = hands.count('A')
        sum_not_aces = sum(list(map(int, list(filter(lambda x: x != 'A', hands)))))

        if num_of_aces >= 1:
            default = list(itertools.product(self.ace_values, repeat=num_of_aces))
            sum_of_aces = [sum(list(map(int, list(x)))) for x in default]


            sums = [x + y for x in [sum_not_aces] * len(sum_of_aces) for y in sum_of_aces]
            try:
                sums = max(list(filter(lambda x: x >= 16 and x <= 21, sums)))
            except:
                sums = min(sums)
        else:
            sums = sum_not_aces
        return sums

aDeck = Deck()
aBlackJack = BlackJack()

# for _ in range(10):
#     te = aDeck.draw(3)
#     print(te)
#     print(aBlackJack.eval(te))

# model = Sequential([
#     Input(52),
#     Dense(128, activation='relu'),
#     Dense(64, activation='relu'),
#     Dense(32, activation='relu'),
#     Dense(16, activation='relu'),
#     Dense(1, activation='relu')
# ])
# model.compile(optimizer='sgd', loss='mse')
#
# def train1():
#     num_train1 = 100
#     xs = []
#     ys = []
#
#     for _ in range(num_train1):
#         sample = aDeck.sample(3)
#         aCard_Indices = []
#         value = aBlackJack.eval(sample)
#         y = int(value >= 16 and value <= 21)
#         for aCard in sample:
#             aCard_Indices.append(decks.index(aCard))
#
#         x = np.zeros(len(decks))
#         x[aCard_Indices[:-1]] = 1
#         xs.append(x)
#         ys.append(y)
#     return np.array(xs), np.array(ys)
#
#
# xs, ys = train1()
# print(xs.shape)
# model.fit(xs, ys, epochs=100)
#
# print(np.expand_dims(xs[0], axis=1).shape, ys[0])
# pred = model.predict(np.expand_dims(xs[0], axis=0))
#
# t1 = np.array(xs[0]).astype(bool)
# print(np.array(decks)[t1])
# print(pred, ys[0])
