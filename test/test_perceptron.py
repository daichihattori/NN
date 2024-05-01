import pytest
from src import perceptron
def test_AND():
    assert perceptron.AND(0, 0) == 0
    assert perceptron.AND(0, 1) == 0
    assert perceptron.AND(1, 0) == 0
    assert perceptron.AND(1, 1) == 1

def test_OR():
    assert perceptron.OR(0, 0) == 0
    assert perceptron.OR(0, 1) == 1
    assert perceptron.OR(1, 0) == 1
    assert perceptron.OR(1, 1) == 1

def test_NAND():
    assert perceptron.NAND(0, 0) == 1
    assert perceptron.NAND(0, 1) == 1
    assert perceptron.NAND(1, 0) == 1
    assert perceptron.NAND(1, 1) == 0

def test_XOR():
    assert perceptron.XOR(0, 0) == 0
    assert perceptron.XOR(0, 1) == 1
    assert perceptron.XOR(1, 0) == 1
    assert perceptron.XOR(1, 1) == 0