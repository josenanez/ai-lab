# /Users/jose/Projects/JoseNanez/ai-lab/data/synthetic/banking/faker_customers/generate_faker_customers.py
import pandas as pd
from faker import Faker
import os

faker = Faker()
data = []

for _ in range(1000):  # Puedes ajustar el tamaño
    data.append({
        "customer_id": faker.uuid4(),
        "name": faker.name(),
        "email": faker.email(),
        "phone": faker.phone_number(),
        "address": faker.address().replace("\n", ", "),
        "account_number": faker.bban(),
        "balance": round(faker.pyfloat(left_digits=5, right_digits=2, positive=True), 2)
    })

df = pd.DataFrame(data)

output_path = os.path.join(os.path.dirname(__file__), "faker_customers.csv")
df.to_csv(output_path, index=False)
print(f"✅ Saved: {output_path}")
