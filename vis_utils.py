import pandas as pd
import config


from matplotlib import pyplot as pyplot


def varying_filter():
  folder_path = '/content/gdrive/MyDrive/Thesis-1/Results'
  files = os.listdir(folder_path)
  file_paths = [os.path.join(folder_path, file) for file in files if file.endswith('.csv')]
  file_paths

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

  fig.savefig('filter.png', dpi=600)


