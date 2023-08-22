import pandas as pd
import numpy as np

def generate_synthetic_df(n = 100, seed = 0):

    df = pd.DataFrame()

    np.random.seed(seed)

    # Continuous
    df["ANNUAL_KILOMETERS_QUANTITY"] = np.clip(np.random.normal(loc=12000, scale=7000, size=n), 0, 100000).astype(int)
    df["DRIVER_AGE"] = np.clip(np.random.normal(loc=50, scale=17, size=n), 15, 120).astype(int)
    df["VEHICLE_AGE"] = np.clip(np.random.normal(loc=7, scale=6, size=n), 0, 50).astype(int)
    df["VEHICLE_PRICE"] = np.clip(np.random.normal(loc=15000, scale=11000, size=n), 100, 500000).astype(int)
    # Categorical
    df["DRIVER_TRAINING_INDICATOR_PRINCIPAL"] = np.random.choice([False, True], size=n, p=[0.87, 0.13])
    df["LEASED_VEHICLE_INDICATOR"] = np.random.choice([False, True], size=n, p=[0.94, 0.06])
    df["MARITAL_STATUS"] = np.random.choice(["Not_Single", "Single"], size=n, p=[0.63, 0.37])
    df["NUMBER_OF_CLAIMS_PAST_5YEARS"] = np.random.choice([0, 1, 2, 3], size=n, p=[0.75, 0.15, 0.08, 0.02])
    df["NUMBER_OF_MINOR_CONVICTIONS_PAST_3YEARS"] = np.random.choice([0, 1, 2, 3], size=n, p=[0.80, 0.15, 0.04, 0.01])

    return df
