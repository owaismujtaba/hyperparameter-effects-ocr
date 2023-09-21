from models import model_3_4,  model_7_4, model_5_4, model_7_4, model_9_4, model_11_4
from models import model_3_1, model_3_2, model_3_3, model_3_5, model_3_7, model_3_9
from trainer import trainner, trainner_expand

def run():
  '''
  model = model_3_4()
  trainner(model, '/3_4.csv')
 
  model = model_5_4()
  trainner(model, '/5_4.csv')
  model = model_7_4()
  trainner(model, '/7_4.csv')
  
  model = model_9_4()
  trainner(model, '/9_4.csv')
  
  model = model_11_4()
  trainner_expand(model, '/11_4.csv')
  '''
  model = model_3_1()
  trainner(model, '/3_1.csv')
  '''
  model = model_3_2()
  trainner_expand(model, '/3_2.csv')

  model = model_3_3()
  trainner_expand(model, '/3_3.csv')

  model = model_3_5()
  trainner_expand(model, '/3_5.csv')

  model = model_3_7()
  trainner_expand(model, '/3_7.csv')

  model = model_3_9()
  trainner_expand(model, '/3_9.csv')
  '''


  
run()