class neural_network_mod():

    scaler =None
    nn_model = None
    train_cols = ['age', 'fnlwgt', 'capital_gain', 'capital_loss', 'hours_per_week',
       'workclass_ Federal-gov', 'workclass_ Local-gov', 'workclass_ Private',
       'workclass_ Self-emp-inc', 'workclass_ Self-emp-not-inc',
       'workclass_ State-gov', 'workclass_ Without-pay', 'education_ 10th',
       'education_ 11th', 'education_ 12th', 'education_ 1st-4th',
       'education_ 5th-6th', 'education_ 7th-8th', 'education_ 9th',
       'education_ Assoc-acdm', 'education_ Assoc-voc', 'education_ Bachelors',
       'education_ Doctorate', 'education_ HS-grad', 'education_ Masters',
       'education_ Preschool', 'education_ Prof-school',
       'education_ Some-college', 'marital_status_ Divorced',
       'marital_status_ Never-married', 'marital_status_ Separated',
       'marital_status_ Widowed', 'marital_status_Married',
       'ocupation_ Adm-clerical', 'ocupation_ Armed-Forces',
       'ocupation_ Craft-repair', 'ocupation_ Exec-managerial',
       'ocupation_ Farming-fishing', 'ocupation_ Handlers-cleaners',
       'ocupation_ Machine-op-inspct', 'ocupation_ Other-service',
       'ocupation_ Priv-house-serv', 'ocupation_ Prof-specialty',
       'ocupation_ Protective-serv', 'ocupation_ Sales',
       'ocupation_ Tech-support', 'ocupation_ Transport-moving',
       'ethnicity_ Amer-Indian-Eskimo', 'ethnicity_ Asian-Pac-Islander',
       'ethnicity_ Black', 'ethnicity_ Other', 'ethnicity_ White',
       'gender_ Female', 'gender_ Male', 'native_country_ Mexico',
       'native_country_ United-States', 'native_country_other']
    catego_columns = ['education', 'workclass', 'marital_status', 
             'ethnicity','gender',
                  'native_country', 'ocupation']
    
    def __init__(self):
        from sklearn.externals import joblib
        from keras.models import load_model
        from sklearn.preprocessing import MinMaxScaler
        
        import numpy as np
        import pandas as pd
        import keras
        from keras.models import Sequential
        
        self.scaler = joblib.load('scaler.save')
        self.nn_model = load_model('my_model.h5')
        
    def predict(self, data):
      data = self.tidy_data(data)
      
      predictions = self.nn_model.predict(data)>0.5
      predictions=np.where(predictions==0, "<=50k", predictions)
      predictions=np.where(predictions=='True', ">50k", predictions)
      return(predictions)
      
    def tidy_data(self,data):
      
      #Transformamos variables object a categoricas
      for col in catego_columns:        
        data[col] = pd.Categorical(data[col])
      
      #Creamos variables dummies con las categoricas
      data_d=pd.get_dummies(data)
      
      #Rellenamos con las variables dummies
      missing_cols = set(self.train_cols) - set(data_d.columns)
      
      for c in missing_cols:
        data_d[c] = 0
        
      # Ensure the order of column in the test set is in the same order than in train set
      data_d = data_d[self.train_cols]
      
      #Escalamos los datos
      data_d = self.scaler.transform(data_d)    
      return(data_d)
      
 
