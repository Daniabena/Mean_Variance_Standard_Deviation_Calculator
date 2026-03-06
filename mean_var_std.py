import numpy as np

def calculate(list):

    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    arr= np.array(list)
    grid= arr.reshape(3, 3)

    col_mean=grid.mean(axis=0).tolist()
    row_mean= grid.mean(axis=1).tolist()
    total_mean= grid.mean().tolist()

    col_var= grid.var(axis=0).tolist()
    row_var= grid.var(axis=1).tolist()
    total_var =grid.var().tolist()

    col_std= grid.std(axis=0).tolist()
    row_std=grid.std(axis=1).tolist()
    total_std= grid.std().tolist()

    col_max= grid.max(axis=0).tolist()
    row_max= grid.max(axis=1).tolist()
    total_max= grid.max().tolist()

    col_min=grid.min(axis=0).tolist()
    row_min=grid.min(axis=1).tolist()
    total_min= grid.min().tolist()

    col_sum= grid.sum(axis=0).tolist()
    row_sum =grid.sum(axis=1).tolist()
    total_sum=grid.sum().tolist()

    results={
        "mean":[col_mean, row_mean, total_mean],
        "variance":[col_var, row_var, total_var],
        "standard deviation":[col_std, row_std, total_std],
        "max":[col_max, row_max, total_max],
        "min":[col_min, row_min, total_min],
        "sum":[col_sum, row_sum, total_sum]
    }

    return results
