import numpy as np

def swish(x: list) -> np.ndarray:
    """Return Swish applied elementwise to x."""
    x = np.asarray(x, dtype=float)
    return x*(1 / (1 + np.exp(-x)))
    pass