"""
Simplest model for testing:  2 hidden layers with 10 units apiece, and one
logistic sigmoid output unit.  Thresholding function is piecewise linear.

This model was employed in "An empirical analysis of dropout in piecewise linear networks"
by Warde-Farley et. al.  It was used to solve binary problems over the MNIST dataset
as well as a toy problem by the others.
"""
import numpy as np
from base_feedforward import Layer
from scipy.special import expit
from data_handler import load_data


class WFModel(object):

    def __init__(self):
        #note: size of input layer is size of MNIST image
        layers_size = [28 * 28, 10, 10, 1]
        self.size = layers_size
        rectifier_func = lambda x: max(0,x)
        #expit function is also known as the logistic function.
        #definition is to make this clear in the program
        sigmoid = lambda x: expit(x)
        rng = np.random.RandomState(1234)
        
        H1 = Layer(rng, layers_size[0], layers_size[1], None, None, rectifier_func)
        H2 = Layer(rng, layers_size[1], layers_size[2], None, None, rectifier_func)
        Out = Layer(rng, layers_size[2], layers_size[3], None, None, sigmoid)

        self.layers = [H1, H2, Out]

    def run_input(self, _input):
        H1_output = H1.run_input(_input)
        H2_output = H2.run_input(H1_output)
        return Out.run_input(H2)

    def get_params(self):
        H1, H2, Out = self.layers
        return {'model': 'WFModel',
                'size': self.size,
                'weights': [H1.W.tolist(), H2.W.tolist(), Out.W.tolist()],
                'biases': [H1.b.tolist(), H2.b.tolist(), Out.b.tolist()]}

def test_WFModel():
    rectifier_func = lambda x: max(0,x)
    wf = WFModel()
    params = wf.get_params()
    
    import json
    f = open('testnet.json', 'w')
    json.dump(params, f)
    f.close()
    
    dataset = 'mnist.pkl.gz'
    classes = [1, 8]
    datasets = load_data(dataset, classes)
    train_set_x, train_set_y = datasets[0]
    valid_set_x, valid_set_y = datasets[1]
    test_set_x, test_set_y = datasets[2]
    print train_set_y[0]
    print type(train_set_y[0])

if __name__ == '__main__':
    test_WFModel()
