import json

def visualize_net(net, epoch, shape):
    nLayers = len(shape)

    netW = []
    
    for i in range(nLayers-1):
        print 'Layer ', i
        fName = '../snapshots/{0}/params_{1}_layer_{2}.txt'.format(net, epoch, i)
        with open(fName, 'rb') as f:
            read_data = f.read()
            rows = read_data.split(';\n')
            rows = rows[:-1]
            print 'Number of rows: ', len(rows)
            layerW = [[float(val) for val in row.split(', ')] for row in rows ]
            print len(layerW)
            netW.append(layerW)
    network = { 'size': shape, 'weights': netW, 'biases': None }
    with open('{0}_{1}_net.json'.format(net, epoch), 'w') as fjson:
        json.dump(network, fjson)
    return None

visualize_net('broken_wfmodel_backprop', 300, [28*28, 10, 10, 1])
    
