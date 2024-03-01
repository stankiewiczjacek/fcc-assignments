import numpy as np

def calculate(list):

    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")
    matrix0 = np.resize(list, (3, 3))
    # print(matrix0)
    m = [(matrix0.mean(axis=0)).tolist(), (matrix0.mean(axis=1)).tolist(), matrix0.mean().tolist()]
    v = [(matrix0.var(axis=0)).tolist(), (matrix0.var(axis=1)).tolist(), matrix0.var().tolist()]
    sd = [(matrix0.std(axis=0)).tolist(), (matrix0.std(axis=1)).tolist(), matrix0.std().tolist()]
    mx = [(matrix0.max(axis=0)).tolist(), (matrix0.max(axis=1)).tolist(), matrix0.max().tolist()]
    mn = [(matrix0.min(axis=0)).tolist(), (matrix0.min(axis=1)).tolist(), matrix0.min().tolist()]
    s = [(matrix0.sum(axis=0)).tolist(), (matrix0.sum(axis=1)).tolist(), matrix0.sum().tolist()]

    calculations = {
        'mean': m,
        'variance': v,
        'standard deviation': sd,
        'max': mx,
        'min': mn,
        'sum': s,
    }

    return calculations
