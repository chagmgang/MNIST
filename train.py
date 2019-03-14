import argparse
import numpy as np
import tensorflow as tf
from tensorflow.python.keras.layers import *

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", type=str, required=True)
    parser.add_argument("--epoch", type=int, required=True)
    parser.add_argument("--batch", type=int, required=True)
    parser.add_argument("--savefile", type=str, required=True)
    args = parser.parse_args()

    mnist = np.load(args.data)
    train_x, train_y = mnist['x'], mnist['y']
    train_x = np.expand_dims(train_x, -1) / 255.0

    model = tf.keras.models.Sequential([
        Conv2D(32, (3, 3), activation='relu'),
        Conv2D(64, (3, 3), activation='relu'),
        MaxPool2D(pool_size=(2,2)),
        Dropout(0.25),
        Flatten(),
        Dropout(0.5),
        Dense(10, activation='softmax')
    ])
    model.compile(optimizer='adam',
                  loss='sparse_categorical_crossentropy', metrics=['accuracy'])
    model.fit(x=train_x, y=train_y, epochs=args.epoch, verbose=1, batch_size=args.batch)
    tf.keras.models.save_model(model, args.savefile)