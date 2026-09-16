from patient import Patient
import numpy as np
import matplotlib.pyplot as plt

# Create Patient objects using the data from the CSV file
Patient.instantiate_from_csv("Metadata and Protein Data for Module 1.csv")

# Sort patients by age at death
sorted_patients = sorted(Patient.all_patients, key=lambda patient: patient.age_at_death)

# Print the sorted patients
for patient in sorted_patients:
    print(patient)

# Filter and print female patients with dementia
filtered_patients = Patient.filter(
    Patient.all_patients,
    sex="Female",
    cognitive_status="Dementia"
)

for patient in filtered_patients:
    print(patient)

# Compare mean ABeta42 levels between female and male patients
female_abeta42 = [patient.abeta42 for patient in Patient.all_patients if patient.sex == "Female"]
male_abeta42 = [patient.abeta42 for patient in Patient.all_patients if patient.sex == "Male"]

means = [np.mean(female_abeta42), np.mean(male_abeta42)]
standard_deviations = [np.std(female_abeta42), np.std(male_abeta42)]

plt.bar(["Female", "Male"], means, yerr=standard_deviations, capsize=5)
plt.xlabel("Sex")
plt.ylabel("ABeta42 (pg/ug)")
plt.title("Mean ABeta42 Levels by Sex")
plt.savefig("bar_graph.png")
plt.show()

# Compare ABeta40 and ABeta42 levels
abeta40 = [patient.abeta40 for patient in Patient.all_patients]
abeta42 = [patient.abeta42 for patient in Patient.all_patients]

plt.scatter(abeta40, abeta42)
plt.xlabel("ABeta40 (pg/ug)")
plt.ylabel("ABeta42 (pg/ug)")
plt.title("ABeta40 vs. ABeta42 Levels")
plt.savefig("scatter_plot.png")
plt.show()