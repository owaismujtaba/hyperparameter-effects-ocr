import tensorflow as tf
from sklearn.model_selection import train_test_split
import numpy as np
from utils import load_train_data, load_test_data
from tensorflow.keras.callbacks import EarlyStopping
import pandas as pd
from sklearn.metrics import classification_report
import config
import pdb

def trainner(model, name):
    import pdb
    pdb.set_trace()
    print(model.summary())
    train_data, train_labels = load_train_data()
    test_data, test_labels = load_test_data()
    X_train, X_test, y_train, y_test = train_test_split(train_data, train_labels, random_state=104, test_size=0.25, shuffle=True)
    X_train = np.array(X_train).reshape(-1, 32, 32)
    X_test = np.array(X_test).reshape(-1, 32, 32)
    print(X_train.shape, y_train.shape,  X_test.shape, y_test.shape)
    early_stopping = EarlyStopping(monitor='val_loss', patience=4, restore_best_weights=True)

    history = model.fit(X_train, y_train, epochs=config.EPOCHS, validation_data=(X_test, y_test), callbacks=[early_stopping] )
    #tf.saved_model.save(model, 'model.h5')
    data = pd.DataFrame(history.history)
    data.to_csv(config.RESULTS + name)
    test_data = np.array(test_data)
    




    test_data = test_data.reshape(-1, 32, 32)
    pred = model.predict(test_data)
    report = classification_report(np.argmax(pred, axis=1), test_labels)

    print(report)



def trainner_expand(model, name):

    train_data, train_labels = load_train_data()
    test_data, test_labels = load_test_data()
    X_train, X_test, y_train, y_test = train_test_split(train_data, train_labels, random_state=104, test_size=0.25, shuffle=True)
    
    X_train = np.array(X_train).reshape(-1, 32, 32)
    X_test = np.array(X_test).reshape(-1, 32, 32)


    print(X_test.shape, X_train.shape)

    temp = np.zeros((X_train.shape[0], 32, 32))
    X_train = np.concatenate((X_train, temp), axis=1)
    temp = np.zeros((X_train.shape[0], X_train.shape[1], 32))
    X_train = np.concatenate((X_train, temp), axis=2)
    print(X_test.shape, X_train.shape)
    import pdb
    pdb.set_trace()
    temp = np.zeros((X_test.shape[0], 32, 32))
    X_test = np.concatenate((X_test, temp), axis=1)
    temp = np.zeros((X_test.shape[0], X_test.shape[1], 32))
    X_test = np.concatenate((X_test, temp), axis=2)

    

    print(X_test.shape, X_train.shape)


    early_stopping = EarlyStopping(monitor='val_loss', patience=4, restore_best_weights=True)

    history = model.fit(X_train, y_train, epochs=config.EPOCHS, validation_data=(X_test, y_test), callbacks=[early_stopping] )
    #tf.saved_model.save(model, 'model.h5')
    data = pd.DataFrame(history.history)
    data.to_csv(config.RESULTS + name)
    test_data = np.array(test_data)
    
    
    test_data = test_data.reshape(-1, 32, 32)

    temp = np.zeros((test_data.shape[0], 32, 32))
    test_data = np.concatenate((test_data, temp), axis=1)
    temp = np.zeros((test_data.shape[0], test_data.shape[1], 32))
    test_data = np.concatenate((test_data, temp), axis=2)


    pred = model.predict(test_data)
    report = classification_report(np.argmax(pred, axis=1), test_labels)

    print(report)
