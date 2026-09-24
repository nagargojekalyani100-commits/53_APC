class Patient:
    def __init__(self, patient_id, name, age, disease, consultation_fee):
        self.patient_id = patient_id
        self.name = name
        self.age = age
        self.disease = disease
        self.consultation_fee = consultation_fee

    def display_information(self):
        print("Patient ID:", self.patient_id)
        print("Name:", self.name)
        print("Age:", self.age)
        print("Disease:", self.disease)
        print("Consultation Fee:", self.consultation_fee)

    def calculate_total_bill(self):
        return self.consultation_fee


p1 = Patient(101, "Kalyani", 20, "Fever", 500)

p1.display_information()
print("Total Bill:", p1.calculate_total_bill())