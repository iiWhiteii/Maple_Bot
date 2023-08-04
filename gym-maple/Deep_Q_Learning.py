
import tensorflow as tf
import numpy as np
from collections import deque

class Deep_Q_Model:
    def __init__(self, input_shape, n_outputs):
        self.input_shape = input_shape
        self.n_outputs = n_outputs
        self.model = self._build_model()

        # Initialize replay buffer
        self.replay_buffer = deque(maxlen=2000)

    def _build_model(self):
        model = tf.keras.models.Sequential([
            tf.keras.layers.Dense(32, activation="elu", input_shape=self.input_shape),
            tf.keras.layers.Dense(32, activation="elu"),
            tf.keras.layers.Dense(self.n_outputs)
        ])
        return model

    def epsilon_greedy_policy(self, state, epsilon=0):
        if np.random.rand() < epsilon:
            return np.random.randint(self.n_outputs)  # random action
        else:
            Q_values = self.model.predict(state[np.newaxis], verbose=0)[0]
            return Q_values.argmax()

    def sample_experiences(self, batch_size):
        indices = np.random.randint(len(self.replay_buffer), size=batch_size)
        batch = [self.replay_buffer[index] for index in indices]


        
        return [
            np.array([experience[field_index] for experience in batch])
            for field_index in range(6)
        ]

    def play_one_step(self, env, state, epsilon):
        action = self.epsilon_greedy_policy(state, epsilon)
        next_state, reward, done, truncated, info = env.step(action)
        self.replay_buffer.append((state, action, reward, next_state, done, truncated))
        return next_state, reward, done, truncated, info 
    



    
        






    