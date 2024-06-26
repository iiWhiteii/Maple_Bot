import gym
import numpy as np
import tensorflow as tf
from tensorflow import keras
from collections import deque
import time
import pydirectinput as pdi
import os
from datetime import datetime 



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
        pdi.keyDown("down")
        press_and_release("alt")
        pdi.keyUp("down")
    elif action == 3:
        special_press_and_release("1")
    elif action == 4:
        press_and_release("right")
        press_and_release("q")
        press_and_release("2")
    elif action == 5:
        press_and_release("left")
        press_and_release("q")
        press_and_release("2")
   
    elif action == 6: 
        press_and_release("w")

        
    return action

class DQN:
    def __init__(self, input_shape, n_outputs):
       
        self.input_shape = input_shape
        self.n_outputs = n_outputs   

        self.model = self.build_model()
        self.target_network = self.build_target_network() 

        self.save_path = 'gym-maple\DQN_Weight\Weight'




        #self.optimizer = keras.optimizers.SGD(lr=1e-4)

        self.optimizer = keras.optimizers.Adam(lr=1e-5)
        self.loss_fn = keras.losses.mean_squared_error
        #self.loss_fn2 = keras.losses.sparse_categorical_crossentropy


    def build_model(self):
        model = keras.models.Sequential([
            keras.layers.Dense(1000, activation='relu', input_shape = self.input_shape), 
            keras.layers.Dense(464,activation='relu'),
            keras.layers.Dense(464, activation='relu'),
            keras.layers.Dense(432, activation='relu'),
            keras.layers.Dense(self.n_outputs)])
        return model 
    

    def build_target_network(self): 
        target_network = keras.models.Sequential([
            keras.layers.Dense(1000, activation='relu', input_shape = self.input_shape), 
            keras.layers.Dense(464,activation='relu'),
            keras.layers.Dense(464, activation='relu'),
            keras.layers.Dense(432, activation='relu'),
            keras.layers.Dense(self.n_outputs)])
        return target_network 

    

    def model_summary(self):
        return self.model.summary()
    

    def update_target_network(self):
        self.target_network.set_weights(self.model.get_weights())
        return self.target_network.set_weights(self.model.get_weights())
    


    def epsilon_greedy_policy(self,state,epsilon):
        self.epsilon = epsilon
        if np.random.rand() < self.epsilon:
            self.random_action = np.random.randint(7)
            perform_action(self.random_action)
            return self.random_action
        
        else:
            #if np.random.rand() < 0.3:
                ''' sometimes the action don't get detected'''
                # Use the target network for exploration (optional)
              #  self.Q_values = self.target_network.predict(state[np.newaxis])
               # self.best_action = np.argmax(self.Q_values[0])
              #  perform_action(self.best_action)
            #if
                self.Q_values = self.model.predict(state[np.newaxis])
                self.best_action = np.argmax(self.Q_values[0])
                perform_action(self.best_action)

                return self.best_action
        
        
        
    def training_step(self,discount_rate,sample_experiences):
        #  Essential Part For Agent Learning  

        self.current_states, self.actions, self.rewards, self.next_states = sample_experiences
        self.actions = np.array(self.actions)
        self.rewards = np.array(self.rewards)
        
        
        
        #self.next_Q_values = self.model.predict(self.next_states)
        #self.max_Q_values = np.max(self.next_Q_values,axis=1)
        #self.target_Q_values = self.rewards + (discount_rate * self.max_Q_values)

       #Testing out Target Q Network
        self.selected_actions = np.argmax(self.model.predict(self.next_states), axis=1)
        self.target_Q_values = self.target_network.predict(self.next_states)
        self.target_Q_values = self.target_Q_values[np.arange(self.target_Q_values.shape[0]), self.selected_actions]



        self.target_Q_values = self.rewards + (discount_rate * self.target_Q_values)


        self.mask = tf.one_hot(self.actions, 7)
        
        
        with tf.GradientTape() as tape:
            self.all_Q_values = self.model(self.current_states)
            self.Q_values = tf.reduce_sum(self.all_Q_values * self.mask, axis=1, keepdims=True)
            self.loss = tf.reduce_mean(self.loss_fn(self.target_Q_values, self.Q_values))   

        self.grads = tape.gradient(self.loss, self.model.trainable_variables)
        self.optimizer.apply_gradients(zip(self.grads, self.model.trainable_variables))
       
        if self.save_path is not None:
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            self.weights_filename = f'weights_{timestamp}.h5'
            self.weights_path = os.path.join(self.save_path, self.weights_filename)
            self.model.save_weights(self.weights_path)


        return self.loss






























    
    '''def training_step(self, discount_rate, sample_experiences):
        self.current_states, self.actions, self.rewards, self.next_states = sample_experiences
        self.actions = np.array(self.actions)
        self.rewards = np.array(self.rewards)

        # Get target Q values from the target network
        target_next_Q_values = self.target_network.predict(self.next_states)
    
        # Use the same mask technique for both current and target Q values
        mask_current = tf.one_hot(self.actions, 6)
        mask_target = tf.one_hot(np.argmax(target_next_Q_values, axis=1), 6)
    
        with tf.GradientTape() as tape:
            all_Q_values = self.model(self.current_states)
            Q_values_current = tf.reduce_sum(all_Q_values * mask_current, axis=1, keepdims=True)
            target_Q_values = self.rewards + (discount_rate * tf.reduce_sum(target_next_Q_values * mask_target, axis=1, keepdims=True))
            self.loss = tf.reduce_mean(self.loss_fn(target_Q_values, Q_values_current))

        self.grads = tape.gradient(self.loss, self.model.trainable_variables)
        self.optimizer.apply_gradients(zip(self.grads, self.model.trainable_variables))

        return self.loss'''




# Test this if it actually works 

   '''' def training_step(self,discount_rate,sample_experiences):
        #  Essential Part For Agent Learning  

        self.current_states, self.actions, self.rewards, self.next_states = sample_experiences
        self.actions = np.array(self.actions)
        self.rewards = np.array(self.rewards)
        
        
        
        #self.next_Q_values = self.model.predict(self.next_states)
        #self.max_Q_values = np.max(self.next_Q_values,axis=1)
        #self.target_Q_values = self.rewards + (discount_rate * self.max_Q_values)

       #Testing out Target Q Network
        self.selected_actions = np.argmax(self.model.predict(self.next_states), axis=1)
        self.target_Q_values = self.target_network.predict(self.next_states)
        self.target_Q_values = self.target_Q_values[np.arange(self.target_Q_values.shape[0]), self.selected_actions]



        self.target_Q_values = self.rewards + (discount_rate * self.target_Q_values)


        self.mask = tf.one_hot(self.actions, 7)
        
        
        with tf.GradientTape() as tape:
            self.all_Q_values = self.model(self.current_states)
            self.Q_values = tf.reduce_sum(self.all_Q_values * self.mask, axis=1, keepdims=True)
            self.loss = tf.reduce_mean(self.loss_fn(self.target_Q_values, self.Q_values))   

        self.grads = tape.gradient(self.loss, self.model.trainable_variables)
        self.optimizer.apply_gradients(zip(self.grads, self.model.trainable_variables))
       
        if self.save_path is not None:
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            self.weights_filename = f'weights_{timestamp}.h5'
            self.weights_path = os.path.join(self.save_path, self.weights_filename)
            self.model.save_weights(self.weights_path)


        return self.loss'''


    


        
        

    
        

    









    