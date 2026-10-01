# Base class
class Report:
    def generate(self):
        print("Generating report")


# PDF Report
class PDFReport(Report):
    def generate(self):
        print("Generating PDF Report")


# Excel Report
class ExcelReport(Report):
    def generate(self):
        print("Generating Excel Report")


# HTML Report
class HTMLReport(Report):
    def generate(self):
        print("Generating HTML Report")


# Function that accepts any report object
def generate_report(report):
    report.generate()


# Create objects
pdf = PDFReport()
excel = ExcelReport()
html = HTMLReport()

# Calling the function with different objects
generate_report(pdf)
generate_report(excel)
generate_report(html)