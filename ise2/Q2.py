# create a student marks array and use boolean indexing to display students scoring above the average
import numpy as np

# Student marks
marks = np.array([65, 78, 92, 55, 88, 72, 95, 60])

#  average
average = np.mean(marks)

# here we use the boolean indexing to display the students scoring above average
above_average = marks[marks > average]

print("Marks:", marks)
print("Average:", average)
print("Students scoring above average:", above_average)