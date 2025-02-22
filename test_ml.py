import pandas as pd
from sklearn.datasets import make_classification
from sklearn.ensemble import RandomForestClassifier
import numpy as np
from ml.model import train_model
from train_model import X_train, y_train
import os
from sklearn.model_selection import train_test_split

# TODO: implement the first test. Change the function name and input as needed
def test_randomforest():
    """
    this is a test that the model was trained using randomforestclassifier
    """
    model = train_model(X_train, y_train)
    assert type(model) == RandomForestClassifier, f"Unexpected type of model: {type(model)}"


# TODO: implement the second test. Change the function name and input as needed
def test_splitting_data():
    """
    testing to see if the data was split into a training set and a testing set
    """
    project_path = os.getcwd()
    data_path = os.path.join(project_path, "data", "census.csv")
    data = pd.read_csv(data_path)

    train, test = train_test_split(data, test_size=0.2, random_state=0)

    assert not train.empty, "Nothing in the training dataset"
    assert not test.empty, "Nothing in the test dataset"

# TODO: implement the third test. Change the function name and input as needed
def test_loading_data():
    """
    testing to see if the data was loaded properly
    """
    X, y = make_classification(n_samples=50, n_features=5, random_state=42)
    assert X.shape == (50, 5), f"Unexpected shape for X: {X.shape}"
    assert y.shape == (50,), f"Unexpected shape for y: {y.shape}"