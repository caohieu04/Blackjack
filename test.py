import model
import pandas as pd
import numpy as np
import game
ranks = [str(x) for x in list(range(2, 11))] + ['A', 'J', 'Q', 'K']
suits = ['♠', '♣', '♦', '♥']
decks = [x + y for x in ranks for y in suits]
epochs = 5

model = model.MyModel()
model = model.Sequential

model.load_weights('train1.pt')
df = pd.read_csv('train1.csv')
te = np.array(df.values)

xs = te[:,1:-1]
ys = te[:,-1]
ys[ys == 0] = -1

black_jack = game.BlackJack()

mp = dict.fromkeys(range(2, 32))

# xs = xs[:1000]
# ys = ys[:1000]
# print(xs.shape)
pred = model.predict(xs)

# for x in xs:
#     print(type(x))
#     for i, x_elem in enumerate(x):
#         if x_elem == 1: print(decks[i] )
cards = [[decks[i]for i, x_elem in enumerate(x) if x_elem == 1] for x in xs ]
print(pred.shape)
print(len(cards))
scores = np.array([black_jack.eval(card) for card in cards])
print(scores.shape)


for i in np.unique(scores):
    val = np.sum(pred[scores == i]) / pred[scores == i].shape[0]
    print(f'{i}-score = {val}')

