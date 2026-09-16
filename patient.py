import csv

# Create a Patient class to store patient demographic and protein data
class Patient:
    all_patients = []

    # Initialize each patient with their demographic, clinical, and protein attributes
    def __init__(self, donor_id: str, age_at_death: float, sex: str,
             cognitive_status: str, apoe_genotype: str, thal: str,
             braak: str, abeta40: float, abeta42: float,
             ttau: float, ptau: float):

        self.donor_id = donor_id
        self.age_at_death = age_at_death
        self.sex = sex
        self.cognitive_status = cognitive_status
        self.apoe_genotype = apoe_genotype
        self.thal = thal
        self.braak = braak
        self.abeta40 = abeta40
        self.abeta42 = abeta42
        self.ttau = ttau
        self.ptau = ptau

        Patient.all_patients.append(self)

    # Represent each patient with identifying and demographic information
    def __repr__(self):
        return f"{self.donor_id}: {self.sex}, Age {self.age_at_death}, {self.cognitive_status}"

    # Create Patient objects from each row of the CSV file
    @classmethod
    def instantiate_from_csv(cls, filename):
        with open(filename, encoding="utf8") as f:
            reader = csv.DictReader(f)

            for row in reader:
                cls(
                donor_id=row["Donor ID"],
                age_at_death=float(row["Age at Death"]),
                sex=row["Sex"],
                cognitive_status=row["Cognitive Status"],
                apoe_genotype=row["APOE Genotype"],
                thal=row["Thal"],
                braak=row["Braak"],
                abeta40=float(row["ABeta40 pg/ug"]),
                abeta42=float(row["ABeta42 pg/ug"]),
                ttau=float(row["tTAU pg/ug"]),
                ptau=float(row["pTAU pg/ug"])
            )

    # Filter patients based on selected attributes
    @classmethod
    def filter(cls, list, sex: str = "any", cognitive_status: str = "any"):
        all_patients = list
        remove_list = []

        attr_list = (
            sex,
            cognitive_status
        )

        attr_name = (
            "sex",
            "cognitive_status"
        )

        for attr in range(len(attr_list)):
            if attr_list[attr] != "any":
                for patient in all_patients:
                    if getattr(patient, attr_name[attr]) != attr_list[attr]:
                        remove_list.append(patient)

                all_patients = [patient for patient in all_patients if patient not in remove_list]
                remove_list.clear()

        return all_patients