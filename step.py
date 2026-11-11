import numpy as np
import matplotlib.pyplot as plt

# =====================================================
# 1. LOAD THE DATASET
# =====================================================

data = np.genfromtxt(
    "real_estate.csv",
    delimiter=",",
    skip_header=1
)

# =====================================================
# 2. SELECT INPUT FEATURES AND TARGET
# =====================================================

# Column 0 = No. (row number) -> NOT used
# Columns 1 to 6 = X1, X2, X3, X4, X5, X6
# Column 7 = Y (house price)

X = data[:, 1:7]
y = data[:, 7]

# =====================================================
# 3. STANDARDIZE THE FEATURES
# =====================================================

mean = np.mean(X, axis=0)
std = np.std(X, axis=0)

X = (X - mean) / std

# =====================================================
# 4. ADD INTERCEPT COLUMN
# =====================================================

# Adds a column of 1s for the intercept
X = np.column_stack((np.ones(X.shape[0]), X))

# =====================================================
# 5. INITIALIZE WEIGHTS
# =====================================================

w = np.zeros(X.shape[1])

# =====================================================
# 6. SET PARAMETERS
# =====================================================

learning_rate = 0.01
iterations = 1000

mse_history = []

# =====================================================
# 7. STEEPEST DESCENT ALGORITHM
# =====================================================

for i in range(iterations):

    # Calculate predictions
    y_pred = X @ w

    # Calculate error
    error = y_pred - y

    # Calculate gradient
    gradient = (X.T @ error) / len(y)

    # Update weights
    w = w - learning_rate * gradient

    # Calculate new predictions
    y_pred = X @ w

    # Calculate Mean Squared Error
    mse = np.mean((y_pred - y) ** 2)

    # Store MSE
    mse_history.append(mse)

# =====================================================
# 8. DISPLAY RESULTS
# =====================================================

print("\n======================================")
print("       STEEPEST DESCENT METHOD")
print("======================================")

print("\nNumber of data points:", len(y))

print("Number of features:", X.shape[1] - 1)

print("Learning rate:", learning_rate)

print("Number of iterations:", iterations)

print("\nFinal MSE:", mse_history[-1])

print("\nFinal Weights:")

for i in range(len(w)):
    print("w" + str(i), "=", w[i])

# =====================================================
# 9. PLOT CONVERGENCE
# =====================================================

plt.figure(figsize=(8, 5))

plt.plot(mse_history)

plt.xlabel("Iterations")

plt.ylabel("Mean Squared Error")

plt.title("Steepest Descent Convergence")

plt.grid(True)

plt.show()
