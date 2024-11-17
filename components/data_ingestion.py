import pandas as pd
import sys
from sklearn.model_selection import train_test_split
from Source.exception import CustomException
from Source.logger import logging
from components.data_transformation import datatransformation

class data_ingestion:
    def data_ingestion_func(self):
        try:
            df = pd.read_csv('data/stud.csv')
            logging.info('Data Read Successfully')
            x = df.drop(['math_score'],axis=1)
            y = df['math_score']
            x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.23,random_state=42)
            logging.info('Data splitting successfully')
            x_train.to_csv('data/x_train.csv')
            x_test.to_csv('data/x_test.csv')
            y_train.to_csv('data/y_train.csv')
            y_test.to_csv('data/y_test.csv')
            logging.info('Splitted data has been stored successfully in Data folder')
            return "Data ingestion succcessful."
        except Exception as e:
            CustomException(e,sys)

if __name__=='__main__':
    doc = data_ingestion()
    dot = datatransformation()
    doc_ingestion_func = doc.data_ingestion_func()
    x_train_preprocessed, x_test_preprocessed = dot.data_transformation_func()
    print(doc_ingestion_func)
    


