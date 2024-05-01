import numpy as np

def perceptron(w:np.ndarray, x:np.ndarray, b:float) -> np.ndarray:
    return np.sum(w*x) + b > 0 

def AND(x1:int, x2:int) -> int:
    return perceptron(np.array([0.5, 0.5]), np.array([x1, x2]), -0.7)

def OR(x1:int, x2:int) -> int:
    return perceptron(np.array([0.5, 0.5]), np.array([x1, x2]), -0.2)

def NAND(x1:int, x2:int) -> int:
    return perceptron(np.array([-0.5, -0.5]), np.array([x1, x2]), 0.7)