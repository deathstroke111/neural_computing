import numpy as np

def alpham(v):
    theta = (v + 45) / 10
    out = theta / (1 - np.exp(-theta))
    out = np.where(np.isnan(out), 1.0, out)
    return out

def betam(v):
    theta = (v + 70) / 18
    return 4.0 * np.exp(-theta)

def alphah(v):
    theta = (v + 70) / 20
    return 0.07 * np.exp(-theta)

def betah(v):
    theta = (v + 40) / 10
    return 1 / (1 + np.exp(-theta))

def alphan(v):
    theta = (v + 60) / 10
    out = 0.1 * theta / (1 - np.exp(-theta))
    out = np.where(np.isnan(out), 0.1, out)
    return out

def betan(v):
    theta = (v + 70) / 80
    return 0.125 * np.exp(-theta)

def alphah_double(v):
    theta = (v + 70) / 20
    return 2 * 0.07 * np.exp(-theta)
