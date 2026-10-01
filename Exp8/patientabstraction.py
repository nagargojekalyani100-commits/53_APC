from abc import ABC, abstractmethod


class Patient(ABC):

    @abstractmethod
    def calculate_bill(self):
        pass

    @abstractmethod
    def treatment(self):
        pass


class InPatient(Patient):
    def calculate_bill(self):
        print("In-Patient Bill: ₹5000")

    def treatment(self):
        print("In-Patient: Hospital admission and regular treatment")


class OutPatient(Patient):
    def calculate_bill(self):
        print("Out-Patient Bill: ₹1000")

    def treatment(self):
        print("Out-Patient: Consultation and basic treatment")


class EmergencyPatient(Patient):
    def calculate_bill(self):
        print("Emergency Patient Bill: ₹8000")

    def treatment(self):
        print("Emergency Patient: Immediate emergency treatment")


# Create objects
in_patient = InPatient()
out_patient = OutPatient()
emergency_patient = EmergencyPatient()

# Store objects in a list
patients = [in_patient, out_patient, emergency_patient]

# Display details
for patient in patients:
    patient.treatment()
    patient.calculate_bill()
    print()