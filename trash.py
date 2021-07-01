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
# xs, ys = train1()
# print(xs.shape, ys[..., np.newaxis].shape)
# df = pd.DataFrame(np.c_[xs, ys[..., np.newaxis]])
#
# df.to_csv('train1.csv')
#
# dg = pd.read_csv('train1.csv')
#
# te = np.array(dg.head(5).values)
# print(te[:,1:-1])
# print(te[:,-1])
# print(df.head(5))
# print(te.shape)
# model = Sequential([
#     Input(52),
#     Dense(128, activation='relu'),
#     Dense(64, activation='relu'),
#     Dense(32, activation='relu'),
#     Dense(16, activation='relu'),
#     Dense(1, activation='relu')
# ])
#
# xs = te[:,1:-1]
# ys = te[:,-1]
# print(xs.shape, ys.shape)
# model.compile(optimizer='sgd', loss='mse')
# model.fit(xs, ys, epochs=100)
#
# print(xs[0][..., np.newaxis].shape)
# model.predict(np.expand_dims(xs[0], axis=0))
# t1 = np.array(xs[0]).astype(bool)
# print(np.array(decks)[t1])