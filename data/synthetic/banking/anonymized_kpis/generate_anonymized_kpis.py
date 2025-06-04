import pandas as pd
import numpy as np
import os

# Simulación simple con ruido agregado
np.random.seed(42)

kpis = {
    "customer_id": [f"ID-{i}" for i in range(1, 501)],
    "monthly_income": np.random.normal(3000, 500, 500),
    "loan_amount": np.random.normal(10000, 2500, 500),
    "credit_score": np.random.randint(400, 850, 500),
    "products_held": np.random.randint(1, 5, 500)
}

df = pd.DataFrame(kpis)

output_file = os.path.join(os.path.dirname(__file__), "anonymized_kpis.csv")
df.to_csv(output_file, index=False)
print(f"✅ Anonymized KPIs saved to: {output_file}")
