import pandas as pd
import numpy as np


class Models:
    def __init__(self, model_dict):
        self.cost_dict = model_dict["cost"]
        self.pricing_dict = model_dict["pricing"]
        # self.demand_dict = model_dict["demand"]

    def calculate_cost(self, df):
        """Expected cost from insurance claims."""
        return self._calculate(self.cost_dict, df)

    def calculate_pricing(self, df):
        """Dummy insurance pricing for the sake of the exercice."""
        return self._calculate(self.pricing_dict, df)

    def calculate_profit(self, cost, pricing, variable_expense=0.3):
        """Profit calculation from the insurer's point of view."""
        return pricing * (1 - variable_expense) - cost

    def _calculate(self, dict, df):
        val = np.full(shape=len(df.index), fill_value=dict["base"])

        feature_dict = dict["features_dict"]

        for feature, val_dict in feature_dict.items():
            if val_dict["type"] == "categorical":
                relativity = df[feature].map(val_dict["relativity"])
            elif val_dict["type"] == "continuous":
                relativity = val_dict["a"] * df[feature] + val_dict["b"]
            val = val * np.where(df[feature].notna(), relativity, 1.0)

        return pd.Series(np.maximum(val, dict["min_pred"]))
