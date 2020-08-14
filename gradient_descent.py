import numpy as np

########################################################
# Modeling: what we want to compute

# points = [(np.array([2]),4), (np.array([4]), 2)]
# dimensions = 1

# Generate artificial data
w_true = [1,2,3,4,5]
dimensions = len(w_true)
points = []


for i in range(1000):
    x = np.random.randn(5)
    y = w_true @ x + np.random.rand()
    points.append((x,y))

def cost(w):

    errors = sum((w @ x - y)**2 for x,y in points)
    cost = errors/len(points)
    return cost

def derivative_cost(w):

    gradient = sum(2*(w @ x - y) * x for x, y in points)

    return gradient / len(points)

########################################################3#
# Algorithms: how we compute it
# Gradient descent

def gradient_descent(cost, derivative_cost, dimensions):

    w = np.zeros(dimensions)
    learning_rate = 0.01

    for t in range (1000):

        # calculate the gradient
        gradientW = derivative_cost(w)
        # change w
        w = w - learning_rate * gradientW

    print("weights:", w)
    print("cost:", cost(w))


gradient_descent(cost, derivative_cost, dimensions = dimensions)


