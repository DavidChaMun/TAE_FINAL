import pandas as pd
from joblib import load


class TAESupportVectorMachineClassifier(object):
    model = load("svm_model.joblib")
    dataset = pd.read_csv('./data/dataset_tae_final_no_na_mod.csv')
    category_columns = ['education', 'workclass', 'marital_status', 'ethnicity', 'gender', 'native_country',
                        'ocupation']

    @classmethod
    def fit(cls):
        print("El proceso de entrenamiento demora aproximadamente 45 minutos por lo que no esta permitido ejecutarlo")

    @classmethod
    def predict(cls, x_predict):
        cls.dataset.pop("income") if "income" in cls.dataset else None
        cls.dataset.append(x_predict)

        for column in cls.category_columns:
            cls.dataset[column] = pd.Categorical(cls.dataset[column])

        dummy_dataset = pd.get_dummies(cls.dataset)
        dummy_dataset["Unnamed"] = [_ for _ in range(len(dummy_dataset))]

        y_pred = cls.model.predict(dummy_dataset[-1:])
        return y_pred
