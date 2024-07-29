import SigmoidFunction as sigmoid


def single_neuron_model(features, labels, weights, bias):
    probabilities = []
    mse = 0
    num_features = len(features)
    for feature in range(num_features):
        z = 0
        num_weights = len(weights)
        for weight in range(num_weights):
            z += weights[weight] * features[feature][weight]
        z += bias
        probability = sigmoid.sigmoid(z)
        probabilities.append(probability)
        mse += 1 / num_features * (labels[feature] - probability) ** 2
    rounded_mse = round(mse, 4)
    return probabilities, rounded_mse
