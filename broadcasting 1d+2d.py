import numpy as np
marks = np.array([
    [78, 85, 92, 70],
    [65, 72, 68, 80],
    [90, 88, 95, 85],
    [55, 60, 58, 62],
    [82, 79, 87, 91]
])
bonus = np.array([5, 3, 4, 2])
new_marks = marks + bonus
print("Marks after subject-wise bonus:")
print(new_marks)
