import tensorflow as tf
from tensorflow.keras import layers, models
import numpy as np
import config

def model_3_1():
  model = models.Sequential()
  model.add(layers.Conv2D(128, (3, 3), activation='relu', input_shape=(config.IMAGE_HEIGHT, config.IMAGE_WIDTH, 1)))
  model.add(layers.Dense(512, activation='relu'))
  model.add(layers.Dense(128, activation='relu'))
  model.add(layers.Dense(config.OUTPUTS, activation='softmax'))

  # Compile the model
  model.compile(optimizer='adam',
                loss='sparse_categorical_crossentropy',
                metrics=['accuracy'])

  return model


def model_3_2():
  model = models.Sequential()
  model.add(layers.Conv2D(128, (3, 3), activation='relu', input_shape=(config.IMAGE_HEIGHT, config.IMAGE_WIDTH, 1)))
  model.add(layers.Conv2D(128, (3, 3), activation='relu', input_shape=(config.IMAGE_HEIGHT, config.IMAGE_WIDTH, 1)))
  model.add(layers.Dense(512, activation='relu'))
  model.add(layers.Dense(128, activation='relu'))
  model.add(layers.Dense(config.OUTPUTS, activation='softmax'))

  # Compile the model
  model.compile(optimizer='adam',
                loss='sparse_categorical_crossentropy',
                metrics=['accuracy'])

  return model

def model_3_3():
  model = models.Sequential()
  model.add(layers.Conv2D(128, (3, 3), activation='relu', input_shape=(config.IMAGE_HEIGHT, config.IMAGE_WIDTH, 1)))
  model.add(layers.Conv2D(128, (3, 3), activation='relu', input_shape=(config.IMAGE_HEIGHT, config.IMAGE_WIDTH, 1)))
  model.add(layers.Conv2D(128, (3, 3), activation='relu', input_shape=(config.IMAGE_HEIGHT, config.IMAGE_WIDTH, 1)))

  model.add(layers.Dense(512, activation='relu'))
  model.add(layers.Dense(128, activation='relu'))
  model.add(layers.Dense(config.OUTPUTS, activation='softmax'))

  # Compile the model
  model.compile(optimizer='adam',
                loss='sparse_categorical_crossentropy',
                metrics=['accuracy'])

  return model

def model_3_5():
  model = models.Sequential()
  model.add(layers.Conv2D(128, (3, 3), activation='relu', input_shape=(config.IMAGE_HEIGHT, config.IMAGE_WIDTH, 1)))
  model.add(layers.Conv2D(128, (3, 3), activation='relu', input_shape=(config.IMAGE_HEIGHT, config.IMAGE_WIDTH, 1)))
  model.add(layers.Conv2D(128, (3, 3), activation='relu', input_shape=(config.IMAGE_HEIGHT, config.IMAGE_WIDTH, 1)))
  model.add(layers.Conv2D(128, (3, 3), activation='relu', input_shape=(config.IMAGE_HEIGHT, config.IMAGE_WIDTH, 1)))
  model.add(layers.Conv2D(128, (3, 3), activation='relu', input_shape=(config.IMAGE_HEIGHT, config.IMAGE_WIDTH, 1)))
  model.add(layers.Dense(512, activation='relu'))
  model.add(layers.Dense(128, activation='relu'))
  model.add(layers.Dense(config.OUTPUTS, activation='softmax'))

  # Compile the model
  model.compile(optimizer='adam',
                loss='sparse_categorical_crossentropy',
                metrics=['accuracy'])

  return model
def model_3_7():
  model = models.Sequential()
  model.add(layers.Conv2D(128, (3, 3), activation='relu', input_shape=(config.IMAGE_HEIGHT, config.IMAGE_WIDTH, 1)))
  model.add(layers.Conv2D(128, (3, 3), activation='relu', input_shape=(config.IMAGE_HEIGHT, config.IMAGE_WIDTH, 1)))
  model.add(layers.Conv2D(128, (3, 3), activation='relu', input_shape=(config.IMAGE_HEIGHT, config.IMAGE_WIDTH, 1)))
  model.add(layers.Conv2D(128, (3, 3), activation='relu', input_shape=(config.IMAGE_HEIGHT, config.IMAGE_WIDTH, 1)))
  model.add(layers.Conv2D(128, (3, 3), activation='relu', input_shape=(config.IMAGE_HEIGHT, config.IMAGE_WIDTH, 1)))
  model.add(layers.Conv2D(128, (3, 3), activation='relu', input_shape=(config.IMAGE_HEIGHT, config.IMAGE_WIDTH, 1)))
  model.add(layers.Conv2D(128, (3, 3), activation='relu', input_shape=(config.IMAGE_HEIGHT, config.IMAGE_WIDTH, 1)))
  model.add(layers.Dense(512, activation='relu'))
  model.add(layers.Dense(128, activation='relu'))
  model.add(layers.Dense(config.OUTPUTS, activation='softmax'))

  # Compile the model
  model.compile(optimizer='adam',
                loss='sparse_categorical_crossentropy',
                metrics=['accuracy'])

  return model
  
def model_3_9():
  model = models.Sequential()
  model.add(layers.Conv2D(128, (3, 3), activation='relu', input_shape=(config.IMAGE_HEIGHT, config.IMAGE_WIDTH, 1)))
  model.add(layers.Conv2D(128, (3, 3), activation='relu', input_shape=(config.IMAGE_HEIGHT, config.IMAGE_WIDTH, 1)))
  model.add(layers.Conv2D(128, (3, 3), activation='relu', input_shape=(config.IMAGE_HEIGHT, config.IMAGE_WIDTH, 1)))
  model.add(layers.Conv2D(128, (3, 3), activation='relu', input_shape=(config.IMAGE_HEIGHT, config.IMAGE_WIDTH, 1)))
  model.add(layers.Conv2D(128, (3, 3), activation='relu', input_shape=(config.IMAGE_HEIGHT, config.IMAGE_WIDTH, 1)))
  model.add(layers.Conv2D(128, (3, 3), activation='relu', input_shape=(config.IMAGE_HEIGHT, config.IMAGE_WIDTH, 1)))
  model.add(layers.Conv2D(128, (3, 3), activation='relu', input_shape=(config.IMAGE_HEIGHT, config.IMAGE_WIDTH, 1)))
  model.add(layers.Conv2D(128, (3, 3), activation='relu', input_shape=(config.IMAGE_HEIGHT, config.IMAGE_WIDTH, 1)))
  model.add(layers.Conv2D(128, (3, 3), activation='relu', input_shape=(config.IMAGE_HEIGHT, config.IMAGE_WIDTH, 1)))
  
  model.add(layers.Dense(512, activation='relu'))
  model.add(layers.Dense(128, activation='relu'))
  model.add(layers.Dense(config.OUTPUTS, activation='softmax'))

  # Compile the model
  model.compile(optimizer='adam',
                loss='sparse_categorical_crossentropy',
                metrics=['accuracy'])

  return model


def model_11_4():
  model = models.Sequential()
  model.add(layers.Conv2D(128, (11, 11), activation='relu', input_shape=(config.IMAGE_HEIGHT+32, config.IMAGE_WIDTH+32, 1)))
  #model.add(layers.MaxPooling2D((2, 2)))
  model.add(layers.Conv2D(256, (11, 11), activation='relu'))
  #model.add(layers.MaxPooling2D((2, 2)))
  model.add(layers.Conv2D(512, (11, 11), activation='relu'))
  #model.add(layers.MaxPooling2D((2, 2)))
  model.add(layers.Conv2D(128, (11, 11), activation='relu'))
  model.add(layers.MaxPooling2D((2, 2)))
  model.add(layers.Flatten())
  model.add(layers.Dense(512, activation='relu'))
  model.add(layers.Dense(128, activation='relu'))
  model.add(layers.Dense(config.OUTPUTS, activation='softmax'))

  # Compile the model
  model.compile(optimizer='adam',
                loss='sparse_categorical_crossentropy',
                metrics=['accuracy'])

  return model



def model_3_4():
  model = models.Sequential()
  model.add(layers.Conv2D(128, (3, 3), activation='relu', input_shape=(config.IMAGE_HEIGHT, config.IMAGE_WIDTH, 1)))
  model.add(layers.MaxPooling2D((2, 2)))
  model.add(layers.Conv2D(256, (3, 3), activation='relu'))
  model.add(layers.MaxPooling2D((2, 2)))
  model.add(layers.Conv2D(512, (3, 3), activation='relu'))
  #model.add(layers.MaxPooling2D((2, 2)))
  model.add(layers.Conv2D(128, (3, 3), activation='relu'))
  model.add(layers.MaxPooling2D((2, 2)))
  model.add(layers.Flatten())
  model.add(layers.Dense(512, activation='relu'))
  model.add(layers.Dense(128, activation='relu'))
  model.add(layers.Dense(config.OUTPUTS, activation='softmax'))

  # Compile the model
  model.compile(optimizer='adam',
                loss='sparse_categorical_crossentropy',
                metrics=['accuracy'])

  return model



def model_5_4():
  model = models.Sequential()
  model.add(layers.Conv2D(128, (5, 5), activation='relu', input_shape=(config.IMAGE_HEIGHT, config.IMAGE_WIDTH, 1)))
  model.add(layers.MaxPooling2D((2, 2)))
  model.add(layers.Conv2D(256, (5, 5), activation='relu'))
  #model.add(layers.MaxPooling2D((2, 2)))
  model.add(layers.Conv2D(512, (5, 5), activation='relu'))
  #model.add(layers.MaxPooling2D((2, 2)))
  model.add(layers.Conv2D(128, (5, 5), activation='relu'))
  model.add(layers.MaxPooling2D((2, 2)))
  model.add(layers.Flatten())
  model.add(layers.Dense(512, activation='relu'))
  model.add(layers.Dense(128, activation='relu'))
  model.add(layers.Dense(config.OUTPUTS, activation='softmax'))

  # Compile the model
  model.compile(optimizer='adam',
                loss='sparse_categorical_crossentropy',
                metrics=['accuracy'])

  
  return model



def model_7_4():
  model = models.Sequential()
  model.add(layers.Conv2D(128, (7, 7), activation='relu', input_shape=(config.IMAGE_HEIGHT, config.IMAGE_WIDTH, 1)))
  #model.add(layers.MaxPooling2D((2, 2)))
  model.add(layers.Conv2D(256, (7, 7), activation='relu'))
  #model.add(layers.MaxPooling2D((2, 2)))
  model.add(layers.Conv2D(512, (7, 7), activation='relu'))
  #model.add(layers.MaxPooling2D((2, 2)))
  model.add(layers.Conv2D(128, (7, 7), activation='relu'))
  model.add(layers.MaxPooling2D((2, 2)))
  model.add(layers.Flatten())
  model.add(layers.Dense(512, activation='relu'))
  model.add(layers.Dense(128, activation='relu'))
  model.add(layers.Dense(config.OUTPUTS, activation='softmax'))

  # Compile the model
  model.compile(optimizer='adam',
                loss='sparse_categorical_crossentropy',
                metrics=['accuracy'])

  
  return model


def model_9_4():
  model = models.Sequential()
  model.add(layers.Conv2D(128, (9, 9),padding='valid', activation='relu', input_shape=(config.IMAGE_HEIGHT, config.IMAGE_WIDTH, 1)))
  #model.add(layers.MaxPooling2D((2, 2)))
  model.add(layers.Conv2D(256, (9, 9), activation='relu', padding='valid'))
  #model.add(layers.MaxPooling2D((2, 2)))
  model.add(layers.Conv2D(512, (9, 9), activation='relu',padding='valid'))
  #model.add(layers.MaxPooling2D((2, 2)))
  model.add(layers.Conv2D(128, (5, 5), activation='relu'))
  model.add(layers.MaxPooling2D((2, 2)))
  model.add(layers.Flatten())
  model.add(layers.Dense(512, activation='relu'))
  model.add(layers.Dense(128, activation='relu'))
  model.add(layers.Dense(config.OUTPUTS, activation='softmax'))


  model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy',
                  metrics=['accuracy'])

  return model

