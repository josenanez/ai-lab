from sdv.single_table import GaussianCopulaSynthesizer
from sdv.metadata import SingleTableMetadata
import pandas as pd
import os

# Cargar datos
input_file = os.path.join(os.path.dirname(__file__), "../faker_customers/faker_customers.csv")
df = pd.read_csv(input_file)[["balance"]]  # solo numérico

# Metadata
metadata = SingleTableMetadata()
metadata.detect_from_dataframe(data=df)

# Entrenar modelo
model = GaussianCopulaSynthesizer(metadata)
model.fit(df)

# Generar
synthetic_data = model.sample(1000)
output_file = os.path.join(os.path.dirname(__file__), "copula_customers.csv")
synthetic_data.to_csv(output_file, index=False)

print(f"✅ Copula synthetic data saved to: {output_file}")
