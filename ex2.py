import gurobipy as gp
from gurobipy import GRB

# initialize model
m = gp.Model("mip1")

# Create variables
x_ns = m.addVar(name="x_ns", lb=0)
x_c = m.addVar(name="x_c", lb=0)
x_as = m.addVar(name="x_as", lb=0)
x_t = m.addVar(name="x_t", lb=0)
x_v = m.addVar(name="x_v", lb=0)

# Set the objective function min(z)
m.setObjective(8*x_ns + 6*x_c + 20*x_v + 10*x_as + 5*x_t, GRB.MINIMIZE)

# Add constraints to the model
m.addConstr(x_ns >= 2*x_as)
m.addConstr(40*x_ns + 70*x_c + 100*x_as + 60*x_t <= 250)
m.addConstr(40*x_ns + 70*x_c + 100*x_as + 60*x_t >= 200)
m.addConstr(10*x_ns + 10*x_c + 2*x_t + 40*x_v >= 20)
m.addConstr(55*x_c + 30 * x_t <= 0.45*(40*x_ns + 70 * x_c + 100*x_as + 60*x_t))
m.addConstr(55*x_c + 30 * x_t >= 0.15*(40*x_ns + 70 * x_c + 100*x_as + 60*x_t))
m.addConstr(6*x_c + 20*x_t == 12)

# run the model
m.optimize()

# Print the results
if m.status == GRB.OPTIMAL:
    print("Optimal solution found:")
    print(f"Xas = {x_as.X}")
    print(f"Xns = {x_ns.X}")
    print(f"Xc = {x_c.X}")
    print(f"Xt = {x_t.X}")
    print(f"Xv = {x_v.X}")
    print(f"Objective value = {m.ObjVal}")
else:
    print("No optimal solution found.")