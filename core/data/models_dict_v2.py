model_dict = {
    "cost": {
        "features_dict": {
            "MARITAL_STATUS": {
                "type": "categorical",
                "relativity": {"Not_Single": 0.9, "Single": 1.1},
            },
            "NUMBER_OF_CLAIMS_PAST_5YEARS": {
                "type": "continuous",
                "a": 0.10,
                "b": 0.97,
            },
            "NUMBER_OF_MINOR_CONVICTIONS_PAST_3YEARS": {
                "type": "continuous",
                "a": 0.05,
                "b": 0.99,
            },
            "DRIVER_AGE": {"type": "continuous", "a": -0.02, "b": 2.02},
            "VEHICLE_AGE": {"type": "continuous", "a": -0.02, "b": 1.14},
            "VEHICLE_PRICE": {
                "type": "continuous",
                "a": 0.000003,
                "b": 0.95,
            },
        },
        "base": 700,
        "min_pred": 50,
    },
    "pricing": {
        "features_dict": {
            "MARITAL_STATUS": {
                "type": "categorical",
                "relativity": {"Not_Single": 0.92, "Single": 1.08},
            },
            "NUMBER_OF_CLAIMS_PAST_5YEARS": {
                "type": "continuous",
                "a": 0.07,
                "b": 0.98,
            },
            "NUMBER_OF_MINOR_CONVICTIONS_PAST_3YEARS": {
                "type": "continuous",
                "a": 0.04,
                "b": 0.99,
            },
            "DRIVER_AGE": {"type": "continuous", "a": -0.015, "b": 1.77},
            "VEHICLE_AGE": {"type": "continuous", "a": -0.015, "b": 1.11},
            "VEHICLE_PRICE": {
                "type": "continuous",
                "a": 0.000002,
                "b": 0.965,
            },
        },
        "base": 1000,
        "min_pred": 50,
    },
}
