class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person(self):
        print("Name:", self.name)
        print("Age:", self.age)


class Doctor(Person):
    def __init__(self, name, age, specialization):
        super().__init__(name, age)
        self.specialization = specialization

    def display_doctor(self):
        print("Specialization:", self.specialization)


class Patient(Person):
    def __init__(self, name, age, disease):
        super().__init__(name, age)
        self.disease = disease

    def display_patient(self):
        print("Disease:", self.disease)


class Surgeon(Doctor, Patient):
    def __init__(self, name, age, specialization, disease, surgery_type):
        Doctor.__init__(self, name, age, specialization)
        self.disease = disease
        self.surgery_type = surgery_type

    def display_surgeon(self):
        self.display_person()
        self.display_doctor()
        print("Disease:", self.disease)
        print("Surgery Type:", self.surgery_type)


class MedicalResearcher(Doctor):
    def __init__(self, name, age, specialization, research_area):
        super().__init__(name, age, specialization)
        self.research_area = research_area

    def display_researcher(self):
        self.display_person()
        self.display_doctor()
        print("Research Area:", self.research_area)


# Create Surgeon object
s1 = Surgeon(
    "Dr. Kalyani",
    35,
    "General Surgery",
    "Appendicitis",
    "Appendix Surgery"
)

# Create MedicalResearcher object
r1 = MedicalResearcher(
    "Dr. Rahul",
    40,
    "Medicine",
    "Cancer Research"
)

print("----- Surgeon -----")
s1.display_surgeon()

print("\n----- Medical Researcher -----")
r1.display_researcher()