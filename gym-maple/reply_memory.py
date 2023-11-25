from collections import deque
import numpy as np

class ReplayMemory:
    def __init__(self, max_size):
        self.memory = deque(maxlen=max_size)

    def add_experience(self, experience):
        self.memory.append(experience)

    def sample_experiences(self, batch_size):
        indices = np.random.randint(len(self.memory), size=batch_size)
        batch = [self.memory[index] for index in indices]
        return [np.array([experience[field_index] for experience in batch]) for field_index in range(len(batch[0]))]

