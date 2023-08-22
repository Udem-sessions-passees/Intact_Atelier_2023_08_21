from Intact_Atelier_2023_08_21.code.data.models import Models
from Intact_Atelier_2023_08_21.code.data.models_dict_v2 import model_dict
from Intact_Atelier_2023_08_21.code.data.generate_synthetic_df import generate_synthetic_df

# Create synthetic dataframe
df = generate_synthetic_df(10, 0)

# Instantiate an object from the class "Models"
models = Models(model_dict)

# Calculate the cost and price
cost = models.calculate_cost(df)
pricing = models.calculate_pricing(df)

# Calculate the profit on the synthetic dataframe
df["profit"] = models.calculate_profit(cost, pricing)
