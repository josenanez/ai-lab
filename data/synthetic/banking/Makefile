# ai-lab/data/synthetic/banking/Makefile

all: faker ctgan kpis

faker:
	python faker_customers/generate_faker_customers.py

ctgan:
	python ctgan_generated/generate_ctgan_data.py

kpis:
	python anonymized_kpis/generate_anonymized_kpis.py
