import numpy as np

X = np.array(([2, 9], [1, 5], [3, 7]), dtype=float)
Y = np.array(([92], [86], [89]), dtype=float)
X = X / np.amax(X, axis=0)
Y = Y / 100

def sigmoid(x):
    return (1 / (1 + np.exp(-x)))


def derivatives_sigmoid(x):
    return x * (1 - x)


epoch = 5000
lr = 0.1
input_neurons = 2
hidden_neurons = 3
output_neurons = 1

# Weight and bias
wh = np.random.uniform(size=(input_neurons, hidden_neurons))
bh = np.random.uniform(size=(1, hidden_neurons))
wout = np.random.uniform(size=(hidden_neurons, output_neurons))
bout = np.random.uniform(size=(1, output_neurons))

for i in range(epoch):
    # Forward propogation
    hinp1 = np.dot(X, wh)
    hinp = hinp1 + bh
    hlayer_act = sigmoid(hinp)

    oinp1 = np.dot(hlayer_act, wout)
    oinp = oinp1 + bout
    output = sigmoid(oinp)

    # Backpropogation
    EO = Y - output
    out_gradient = derivatives_sigmoid(output)
    d_output = EO * out_gradient

    EH = d_output.dot(wout.T)
    h_gradient = derivatives_sigmoid(hlayer_act)
    d_hidden = EH * h_gradient

    wout += (hlayer_act.T.dot(d_output)) * lr
    wh += (X.T.dot(d_hidden)) * lr

print(f"Input = {X}")
print(f"Output = {Y}")
print(f"Predicted = {output}")
