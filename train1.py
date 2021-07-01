import model
import pandas as pd
import numpy as np
ranks = [str(x) for x in list(range(2, 11))] + ['A', 'J', 'Q', 'K']
suits = ['♠', '♣', '♦', '♥']
decks = [x + y for x in ranks for y in suits]
epochs = 10

model = model.MyModel()
model = model.Sequential

# model.load_weights('train1.pt')
df = pd.read_csv('Data/train1.csv')
te = np.array(df.values)

xs = te[:,1:-1]
ys = te[:,-1]
ys[ys == 0] = -1
# print(ys[-30:])
# print(xs.shape, ys.shape)
model.compile(optimizer='sgd', loss='mse')
history = model.fit(xs, ys, epochs=epochs)

def predict_it(X, Y):
    pred = model.predict(np.expand_dims(X, axis=0))
    te = np.array(X).astype(bool)
    print(f'EV: {pred[0][0]:.4f} | True label: {Y}  | Cards: {np.array(decks)[te]}')
import random
predicts = random.sample(range(1, 800000), 100)
for p in predicts:
    predict_it(xs[p], ys[p])

model.save('train1.pt')
