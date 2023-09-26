import pandas as pd
import config
import os
import pdb

from matplotlib import pyplot as plt

def vis_filter_loss_accuracy():
    max_size=14
    plotdata = []
    names = []
    for file in file_paths:
        filter = file.split('/')[-1].split('.')[0].split('_')[0]
        names.append(filter)
        data = pd.read_csv(file)

        missing_rows = max_size-data.shape[0]
        info = data[data.shape[0]-1:]

        for i in range(missing_rows):
              data = pd.concat([data, info], ignore_index=True)

        plotdata.append(data)

    fig, axs = plt.subplots(1, 2, figsize=(15,6), sharey=True )

    xaxis = [i for i in range(plotdata[0].shape[0])]

    for index in range(len(plotdata)):

        axs[0].plot(xaxis, plotdata[index]['loss'].values)
        axs[0].legend(names)
        axs[0].set_title('A)                         Training Loss   ',  loc='left')
        axs[0].set_ylim(0, 7)
        axs[0].set_xlabel('epochs')
        axs[0].set_ylabel('training loss')


        axs[1].plot(xaxis, plotdata[index]['val_loss'].values)
        axs[1].set_title('B)                         Validation Loss   ',  loc='left')
        axs[1].legend(names)
        axs[1].set_xlabel('epochs')
        axs[1].set_ylabel('validation loss')
    plt.tight_layout()

    fig.savefig(config.IMAGES_DIR + 'filter_loss.png', dpi=600)


    fig, axs = plt.subplots(1, 2, figsize=(15,6), sharey=True )

    xaxis = [i for i in range(plotdata[0].shape[0])]

    for index in range(len(plotdata)):

        axs[0].plot(xaxis, plotdata[index]['accuracy'].values)
        axs[0].legend(names)
        axs[0].set_title('A)                         Training Accuracy   ',  loc='left')
        axs[0].set_ylim(0, 1)
        axs[0].set_xlabel('epochs')
        axs[0].set_ylabel('training accuracy')


        axs[1].plot(xaxis, plotdata[index]['val_accuracy'].values)
        axs[1].set_title('B)                         Validation Accuracy   ',  loc='left')
        axs[1].legend(names)
        axs[1].set_xlabel('epochs')
        axs[1].set_ylabel('validation accuracy')

    plt.tight_layout()
    fig.savefig(config.IMAGES_DIR + 'filter_accuracy.png', dpi=600)
    
    
def vis_layer_loss_accuracy():
    
    folder_path = config.RESULTS
    files = os.listdir(folder_path)
    file_paths = [os.path.join(folder_path, file) for file in files if file.endswith('.csv') and file.startswith('3')]
    file_paths = sorted(file_paths, key=lambda x: os.path.basename(x))
    print(file_paths)
    #pdb.set_trace()
    
    max_size=10
    plotdata = []
    names = []
    for file in file_paths:
        filtr = file.split('/')[-1].split('.')[0].split('_')[1]
        names.append(filtr)
        data = pd.read_csv(file)
        #pdb.set_trace()
        missing_rows = max_size-data.shape[0]
        info = data[data.shape[0]-1:]

        for i in range(missing_rows):
              data = pd.concat([data, info], ignore_index=True)

        plotdata.append(data)

    fig, axs = plt.subplots(1, 2, figsize=(15,6), sharey=True )

    xaxis = [i for i in range(plotdata[0].shape[0])]

    for index in range(len(plotdata)):

        axs[0].plot(xaxis, plotdata[index]['loss'].values)
        axs[0].legend(names)
        axs[0].set_title('A)                         Training Loss   ',  loc='left')
        axs[0].set_ylim(0, 7)
        axs[0].set_xlabel('epochs')
        axs[0].set_ylabel('training loss')


        axs[1].plot(xaxis, plotdata[index]['val_loss'].values)
        axs[1].set_title('B)                         Validation Loss   ',  loc='left')
        axs[1].legend(names)
        axs[1].set_xlabel('epochs')
        axs[1].set_ylabel('validation loss')
    plt.tight_layout()

    fig.savefig('layer_3_loss.png', dpi=600)


    fig, axs = plt.subplots(1, 2, figsize=(15,6), sharey=True )

    xaxis = [i for i in range(plotdata[0].shape[0])]

    for index in range(len(plotdata)):

        axs[0].plot(xaxis, plotdata[index]['accuracy'].values)
        axs[0].legend(names)
        axs[0].set_title('A)                         Training Accuracy   ',  loc='left')
        axs[0].set_ylim(0, 1)
        axs[0].set_xlabel('epochs')
        axs[0].set_ylabel('training accuracy')


        axs[1].plot(xaxis, plotdata[index]['val_accuracy'].values)
        axs[1].set_title('B)                         Validation Accuracy   ',  loc='left')
        axs[1].legend(names)
        axs[1].set_xlabel('epochs')
        axs[1].set_ylabel('validation accuracy')

    plt.tight_layout()
    fig.savefig('layer_3_accuracy.png', dpi=600)

    
    
def vis_filter_layer():
    
    folder_path = config.RESULTS
    files = os.listdir(folder_path)
    file_paths = [os.path.join(folder_path, file) for file in files if file.endswith('.csv')]
    file_paths = sorted(file_paths, key=lambda x: os.path.basename(x))
    
    
    filtrs = []
    layers = []
    accuracys = []
    losses = []
    
    for file in file_paths:
        filtr = file.split('/')[-1].split('.')[0].split('_')[0]
        layer = file.split('/')[-1].split('.')[0].split('_')[1]
        
        data = pd.read_csv(file)
        
        loss = data.iloc[data.shape[0]-1]['val_loss']
        accuracy = data.iloc[data.shape[0]-1]['val_accuracy']
        
        filtrs.append(filtr)
        accuracys.append(accuracy)
        layers.append(layer)
        losses.append(loss)
        
        
    
    data = {'filter':filtrs, 'layers':layers, 'loss':losses, 'accuracy':accuracys}
    
    data = pd.DataFrame(data)
    
    
    
    
    
def vis_test_filter_layer():
    
    folder_path = config.RESULTS
    files = os.listdir(folder_path)
    file_paths = [os.path.join(folder_path, file) for file in files if file.endswith('.txt')]
    file_paths = sorted(file_paths, key=lambda x: os.path.basename(x))
    
    pdb.set_trace()
    
    #with f
    
vis_layer_loss_accuracy()