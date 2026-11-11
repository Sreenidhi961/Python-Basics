import numpy as np
marks = np.array([
    [78, 85, 92, 70],
    [65, 72, 68, 80],
    [90, 88, 95, 85],
    [55, 60, 58, 62],
    [82, 79, 87, 91]
])
adjustment = np.array([-2, 0, 3, -1, 1])
adjustment = adjustment[:, np.newaxis]
new_marks = marks + adjustment
print("Marks after student-wise adjustment:")
print(new_marks)
