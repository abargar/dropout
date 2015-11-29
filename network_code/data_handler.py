import os
import gzip
import cPickle
import numpy as np

def load_data(dataset, classes = None):
    ''' Loads the dataset

    :type dataset: string
    :type classes (added): list of strings
    :param dataset: the path to the dataset (here MNIST)
    :param classes: if exist, specify which classes from the dataset to include
    '''


    # Download the MNIST dataset if it is not present
    data_dir, data_file = os.path.split(dataset)
    if data_dir == "" and not os.path.isfile(dataset):
        # Check if dataset is in the data directory.
        new_path = os.path.join(
            os.path.split(__file__)[0],
            "data",
            dataset
        )
        if os.path.isfile(new_path) or data_file == 'mnist.pkl.gz':
            dataset = new_path

    if (not os.path.isfile(dataset)) and data_file == 'mnist.pkl.gz':
        import urllib
        origin = (
            'http://www.iro.umontreal.ca/~lisa/deep/data/mnist/mnist.pkl.gz'
        )
        print 'Downloading data from %s' % origin
        urllib.urlretrieve(origin, dataset)

    print '... loading data'

    # Load the dataset
    f = gzip.open(dataset, 'rb')
    train_set, valid_set, test_set = cPickle.load(f)
    f.close()
    if classes:
        return filter_by_classes([train_set, valid_set, test_set], classes)
    else:
        return [train_set, valid_set, test_set]

def filter_by_classes(datasets, classes):
    train_x, train_y = datasets[0]
    valid_x, valid_y = datasets[1]
    test_x, test_y = datasets[2]
    
    indices = np.in1d(train_y.ravel(), classes).reshape(train_y.shape)
    class_inds = np.where(indices)
    filtered_train_set = [train_x[class_inds], train_y[class_inds]]
    
    indices = np.in1d(valid_y.ravel(), classes).reshape(valid_y.shape)
    class_inds = np.where(indices)
    filtered_valid_set = [valid_x[class_inds], valid_y[class_inds]]    

    indices = np.in1d(test_y.ravel(), classes).reshape(test_y.shape)
    class_inds = np.where(indices)
    filtered_test_set = [test_x[class_inds], test_y[class_inds]]

    return [filtered_train_set, filtered_valid_set, filtered_test_set]

def test_data_handler():
    datasets = load_data('mnist.pkl.gz', [1,8])

    train_set = datasets[0]
    train_x = train_set[0]
    train_y = train_set[1]
    import matplotlib.pyplot as plt
    
    print train_y[25]
    test_img = train_x[25].reshape(28, 28)
    plt.gray()
    plt.imshow(test_img)
    plt.axis('off')
    plt.show()

    
    
    
if __name__ == '__main__':
    test_data_handler()
