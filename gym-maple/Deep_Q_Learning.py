

import tensorflow as tf 
import numpy as np
from collections import deque

class Deep_Q_Model:
    def __init__(self,input_shape,n_outputs,env,replay_buffer): 
        self.replay_buffer = deque(maxlen=2000)
        self.env = env
        self.input_shape = [input_shape]
        self.n_outputs = n_outputs

    # epsilon greedy policy
    def random_action(self,state,epsilon=0): 

        model = tf.keras.models.Sequential([
                tf.keras.layers.Dense(32, activation="elu", input_shape=self.input_shape),
                tf.keras.layers.Dense(32, activation="elu"),
                tf.keras.layers.Dense(self.n_outputs)
                ]) 
    
        #print(self.input_shape)    
        self.state = state
        if np.random.rand() < epsilon:
            return np.random.randint(self.n_outputs)
        else:
            Q_values = model.predict(state(np.newaxis),verbose=0)[0]
        return model, Q_values 
    
    

    # We're saving this function for later because we will be appending 
    # state, action, reward, next_state, done, truncated
    # then we will be randomly sampling them

    def sample_experience(self,batch_size):
        indicies = np.random.randint( len(self.replay_buffer), size = batch_size) 
        batch = [self.replay_buffer[index] for index in indicies]
        return [      
             np.array([experience[field_index] for experience in batch]) 
                for field_index in range(6)
                ]
    
    def play_one_step(self,random_action):
        # do random_action
        self.random_action = random_action(self.state,epsilon=0)
        #this will trigger our open gym
        next_state, reward, done, truncated, info = self.env.step(random_action) 
        self.replay_buffer.append(next_state,reward,done,truncated,info)

    
    
        






    