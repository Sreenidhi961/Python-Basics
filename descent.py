import numpy as np
import matplotlib.pyplot as plt

# ==========================================
# LOAD DATA
# ==========================================

data = np.genfromtxt(
    "real_estate.csv",
    delimiter=",",
    skip_header=1
)

# ==========================================
# SELECT FEATURES AND TARGET
# ==========================================

# Column 0 = No. (not used)
# Columns 1-6 = X1 to X6
# Column 7 = Y = house price

X = data[:, 1:7]
y = data[:, 7]

# ==========================================
# STANDARDIZE FEATURES
# ==========================================

X_mean = np.mean(X, axis=0)
X_std = np.std(X, axis=0)

X = (X - X_mean) / X_std

# ==========================================
# ADD INTERCEPT
# ==========================================

X = np.column_stack((np.ones(X.shape[0]), X))

# ==========================================
# INITIALIZE WEIGHTS
# ==========================================

w = np.zeros(X.shape[1])

# ==========================================
# PARAMETERS
# ==========================================

learning_rate = 0.01
iterations = 1000

mse_history = []

# ==========================================
# STEEPEST DESCENT
# ==========================================

for i in range(iterations):

    # Prediction
    y_pred = X @ w

    # Error
    error = y_pred - y

    # Gradient
    gradient = (X.T @ error) / len(y)

    # Update weights
    w = w - learning_rate * gradient

    # New prediction
    y_pred = X @ w

    # Mean Squared Error
    mse = np.mean((y_pred - y) ** 2)

    mse_history.append(mse)

# ==========================================
# RESULTS
# ==========================================

print()
print("======================================")
print("       STEEPEST DESCENT METHOD")
print("======================================")

print("Number of data points:", len(y))
print("Number of features:", X.shape[1] - 1)
print("Learning rate:", learning_rate)
print("Iterations:", iterations)

print()
print("Final MSE:", mse_history[-1])

print()
print("Final Weights:")

for i in range(len(w)):
    print("w" + str(i), "=", w[i])

# ==========================================
# CONVERGENCE GRAPH
# ==========================================

plt.figure(figsize=(8, 5))

plt.plot(mse_history)

plt.xlabel("Iterations")
plt.ylabel("Mean Squared Error")

plt.title("Steepest Descent Convergence")

plt.grid(True)

plt.show()
