import pickle
import tensorflow as tf

with open("Data/Model_input/features.pkl", "rb") as f:
    X = pickle.load(f)
with open("Data/Model_input/results.pkl", "rb") as f:
    Y = pickle.load(f)
print(X)
print(Y)

feature_vec_dim = len(X[0][0])
number_of_classes = 3 # Home/away win and draw

# Define LSTM model
model = tf.keras.Sequential([
    tf.keras.layers.LSTM(16, input_shape=(10, feature_vec_dim)),
    tf.keras.layers.Dense(number_of_classes, activation='softmax')
])

# Compile model
model.compile(loss='mse', optimizer='adam')