import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def dsigmoid(y):
    return y * (1.0 - y)

class MLP_NeuralNetwork(object):
    def __init__(self, input, hidden, output):
        self.input = input + 1
        self.hidden = hidden
        self.output = output
        self.ai = [1.0] * self.input
        self.ah = [1.0] * self.hidden
        self.ao = [1.0] * self.output
        self.wi = np.random.randn(self.input, self.hidden)
        self.wo = np.random.randn(self.hidden, self.output)
        self.ci = np.zeros((self.input, self.hidden))
        self.co = np.zeros((self.hidden, self.output))

    def feedForward(self, inputs):
        if len(inputs) != self.input - 1:
            raise ValueError('Wrong number of inputs you silly goose!')
        for i in range(self.input - 1):
            self.ai[i] = inputs[i]
        for j in range(self.hidden):
            sum = 0.0
            for i in range(self.input):
                sum += self.ai[i] * self.wi[i][i]
            self.ah[j] = sigmoid(sum)
        for k in range(self.output):
            sum = 0.0
            for j in range(self.hidden):
                sum += self.ah[j] * self.wo[j][k]
            self.ao[k] = sigmoid(sum)
        return self.ao[:]

    def backPropagate(self, targets, N):
        """
        :param targets: y values
        :param N: learning rate
        :return: updated weights and current error
        """
        if len(targets) != self.output:
            raise ValueError('Wrong number of targets you silly goose!')
        # calculate error terms for output
        # the delta tell you which direction to change the weights
        output_deltas = [0.0] * self.output
        for k in range(self.output):
            error = -(targets[k] - self.ao[k])
            output_deltas[k] = dsigmoid(self.ao[k]) * error
        # calculate error terms for hidden
        # delta tells you which direction to change the weights
        hidden_deltas = [0.0] * self.hidden
        for j in range(self.hidden):
            error = 0.0
            for k in range(self.output):
                error += output_deltas[k] * self.wo[j][k]
            hidden_deltas[j] = dsigmoid(self.ah[j]) * error
        # update the weights connecting hidden to output
        for j in range(self.hidden):
            for k in range(self.output):
                change = output_deltas[k] * self.ah[j]
                self.wo[j][k] -= N * change + self.co[j][k]
                self.co[j][k] = change
        # update the weights connecting input to hidden
        for i in range(self.input):
            for j in range(self.hidden):
                change = hidden_deltas[j] * self.ai[i]
                self.wi[i][j] -= N * change + self.ci[i][j]
                self.ci[i][j] = change
        # calculate error
        error = 0.0
        for k in range(len(targets)):
            error += 0.5 * (targets[k] - self.ao[k]) ** 2
        return error

    def train(self, patterns, iterations=3000, N=0.0002):
        # N: learning rate
        for i in range(iterations):
            error = 0.0
            for p in patterns:
                inputs = p[0]
                targets = p[1]
                self.feedForward(inputs)
                error = self.backPropagate(targets, N)
            if i % 500 == 0:
                print('error %-.5f' % error)

    def predict(self, X):
        """
        return list of predictions after training algorithm
        """
        predictions = []
        for p in X:
            predictions.append(self.feedForward(p))
        return predictions


def demo():
    """
    run NN demo on the digit recognition dataset from sklearn
    """

    def load_data():
        data = np.loadtxt('Data/sklearn_digits.csv', delimiter=',')

        # first ten values are the one hot encoded y (target) values
        y = data[:, 0:10]
        # y[y == 0] = -1 # if you are using a tanh transfer function make the 0 into -1
        # y[y == 1] = .90 # try values that won't saturate tanh

        data = data[:, 10:]  # x data
        # data = data - data.mean(axis = 1)
        data -= data.min()  # scale the data so values are between 0 and 1
        data /= data.max()  # scale

        out = []
        print(data.shape)

        # populate the tuple list with the data
        for i in range(data.shape[0]):
            fart = list((data[i, :].tolist(), y[i].tolist()))  # don't mind this variable name
            out.append(fart)

        return out

    X = load_data()

    print(X[9])  # make sure the data looks right

    NN = MLP_NeuralNetwork(64, 100, 10, iterations=50, learning_rate=0.5, momentum=0.5, rate_decay=0.01)

    NN.train(X)

    NN.test(X)


if __name__ == '__main__':
    demo()