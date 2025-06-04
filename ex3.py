import gurobipy as gp
from gurobipy import GRB
import numpy as np
import scipy

def solver (a, b,c):
    constraint_mat = a # m x n matrix
    constraints = b # m vector
    objective = c # n vector

    model = gp.Model("matrix1")
    x = model.addMVar(shape=np.shape(c)[0], lb="0", name="x")
    model.setObjective(objective @ x, GRB.MAXIMIZE)
    model.addConstr(constraint_mat @ x <= constraints, name="c")
    model.optimize()

    if model.status == GRB.OPTIMAL:
        print("Optimal solution found:")
        for v in model.getVars():
            print(f"{v.VarName, v.X}")
        print(f"Objective value = {model.ObjVal}")
    else:
        print("No optimal solution found.")

a = np.array(
    [[3,5,9,7,4,6],
    [1,1,7,6,2,3],
    [7,5,8,0,6,1],
    [6,7,3,3,1,3],
    [6,5,8,4,0,0],
    [3,1,6,5,7,4]]
)
c = np.array([6,7,7,3,6,8])
b = np.array([10,10,10,10,10,10]) * c
solver(a,b,c)