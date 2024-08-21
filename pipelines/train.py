import tensorflow as tf
from tensorflow.keras import layers, models

from services.process_data import get_data, read_labels_file

train_images = get_data("train-images.idx3-ubyte")
train_labels = read_labels_file("train-labels.idx1-ubyte")

model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.Flatten(),
    layers.Dense(64, activation='relu'),
    layers.Dense(10, activation='softmax')  # 10 output classes for digits 0-9
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

model.fit(train_images, train_labels, epochs=5, batch_size=64, validation_split=0.2)

test_loss, test_acc = model.evaluate(train_images, train_labels)
print(f'Test accuracy: {test_acc}')

model.save('digit_recognition_model.h5')
