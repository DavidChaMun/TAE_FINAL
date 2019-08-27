class neural_network_mod():

    scaler =None
    model = None
    
    def __init__(self):
        from sklearn.externals import joblib
        from keras.models import load_model
        from sklearn.preprocessing import MinMaxScaler
        #self.scaler = joblib.load('scaler.save')
        self.model = load_model('best_neural_network_ever.h5')

ob = neural_network_mod()
from sklearn.externals import joblib
temp = joblib.load('scaler.save')
print(type(temp))

