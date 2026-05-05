import tensorflow as tf
from tensorflow.keras.layers import *

def UNet(input_shape):
    inputs = Input(input_shape)

    c1 = Conv2D(64, 3, activation="relu", padding="same")(inputs)
    c1 = Conv2D(64, 3, activation="relu", padding="same")(c1)
    p1 = MaxPooling2D()(c1)

    c2 = Conv2D(128, 3, activation="relu", padding="same")(p1)
    c2 = Conv2D(128, 3, activation="relu", padding="same")(c2)
    p2 = MaxPooling2D()(c2)

    b = Conv2D(256, 3, activation="relu", padding="same")(p2)

    u1 = UpSampling2D()(b)
    u1 = Concatenate()([u1, c2])
    c3 = Conv2D(128, 3, activation="relu", padding="same")(u1)

    u2 = UpSampling2D()(c3)
    u2 = Concatenate()([u2, c1])
    c4 = Conv2D(64, 3, activation="relu", padding="same")(u2)

    outputs = Conv2D(1, 1, activation="sigmoid")(c4)

    return tf.keras.Model(inputs, outputs)
