import itertools
import random
from tensorflow.keras import *
from tensorflow.keras.layers import *
import numpy as np
import game
import pandas as pd

aDeck = game.Deck()
aBlackJack = game.BlackJack()
ranks = [str(x) for x in list(range(2, 11))] + ['A', 'J', 'Q', 'K']
suits = ['♠', '♣', '♦', '♥']
decks = [x + y for x in ranks for y in suits]

def rev(X):
    te = np.array(X).astype(bool)
    return np.array(decks)[te]

xs = []
ys = []
cnt = 7 * 50 ** 3

for threshold in range(15,22):
    for i in decks:
        for j in decks:
            for k in decks :
                if i != j and j != k:
                    if cnt == 0:
                        break
                    cnt -= 1
                    sample = [i, j, k]
                    aCard_Indices = []
                    value = aBlackJack.eval(sample)
                    y = int(value > threshold and value <= 21)
                    for aCard in sample:
                        aCard_Indices.append(decks.index(aCard))

                    x = np.zeros(len(decks))
                    x[aCard_Indices[:-1]] = 1
                    xs.append(x)
                    ys.append(y)
xs = np.array(xs)
ys = np.array(ys)
df = pd.DataFrame(np.c_[xs, ys[..., np.newaxis]])
df.to_csv('train.csv')
print(xs.shape, ys.shape)
