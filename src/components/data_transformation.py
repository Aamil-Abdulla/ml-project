import os
import sys
import numpy as np 
import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler , OneHotEncoder
from src.utils import save_object
from src.logger import logging
from src.exception import CustomException
from src.utils import save_object
from dataclasses import dataclass

@dataclass
class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join("artifacts", "preprocessor.pkl")

class DataTransformation :
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()
    
    def get_data_transformer_obj(self):
        try:
            cat_columns = [
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course",
            ]

            num_columns = [
            "writing_score",
            "reading_score"
            ]
            num_pipeline = Pipeline(
            steps = [
                ("imputer",SimpleImputer(strategy="median")),
                ("scaler",StandardScaler())
            ]
            )
            cat_pipeline = Pipeline(
                steps = [
                    ("imputer",SimpleImputer(strategy = "most_frequent")),
                    ("one_hot_encoder",OneHotEncoder()),
                    ("scaler",StandardScaler())
                ]
            )
            logging.info(f"Numerical coloumns{num_columns} and Categorical Columns{cat_columns}")
            preprocessor = ColumnTransformer(
                [
                    ("num_pipeline", num_pipeline, num_columns),
                    ("cat_pipeline", cat_pipeline , cat_columns)
                ]
            )
            return preprocessor
    
    
        except Exception as e:
            raise CustomException(e,sys)

    def Initiate_Data_Transformation(self,train_path,test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            logging.info("read train data and test data")
            preprocessor_obj = self.get_data_transformer_obj()
            target_column_name = "math_score"
            numerical_columns = ["write_score"]
            input_feature_train_df= train_df.drop(columns=[target_column_name ] , axis = 1)
            target_feature_train_df=train_df[target_column_name]
            input_feature_test_df= test_df.drop(columns=[target_column_name ] , axis = 1)
            target_feature_test_df=test_df[target_column_name]

            input_feature_train_arr = preprocessor_obj.fit_transform(input_feature_train_df)
            input_feature_test_arr = preprocessor_obj.transform(input_feature_test_df)

            train_arr = np.c_[
                input_feature_train_arr, np.array(target_feature_train_df)

            ]
            test_arr = np.c_[
                input_feature_test_arr, np.array(target_feature_test_df)
            ]
            logging.info(f"Saved Preprocessing object")
            save_object(
                file_path = self.data_transformation_config.preprocessor_obj_file_path,obj = preprocessor_obj
            )
            return ( 
                train_arr,
                test_arr, 
                self.data_transformation_config.preprocessor_obj_file_path
            )

        except:
            pass

        






