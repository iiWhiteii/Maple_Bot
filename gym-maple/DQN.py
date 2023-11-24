import gym
import numpy as np
import tensorflow as tf
from tensorflow import keras
from collections import deque
import time
import pydirectinput as pdi


def press_and_release(key, duration=0.1):
    pdi.keyDown(key)
    time.sleep(duration)
    pdi.keyUp(key)

def special_press_and_release(key):
    pdi.keyDown(key)
    pdi.keyUp(key)




def perform_action(action):
    if action == 0:
        press_and_release("left")
        press_and_release("alt")
        press_and_release("alt")
    elif action == 1:
        press_and_release("right")
        press_and_release("alt")
        press_and_release("alt")
    elif action == 2:
        special_press_and_release("up")
        special_press_and_release("w")
    elif action == 3:
        special_press_and_release("down")
        special_press_and_release("w")
    elif action == 4:
        press_and_release("right")
        press_and_release("q")
    elif action == 5:
        press_and_release("left")
        press_and_release("q")

    return action










class DQN:
    def __init__(self, reply_memory, input_shape, n_outputs,epsilon):
        self.epsilon = epsilon
        self.input_shape = input_shape
        self.n_outputs = n_outputs        
        self.model = self.build_model()
        

        self.reply_memory = reply_memory # THINKING OF HAVING REPLY_MEMORY ON SERPARATE FILES




        self.optimizer = keras.optimizers.Adam(lr=1e-3)
        self.loss_fn = keras.losses.mean_squared_error


    def build_model(self):
        model = keras.models.Sequential([
            keras.layers.Dense(128, activation='elu', input_shape = self.input_shape), 
            keras.layers.Dense(64,activation='elu'),
            keras.layers.Dense(32, activation='elu'),
            keras.layers.Dense(6)])
        return model 
    

    def epsilon_greedy_policy(self,state):
        if np.random.rand() < self.epsilon:
            self.random_action = np.random.randint(6)
            perform_action(self.random_action)
            return self.random_action
        
        else:
            self.Q_values = self.model.predict(state[np.newaxis])
            self.best_action = np.argmax(self.Q_values[0])
            perform_action(self.best_action)
            return self.best_action
        


    def training_step(self,batch_size,discount_rate,sample_experiences):
        '''  Essential Part For Agent Learning    '''
        
        self.current_states, self.actions, self.rewards, self.next_states = sample_experiences(batch_size)
        self.actions = np.array(self.actions)
        self.rewards = np.array(self.rewards)
        self.next_Q_values = self.model.predict(self.next_states)
        self.max_Q_values = np.max(self.next_Q_values,axis=1)
        self.target_Q_values = self.rewards + (discount_rate * self.next_Q_values )
        self.mask = tf.one_hot(self.actions, 6)
        
        
        with tf.GradientTape() as tape:
            self.all_Q_values = self.model(self.current_states)
            self.Q_values = tf.reduce_sum(self.all_Q_values * self.mask, axis=1, keepdims=True)
            self.loss = tf.reduce_mean(self.loss_fn(self.target_Q_values, self.Q_values))   

        self.grads = tape.gradient(self.loss, self.model.trainable_variables)
        self.optimizer.apply_gradients(zip(self.grads, self.model.trainable_variables))
    


        
        

    
        

    









    