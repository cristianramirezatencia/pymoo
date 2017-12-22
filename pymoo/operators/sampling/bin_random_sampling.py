from pymoo.model import random


class BinaryRandomSampling:
    """
    Randomly sample a binary representation of 0's and 1's.
    """

    def sample(self, problem, n_samples, data):
        return random.randint(0, 1, size=(n_samples, problem.n_var))
