from sklearn.linear_model import LogisticRegression
import pickle
import pandas as pd


def model(dbt, fal):
    # Set the environment
    dbt.config({"fal_environment": "scikit"})

    # Load the dataset
    df = dbt.ref("raw_iris_train")
    X = df[["sepal.length", "sepal.width", "petal.length", "petal.width"]]
    y = df["variety"]

    # Create and train the model
    logisticRegr = LogisticRegression()
    logisticRegr.fit(X, y)

    # Store the model in another table
    s = pickle.dumps(logisticRegr)
    df = pd.DataFrame([s], columns=["pickled_model"])
    return df
