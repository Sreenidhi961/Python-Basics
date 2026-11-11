import numpy as np
import matplotlib.pyplot as plt

# =========================================================
# CONJUGATE GRADIENT METHOD
# UCI REAL ESTATE VALUATION DATASET
# =========================================================

# ---------------------------------------------------------
# 1. LOAD DATA
# ---------------------------------------------------------

data = np.genfromtxt(
    "real_estate.csv",
    delimiter=",",
    skip_header=1
)

# ---------------------------------------------------------
# 2. SELECT FEATURES AND TARGET
# ---------------------------------------------------------

# Column 0  = No. -> ignored
# Columns 1-6 = X1 to X6 -> input features
# Column 7  = Y -> house price

X = data[:, 1:7]
y = data[:, 7]

# ---------------------------------------------------------
# 3. STANDARDIZE FEATURES
# ---------------------------------------------------------

X_mean = np.mean(X, axis=0)
X_std = np.std(X, axis=0)

X = (X - X_mean) / X_std

# ---------------------------------------------------------
# 4. ADD INTERCEPT
# ---------------------------------------------------------

X = np.column_stack((np.ones(len(X)), X))

# ---------------------------------------------------------
# 5. FORM THE LINEAR SYSTEM
# ---------------------------------------------------------

# Linear regression:
#
# A w = b
#
# A = X^T X / n
# b = X^T y / n

n = len(y)

A = (X.T @ X) / n
b = (X.T @ y) / n

# ---------------------------------------------------------
# 6. INITIALIZE
# ---------------------------------------------------------

w = np.zeros(X.shape[1])

# Residual
r = b - A @ w

# Initial search direction
p = r.copy()

mse_history = []

# ---------------------------------------------------------
# 7. CONJUGATE GRADIENT
# ---------------------------------------------------------

max_iterations = X.shape[1]

for i in range(max_iterations):

    # A multiplied by search direction
    Ap = A @ p

    # Step size
    alpha = (r @ r) / (p @ Ap)

    # Update weights
    w = w + alpha * p

    # Update residual
    r_new = r - alpha * Ap

    # Calculate predictions
    y_pred = X @ w

    # Calculate MSE
    mse = np.mean((y_pred - y) ** 2)

    mse_history.append(mse)

    # Check convergence
    if np.linalg.norm(r_new) < 1e-10:
        break

    # Calculate beta
    beta = (r_new @ r_new) / (r @ r)

    # New conjugate direction
    p = r_new + beta * p

    # Update residual
    r = r_new

# ---------------------------------------------------------
# 8. DISPLAY RESULTS
# ---------------------------------------------------------

print()
print("==========================================")
print("       CONJUGATE GRADIENT METHOD")
print("==========================================")

print("Number of data points :", len(y))
print("Number of features    :", 6)
print("Number of iterations  :", len(mse_history))

print()
print("Final MSE :", mse_history[-1])

print()
print("Final weights:")

for i in range(len(w)):
    print("w" + str(i), "=", w[i])

# ---------------------------------------------------------
# 9. PLOT CONVERGENCE
# ---------------------------------------------------------

plt.figure(figsize=(8, 5))

plt.plot(
    range(1, len(mse_history) + 1),
    mse_history,
    marker="o"
)

plt.xlabel("Iterations")
plt.ylabel("Mean Squared Error")

plt.title("Conjugate Gradient Convergence")

plt.grid(True)

plt.show()
