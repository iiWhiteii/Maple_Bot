from gym.envs.registration import register

register(
    id= "gym_maple/MapleEnv-v0",
    entry_point ="gym_maple.envs:MapleEnv",
)


