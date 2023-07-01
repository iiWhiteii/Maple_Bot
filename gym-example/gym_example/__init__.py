from gym.envs.registration import register

register(
    id= "gym_examples/BasicEnv-v0",
    entry_point ="gym_example.envs:BasicEnv",
)


