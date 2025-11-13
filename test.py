# test.py
import pytest
from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib
import os

MODEL_PATH = 'model.pkl'

def test_model_accuracy():
    """
    Tests the accuracy of a sample machine learning model.
    """
    # 1. Load the sample data
    cancer = datasets.load_breast_cancer()
    X, y = cancer.data, cancer.target
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # 2. Load pre-trained model (or train a dummy one if it doesn't exist)
    if not os.path.exists(MODEL_PATH):
        # In a real pipeline, the model should be a pre-built artifact 
        # from a previous "train" stage.
        model = LogisticRegression(max_iter=1000)
        model.fit(X_train, y_train)
        joblib.dump(model, MODEL_PATH) 
    else:
        model = joblib.load(MODEL_PATH)

    # 3. Make predictions and evaluate
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)

    # 4. Assert a minimum acceptable accuracy threshold
    assert accuracy > 0.90, f"Model accuracy is too low: {accuracy}"

if __name__ == "__main__":
    # Allows local execution with `python test.py`
    pytest.main([__file__])
