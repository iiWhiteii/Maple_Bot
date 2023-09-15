import gym
import numpy as np
import tensorflow as tf
from tensorflow import keras
from collections import deque

class Deep_Q_Model:
    def __init__(self, input_shape, n_outputs):
        self.input_shape = input_shape
        self.n_outputs = n_outputs
        self.model = self._build_model()

        # Initialize replay buffer
        self.replay_memory = deque(maxlen=2000)

        # Define constants
        self.batch_size = 32
        self.discount_rate = 0.95
        self.optimizer = keras.optimizers.Adam(lr=1e-3)
        self.loss_fn = keras.losses.mean_squared_error

    def _build_model(self):
        model = tf.keras.models.Sequential([
            tf.keras.layers.Dense(32, activation="elu", input_shape=np.array(self.input_shape)),
            tf.keras.layers.Dense(32, activation="elu"),
            tf.keras.layers.Dense(self.n_outputs)
        ])
        return model

    def epsilon_greedy_policy(self, state, epsilon=0):
        if np.random.rand() < epsilon:
            return np.random.randint(self.n_outputs)
        else:
            Q_values = self.model.predict(state[np.newaxis])
            return np.argmax(Q_values[0])

    def sample_experiences(self, batch_size):
        indices = np.random.randint(len(self.replay_memory), size=batch_size)
        batch = [self.replay_memory[index] for index in indices]
        states, actions, rewards, next_states, dones, truncateds = [
            np.array([experience[field_index] for experience in batch])
            for field_index in range(6)]
        return states, actions, rewards, next_states, dones, truncateds

    def play_one_step(self, env, state, epsilon):
        action = self.epsilon_greedy_policy(state, epsilon)
        next_state, reward, done, truncated, info = env.step(action)
        memory = state, action, reward, next_state, done, truncated
        self.replay_memory.append((memory))
        return next_state, reward, done, truncated, info

    def training_step(self):
        experiences = self.sample_experiences(self.batch_size)
        states, actions, rewards, next_states, dones, truncateds = experiences
        next_Q_values = self.model.predict(next_states)
        max_next_Q_values = np.max(next_Q_values, axis=1)
        target_Q_values = rewards + (1 - dones) * self.discount_rate * max_next_Q_values
        mask = tf.one_hot(actions, self.n_outputs)
        with tf.GradientTape() as tape:
            all_Q_values = self.model(states)
            Q_values = tf.reduce_sum(all_Q_values * mask, axis=1, keepdims=True)
            loss = tf.reduce_mean(self.loss_fn(target_Q_values, Q_values))
        grads = tape.gradient(loss, self.model.trainable_variables)
        self.optimizer.apply_gradients(zip(grads, self.model.trainable_variables))

    
        






    