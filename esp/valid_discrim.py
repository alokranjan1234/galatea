from galatea.esp import Im2Word

dataset = Im2Word(start=99000, stop=100000
                          )

from pylearn2.utils import serial

model = serial.load('rectifier_7.pkl')

import theano.tensor as T
X = T.matrix()
state = model.fprop(X)
target = T.matrix()

right_cost = model.layers[-1].kl(Y=target, Y_hat=state)
wrong_cost = model.layers[-1].kl(Y=target[::-1,:], Y_hat=state)

from theano.printing import Print
right_cost = Print('right_cost')(right_cost)

acc = (wrong_cost > right_cost).mean()

from theano import function

f = function([X, target], acc)

acc = f(dataset.X, dataset.y)

print acc
