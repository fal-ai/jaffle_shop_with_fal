import pickle
import pandas as pd


def model(dbt, fal):
    # Set the environment
    dbt.config({"fal_environment": "scikit"})

    # Get the serialized model
    logistic_regr_df = dbt.ref("classification_model")
    pickled_model = logistic_regr_df.iloc[0]["pickled_model"]
    logistic_regr = pickle.loads(pickled_model)

    # Run predictions against a dataframe
    predictions = logistic_regr.predict(dbt.ref("raw_iris_test"))

    df = pd.DataFrame(predictions, columns=["outputs"])
    return df
