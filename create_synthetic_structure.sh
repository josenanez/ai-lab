#!/bin/bash

# Ruta base
BASE_DIR="/Users/jose/Projects/JoseNanez/ai-lab/data/synthetic"

# Lista completa en formato "industria/subcarpeta"
FOLDERS=(
  "banking/ctgan_generated"
  "banking/faker_customers"
  "banking/anonymized_kpis"
  "insurance/ctgan_claims"
  "insurance/faker_policyholders"
  "insurance/anonymized_risk_metrics"
  "healthcare/ctgan_patients"
  "healthcare/faker_profiles"
  "healthcare/anonymized_clinical_data"
  "government/ctgan_subsidies"
  "government/faker_identities"
  "government/anonymized_public_data"
  "legal/faker_contracts"
  "legal/ctgan_cases"
  "legal/anonymized_documents"
  "general/diffusers_images"
  "general/mixed_tabular"
)

# Crear estructura
echo "📁 Creating synthetic data folders under $BASE_DIR"
for folder in "${FOLDERS[@]}"; do
  FULL_PATH="$BASE_DIR/$folder"
  mkdir -p "$FULL_PATH"
  echo "✅ Created: $FULL_PATH"
done

# Agregar a .gitignore si no está
GITIGNORE_FILE="/Users/jose/Projects/JoseNanez/ai-lab/.gitignore"
if ! grep -q "/data/synthetic/" "$GITIGNORE_FILE"; then
  echo -e "\n# Ignore synthetic data\n/data/synthetic/" >> "$GITIGNORE_FILE"
  echo "🛡️  Updated .gitignore to exclude /data/synthetic/"
else
  echo "ℹ️  .gitignore already excludes /data/synthetic/"
fi
