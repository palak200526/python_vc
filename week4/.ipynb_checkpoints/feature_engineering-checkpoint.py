import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin


class ChurnFeatureEngineer(BaseEstimator, TransformerMixin):

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.copy()

        X["Tenure Years"] = X["Tenure Months"] / 12

        X["Average Monthly Charge"] = (
            X["Total Charges"] /
            X["Tenure Months"].replace(0, np.nan)
        )

        service_columns = [
            "Phone Service",
            "Multiple Lines",
            "Online Security",
            "Online Backup",
            "Device Protection",
            "Tech Support",
            "Streaming TV",
            "Streaming Movies"
        ]

        available_services = [
            col for col in service_columns
            if col in X.columns
        ]

        X["Service Count"] = (
            X[available_services]
            .eq("Yes")
            .sum(axis=1)
        )

        X["Charge Tenure Interaction"] = (
            X["Monthly Charges"] * X["Tenure Months"]
        )

        return X