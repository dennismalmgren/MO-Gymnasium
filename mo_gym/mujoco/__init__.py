from gym.envs.registration import register


register(
    id='mo-halfcheetah-v4',
    entry_point='mo_gym.mujoco.half_cheetah:MOHalfCheehtahEnv',
    max_episode_steps=1000,
)