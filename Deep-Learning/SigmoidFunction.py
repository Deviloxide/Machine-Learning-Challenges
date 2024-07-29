import math

def sigmoid(z):
    denominator = 1 + math.exp(-z)
    result = 1 / denominator
    return round(result, 4)
