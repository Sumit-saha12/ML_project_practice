import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from Source.exception import CustomException
from Source.logger import logging
import pickle
# from components.data_ingestion import data_ingestion
import sys

class datatransformation():
    def data_transformation_func(self):
        try:
            x_train = pd.read_csv('data/x_train.csv')
            x_test = pd.read_csv('data/x_test.csv')
            y_train = pd.read_csv('data/y_train.csv')
            y_test = pd.read_csv('data/y_test.csv')

            num_features = ['reading_score','writing_score']
            cat_features = ['gender',
                            'race_ethnicity',
                            'parental_level_of_education',
                            'lunch',
                            'test_preparation_course']
            
            num_pipeline = Pipeline(
                steps=[
                    ('Imputer',SimpleImputer(strategy='median')),
                    ('Scaling',StandardScaler())
                ]
            )

            cat_pipeline = Pipeline(
                steps=[
                    ('imputer',SimpleImputer(strategy='most_frequency')),
                    ('OneHot',OneHotEncoder()),
                    ('Scaling',StandardScaler(with_mean=False))
                ]
            )

            preprocessor = ColumnTransformer(
                [
                    ('Num_Preprocessing',num_pipeline,num_features),
                    ('Cat_preprocessing',cat_pipeline,cat_features)
                ]
            )
            logging.info('Data is scaled')
            x_train_preprocessed = preprocessor.fit_transform(x_train)
            x_test_preprocessed = preprocessor.transform(x_test)
            logging.info('Scaled data is saved')

            pickle.dump(preprocessor,open('models/preprocessing.pkl','wb'))
            logging.info('Preprocessing pkl file is saved')

            return (x_train_preprocessed)

        except Exception as e:
            CustomException(e,sys)
            
if __name__=='__main__':
    dot = datatransformation()
    print(dot.data_transformation_func())

    