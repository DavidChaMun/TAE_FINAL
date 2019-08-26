import pandas as pd 
from sklearn import preprocessing
from sklearn.tree import DecisionTreeClassifier 
from sklearn.tree import DecisionTreeRegressor 
from sklearn import metrics 
from sklearn.ensemble.forest import RandomForestClassifier
from sklearn.ensemble.forest import RandomForestRegressor
import os
import re

class TAERandomForestClassifier(object):
    lab_encoders = {}
    dummy_encoder = None
    rfc_model = None
    n_estimators = 1300
    max_features = 5
    
    def encode_fit(self, cat_data):
        #Encodes string to numeric labels
        tdc_set_encoded = cat_data.copy(deep=True)
        for cn in cat_data.columns:
            self.lab_encoders[cn] = preprocessing.LabelEncoder()
            self.lab_encoders[cn].fit(cat_data[str(cn)])
            tdc_set_encoded[str(cn)] = self.lab_encoders[cn].transform(cat_data[str(cn)])
        
        #Encodes to dummy dataset
        self.dummy_encoder = preprocessing.OneHotEncoder(categories="auto")
        self.dummy_encoder.fit(tdc_set_encoded[cat_data.columns])
        
        #print(len(self.dummy_encoder.get_feature_names()))
        
        encoded_cat_data = pd.DataFrame(data=self.dummy_encoder.transform(tdc_set_encoded).todense(), columns=self.dummy_encoder.get_feature_names())
        return encoded_cat_data
    
    def encode(self, cat_data):
        for cn in cat_data.columns:
              cat_data[str(cn)] = self.lab_encoders[cn].transform(cat_data[str(cn)]) 
        
        
        #Encodes to dummy dataset
        encoded_cat_data = pd.DataFrame(data=self.dummy_encoder.transform(cat_data).todense(), columns=self.dummy_encoder.get_feature_names())    
        return encoded_cat_data       
    def fit(self, x_train, y_train, cat_cols, num_cols):
        #Separates dataset in categorical and numbers
        x_train_num = x_train[num_cols].copy(deep=True)
        x_train_cat = x_train[cat_cols].copy(deep=True)
        
        x_train_cat = self.encode_fit(x_train_cat)
        
        x_train_num.reset_index(drop=True, inplace=True)
        x_train_cat.reset_index(drop=True, inplace=True)
        
        f_x_train = pd.concat([x_train_num, x_train_cat], axis=1)

        self.rfc_model = RandomForestClassifier(n_estimators=self.n_estimators, criterion="entropy", max_features=self.max_features)
        self.rfc_model = self.rfc_model.fit(f_x_train, y_train)
        
    def predict(self, x_predict, cat_cols, num_cols):
        #Separates dataset in categorical and numbers
        x_predict_num = x_predict[num_cols].copy(deep=True)
        x_predict_cat = x_predict[cat_cols].copy(deep=True)
        
        x_predict_cat = self.encode(x_predict_cat)
        f_x_predict = pd.concat([x_predict_num, x_predict_cat], axis=1)
        y_pred = self.rfc_model.predict(f_x_predict)
        return y_pred
    
    def cal_conf_matrix(self, x_test, y_test, catego_columns, numeric_cols):
        y_pred = self.predict(x_test, catego_columns, numeric_cols)
        # [[VP, FP], [FN, VN]]
        print("Matriz de confusión:")
        print(metrics.confusion_matrix(y_test, y_pred))

        #Correr varias veces y ver como varia. Basado en el indice de jaccard
        print("Precisión:", metrics.accuracy_score(y_test, y_pred))