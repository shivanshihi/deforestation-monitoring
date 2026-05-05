import numpy as np

def load_dummy_data():
    X_train = np.random.rand(20, 256, 256, 4)
    y_train = np.random.randint(0, 2, (20, 256, 256, 1))
    return X_train, y_train
