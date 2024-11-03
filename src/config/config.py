import os
from pathlib import Path

class Config:
    RANDOM_STATE = 42
    
    # Paths
    ROOT_DIR = Path(__file__).parent.parent.parent
    DATA_DIR = os.path.join(ROOT_DIR, "data")
    RAW_DATA_DIR = os.path.join(DATA_DIR, "raw")
    PROCESSED_DATA_DIR = os.path.join(DATA_DIR, "processed")
    MODEL_DIR = os.path.join(ROOT_DIR, "models")
    LOG_DIR = os.path.join(ROOT_DIR, "logs")
    
    # Data
    RAW_DATA_FILE = os.path.join(RAW_DATA_DIR, "house_prices.csv")
    TRAIN_DATA_FILE = os.path.join(PROCESSED_DATA_DIR, "train.csv")
    TEST_DATA_FILE = os.path.join(PROCESSED_DATA_DIR, "test.csv")
    
    # Model parameters
    TARGET_COLUMN = "SalePrice"
    TEST_SIZE = 0.2
    
    # MLflow settings
    MLFLOW_TRACKING_URI = "file:./mlruns"
    EXPERIMENT_NAME = "house_price_prediction"
    
    # Model hyperparameters search space
    MODEL_PARAMS = {
        'xgboost': {
            'n_estimators': [100, 200, 300],
            'max_depth': [3, 4, 5],
            'learning_rate': [0.01, 0.1, 0.3],
            'subsample': [0.8, 0.9, 1.0]
        },
        'lightgbm': {
            'n_estimators': [100, 200, 300],
            'max_depth': [3, 4, 5],
            'learning_rate': [0.01, 0.1, 0.3],
            'subsample': [0.8, 0.9, 1.0]
        }
    }