import json
import numpy as np
from base_feedforward import Layer

layers_size = [100, 50, 50, 12]

H1 = Layer(np.random.RandomState(1234), layers_size[0], layers_size[1])
H2 = Layer(np.random.RandomState(1234), layers_size[1], layers_size[2])
Out = Layer(np.random.RandomState(1234), layers_size[2], layers_size[3])

network = {'size': layers_size, 'weights': [H1.W.tolist(), H2.W.tolist(), Out.W.tolist()],
           'biases': [H1.b.tolist(), H2.b.tolist(), Out.b.tolist()]}

f = open('testnet.json', 'w')
##f.write(
##    "Size: {0}\nWeights: [{1},{3}]\nBiases:[{2},{4}]"
##    .format(network['size'], network['weights'][0], network['biases'][0],
##            network['weights'][1], network['biases'][1]))
json.dump(network, f)
f.close()

