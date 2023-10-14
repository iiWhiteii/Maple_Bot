import gym
import numpy as np
import tensorflow as tf
from tensorflow import keras
from collections import deque
import pydirectinput

import time

class DQN:
    def __init__(self, input_shape, n_outputs, learning_rate=1e-3, discount_rate=0.95, batch_size=32):
        self.input_shape = input_shape
        self.n_outputs = n_outputs
        self.batch_size = batch_size
        self.discount_rate = discount_rate

        # Create the DQN model
        self.model = self.build_model()

        # Initialize replay memory
        self.replay_memory = deque(maxlen=2000)

        # Create optimizer and loss function
        self.optimizer = keras.optimizers.Adam(learning_rate=learning_rate)
        self.loss_fn = keras.losses.mean_squared_error

    def build_model(self):
        model = keras.models.Sequential([
            keras.layers.Dense(128, activation="elu", input_shape=self.input_shape),
            keras.layers.Dense(64, activation="elu"),
            keras.layers.Dense(self.n_outputs)
        ])
        return model

    def epsilon_greedy_policy(self, state, epsilon):
        if np.random.rand() < epsilon:
            return np.random.randint(self.n_outputs)
        else:
            Q_values = self.model.predict(state[np.newaxis])
            return np.argmax(Q_values[0])

    def training_step(self):
        states, actions, rewards, next_states = self.sample_experiences()
        next_Q_values = self.model.predict(next_states)
        max_next_Q_values = np.max(next_Q_values, axis=1)
        target_Q_values = rewards + (self.discount_rate * max_next_Q_values)
        mask = tf.one_hot(actions, self.n_outputs)
        
        with tf.GradientTape() as tape:
            all_Q_values = self.model(states)
            Q_values = tf.reduce_sum(all_Q_values * mask, axis=1, keepdims=True)
            loss = tf.reduce_mean(self.loss_fn(target_Q_values, Q_values))
        
        grads = tape.gradient(loss, self.model.trainable_variables)
        self.optimizer.apply_gradients(zip(grads, self.model.trainable_variables))

        






    