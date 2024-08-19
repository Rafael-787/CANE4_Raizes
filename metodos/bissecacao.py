from sympy import *

# Define the variable
x = symbols('x')

# Define the equation, e.g., x^2 - 4 = 0
equation = Eq(x**2 - 4, 0)
expr = x**2 -4

# Solve the equation
solutions = solve(equation, x)

print(solutions)

a = expr.subs(x,3).evalf()
print(a)
