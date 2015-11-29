import numpy as np
from base_feedforward import Layer
from data_handler import load_data

ReLU = np.vectorize(lambda x: max(0.0,x))
identity = np.vectorize(lambda x: x)
shape = [28*28, 1200, 1200, 10]
activations = [ReLU, ReLU, identity]
layers = []
net = 'hinton_backprop'
epoch = 1200

dropout = False
num_samples = 200

for class_label in range(1):
    
    datasets = load_data('data/mnist.pkl.gz', [class_label])
    train_set = datasets[0]
    train_x = train_set[0][0:num_samples,:]
    train_y = train_set[1][0:num_samples]

    sum_values = np.array([ np.zeros(shape[1]), np.zeros(shape[2]), np.zeros(shape[3]) ])

    print '!!! Current class label: {} !!!'.format(class_label)
    for epoch in [2700]:
        print 'Current epoch: ', epoch
        for i in range(len(shape) - 1):
            fName = 'snapshots/{0}/params_{1}_layer_{2}.txt'.format(net, epoch, i)
            with open(fName, 'rb') as f:
                read_data = f.read()
                rows = read_data.split(';\n')
                rows = rows[:-1]
                layerW = [[float(val) for val in row.split(', ')] for row in rows ]
                layers.append(np.asarray(layerW))
                np.savetxt("{}_{}_layer{}.csv".format(net, epoch, i), np.asarray(layerW), delimiter=",")
##        for counter in range(num_samples):
##            if counter % 10 == 0:
##                print 'on sample ', counter
##            test_img = train_x[counter]
##            test_value = train_y[counter]
##            layer_input = test_img
##
##            for i in range(len(shape) - 1):
##                outputName = 'activations/{}/{}/{}_{}.csv'.format(net, class_label, epoch, i)
##                with open(outputName, 'ab') as f:
##                    lin_output = np.tensordot(layer_input, layers[i], (0,0))
##                    output = activations[i](lin_output)
####                    sum_values[i] += output
##                    layer_input = output
##                    f.write(', '.join('%f' %F for F in output))
##                    f.write('\n')

##        avg_values = [layer_sum / num_samples for layer_sum in sum_values]
##        avgOutputName = 'activations/{}/{}/epoch={}_average_over_{}.csv'.format(net, class_label, epoch, num_samples)

##        with open(avgOutputName, 'ab') as f:
##            for i in range(len(avg_values)):
##                f.write(', '.join('%f' %F for F in avg_values[i]))
##                f.write('\n')
