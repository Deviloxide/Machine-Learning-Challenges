import math

def softmax(scores):
    probabilities = []
    for score in scores:
        probability = math.exp(score)
        probabilities.append(probability)
    num_scores = len(scores)
    total = sum(probabilities)
    for i in range(num_scores):
        probabilities[i] = round(probabilities[i] / total, 4)
    return probabilities
