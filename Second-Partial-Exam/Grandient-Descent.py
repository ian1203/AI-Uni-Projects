import numpy as np
import matplotlib.pyplot as plt


# Function to compute f(x) = x^2 + 4x + 5
def f(x):
    return x ** 2 + 4 * x + 5


# Derivative of f(x) = 2x + 4
def df(x):
    return 2 * x + 4


# Gradient descent implementation
def gradient_descent(x0, alpha, iterations):
    x_values = [x0]
    f_values = [f(x0)]

    x = x0

    for i in range(iterations):
        # Update x using the gradient and learning rate
        x = x - alpha * df(x)
        x_values.append(x)
        f_values.append(f(x))

        print(f"Iteration {i + 1}: x = {x:.6f}, f(x) = {f(x):.6f}")

    return x_values, f_values


# Parameters
x0 = 1  # Initial value
alpha = 0.1  # Learning rate
iterations = 20  # Number of iterations

# Run gradient descent
x_values, f_values = gradient_descent(x0, alpha, iterations)

# Plot the function and the points
x_range = np.linspace(-5, 3, 100)
y_range = [f(x) for x in x_range]

plt.figure(figsize=(10, 6))
plt.plot(x_range, y_range, 'b-', label='f(x) = x^2 + 4x + 5')
plt.scatter(x_values, f_values, color='red', label='Gradient Descent Steps')
plt.plot(x_values, f_values, 'r--')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Gradient Descent Optimization')
plt.legend()
plt.grid(True)
plt.savefig('gradient_descent.png')
plt.show()

# Print the final result
print(f"\nFinal result after {iterations} iterations:")
print(f"x = {x_values[-1]:.6f}")
print(f"f(x) = {f_values[-1]:.6f}")

# The analytical minimum is at x = -b/2a = -4/2 = -2
print("\nAnalytical minimum:")
print(f"x = -2")
print(f"f(x) = {f(-2):.6f}")