import numpy as np
from math import tanh

class Layer:
    
    #_input = None
    W = None
    b = None
    activation = None

    def __init__(self, rng, n_in, n_out, W = None, b = None, activation=np.tanh,
                 dropout = False):
        
        if W == None:
            W = np.asarray(
                rng.uniform(
                    low = -np.sqrt(6. / (n_in + n_out)),
                    high = np.sqrt(6. / (n_in + n_out)),
                    size = (n_in, n_out)
                    ))
        if b == None:
            b = ( np.zeros(n_out))
        self.W = W
        self.b = b
        self.activation = activation


    def run_input(self,_input):
        print "Size of input: ", _input.shape
        lin_output = np.dot(self.W, _input) + self.b
        print self.activation
        if self.activation != None:
            print "Running activation"
            return self.activation(lin_output)
        else:
            print "Skipping activation"
            return lin_output

        
def __main__():
    test_input = np.ones((8,1))
    H = Layer(np.random.RandomState(1234), 8, 8)
    H_output = H.run_input(test_input)
    print "H output: \n", H_output
    
