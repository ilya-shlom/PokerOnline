# import numpy as np
# from sklearn.linear_model import LinearRegression
import pickle
#
#
# table = np.genfromtxt('game_logs/6_trump.csv', delimiter=';')
# x = np.array(table[:, 0]).reshape(-1, 1)
# y = np.array(table[:, 1])
#
# model = LinearRegression()
#
# model.fit(x, y)
#
# with open(f'models/model6_trump.sav', 'a') as data:
#     pass
#
# pickle.dump(model, open(f'models/model6_trump.sav', 'wb'))

loaded_model = pickle.load(open('models/model6.sav', 'rb'))

for i in range(20):
    print(f'{i} - {loaded_model.predict([[i]])}')
