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

def cost(w, i):
    x, y = points[i]
    errors = ((w @ x - y)**2)
    return errors

def stochastic_derivative_cost(w, i):
    x, y = points[i]
    gradient = (2*(w @ x - y) * x)

    return gradient

########################################################3#
# Algorithms: how we compute it
# Gradient descent

def stochastic_gradient_descent(cost, derivative_cost, dimensions):

    w = np.zeros(dimensions)
    learning_rate = 1
    numUpdates = 0
    for t in range (1000):
        for i in range(len(points)):
            # calculate the gradient
            gradient_w = stochastic_derivative_cost(w, i)
            numUpdates += 1
            learning_rate = 1 / numUpdates
            # change w
            w = w - learning_rate * gradient_w

    print("weights:", w)
    print("cost:", cost(w, len(points) -1))


stochastic_gradient_descent(cost, stochastic_derivative_cost, dimensions = dimensions)


