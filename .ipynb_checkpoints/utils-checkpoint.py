import pandas as pd
import config



def load_train_data():
    '''
        Loads train data and labels from the path spacified in the config file
    '''
    print('Loading Train data...')
    train_data = config.TRAIN_DATA + 'csvTrainImages 13440x1024.csv'
    train_data = pd.read_csv(train_data, header=None)
    train_labels = config.TRAIN_DATA +  'csvTrainLabel 13440x1.csv'
    train_labels = pd.read_csv(train_labels, header=None)
    train_labels = train_labels - 1


    return train_data, train_labels

def load_test_data():
    '''
        Loads test data and labels from the path spacified in the config file
    '''
    print('Loading test data...')

    test_data = config.TEST_DATA + 'csvTestImages 3360x1024.csv'
    test_data= pd.read_csv(test_data, header=None)
    test_labels = config.TEST_DATA + 'csvTestLabel 3360x1.csv'
    test_labels = pd.read_csv(test_labels, header=None)
    test_labels = test_labels - 1

    return test_data, test_labels
