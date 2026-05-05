import tensorflow as tf
from unet import UNet
from real_dataset_loader import load_real_data

# Dice Loss
def dice_loss(y_true, y_pred):
    smooth = 1e-6
    intersection = tf.reduce_sum(y_true * y_pred)
    return 1 - (2. * intersection + smooth) / (
        tf.reduce_sum(y_true) + tf.reduce_sum(y_pred) + smooth
    )

# Load data
X_train, y_train = load_real_data()

print("Training samples:", X_train.shape[0])

# Build model
model = UNet((256, 256, 1))

model.compile(
    optimizer="adam",
    loss=dice_loss,
    metrics=["accuracy"]
)

# Train
model.fit(X_train, y_train, epochs=10, batch_size=1)

# Save model
model.save("forest_model")
print("Model saved successfully.")
