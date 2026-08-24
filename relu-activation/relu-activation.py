import numpy as np

def relu(x) -> np.ndarray:
    """Return ReLU applied elementwise to x."""
    return np.asarray(np.maximum(0,x), dtype=float)