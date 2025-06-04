import gurobipy as gp
from gurobipy import GRB
import numpy as np

# initialize model
m = gp.Model("mip1")

# Create variables
x_c = m.addVar(name="Xc", lb=0)
x_o = m.addVar(name="Xo", lb=0)
x_w = m.addVar(name="Xw", lb=0)
x_f = m.addVar(name="Xf", lb=0)

# Set the objective function min(z)
m.setObjective(0.17*x_c + 0.25*x_o + 0.20*x_w + 0.02*x_f, GRB.MAXIMIZE)

# Add constraints to the model
m.addConstr(x_f + x_c + x_o + x_w == 1, name="c0")
m.addConstr(0.2*x_c + 0.3*x_o + 0.1*x_w - 0.02*x_f <= 0.2, name="c1")
m.addConstr(x_c + x_o <= 0.5, name="c2")
m.addConstr(x_o + x_w <= 0.30, name="c3")

# run the model
m.optimize()

# Print the results
if m.status == GRB.OPTIMAL:
    print("Optimal solution found:")
    print(f"Xc = {x_c.X}")
    print(f"Xo = {x_o.X}")
    print(f"Xw = {x_w.X}")
    print(f"Xf = {x_f.X}")
    print(f"Objective value = {m.ObjVal}")

    # get the dual and slack variables
    dualvars = np.array(m.getAttr(GRB.Attr.Pi))
    slack = np.array(m.getAttr(GRB.Attr.Slack))

    print(f"Dual variables: {dualvars}")
    print(f"Slack variables: {slack}")
    



else:
    print("No optimal solution found.")