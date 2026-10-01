class Distance:
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    # Overload + operator
    def __add__(self, other):
        total_feet = self.feet + other.feet
        total_inches = self.inches + other.inches

        # Normalize inches
        if total_inches >= 12:
            total_feet += total_inches // 12
            total_inches = total_inches % 12

        return Distance(total_feet, total_inches)

    def display(self):
        print("Distance =", self.feet, "feet", self.inches, "inches")


# Create objects
d1 = Distance(5, 8)
d2 = Distance(4, 7)

# Add two distances
d3 = d1 + d2

# Display result
d3.display()